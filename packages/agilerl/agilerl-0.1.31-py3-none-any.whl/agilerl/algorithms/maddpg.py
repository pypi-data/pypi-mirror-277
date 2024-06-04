import copy
import inspect
import random
import warnings

import dill
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

from agilerl.networks.evolvable_cnn import EvolvableCNN
from agilerl.networks.evolvable_mlp import EvolvableMLP
from agilerl.utils.algo_utils import unwrap_optimizer
from agilerl.wrappers.make_evolvable import MakeEvolvable
from agilerl.wrappers.pettingzoo_wrappers import PettingZooVectorizationParallelWrapper


class MADDPG:
    """The MADDPG algorithm class. MADDPG paper: https://arxiv.org/abs/1706.02275

    :param state_dims: State observation dimensions for each agent
    :type state_dims: list[tuple]
    :param action_dims: Action dimensions for each agent
    :type action_dims: list[int]
    :param one_hot: One-hot encoding, used with discrete observation spaces
    :type one_hot: bool
    :param n_agents: Number of agents
    :type n_agents: int
    :param agent_ids: Agent ID for each agent
    :type agent_ids: list[str]
    :param max_action: Upper bound of the action space for each agent
    :type max_action: list[float]
    :param min_action: Lower bound of the action space for each agent
    :type min_action: list[float]
    :param discrete_actions: Boolean flag to indicate a discrete action space
    :type discrete_actions: bool, optional
    :param expl_noise: Standard deviation for Gaussian exploration noise, defaults to 0.1
    :type expl_noise: float, optional
    :param index: Index to keep track of object instance during tournament selection and mutation, defaults to 0
    :type index: int, optional
    :param net_config: Network configuration, defaults to mlp with hidden size [64,64]
    :type net_config: dict, optional
    :param batch_size: Size of batched sample from replay buffer for learning, defaults to 64
    :type batch_size: int, optional
    :param lr_actor: Learning rate for actor optimizer, defaults to 0.001
    :type lr_actor: float, optional
    :param lr_critic: Learning rate for critic optimizer, defaults to 0.01
    :type lr_critic: float, optional
    :param learn_step: Learning frequency, defaults to 5
    :type learn_step: int, optional
    :param gamma: Discount factor, defaults to 0.95
    :type gamma: float, optional
    :param tau: For soft update of target network parameters, defaults to 0.01
    :type tau: float, optional
    :param mutation: Most recent mutation to agent, defaults to None
    :type mutation: str, optional
    :param actor_networks: List of custom actor networks, defaults to None
    :type actor_networks: list[nn.Module], optional
    :param critic_networks: List of custom critic networks, defaults to None
    :type critic_networks: list[nn.Module], optional
    :param device: Device for accelerated computing, 'cpu' or 'cuda', defaults to 'cpu'
    :type device: str, optional
    :param accelerator: Accelerator for distributed computing, defaults to None
    :type accelerator: accelerate.Accelerator(), optional
    :param wrap: Wrap models for distributed training upon creation, defaults to True
    :type wrap: bool, optional
    """

    def __init__(
        self,
        state_dims,
        action_dims,
        one_hot,
        n_agents,
        agent_ids,
        max_action,
        min_action,
        discrete_actions,
        expl_noise=0.1,
        index=0,
        net_config={"arch": "mlp", "hidden_size": [64, 64]},
        batch_size=64,
        lr_actor=0.001,
        lr_critic=0.01,
        learn_step=5,
        gamma=0.95,
        tau=0.01,
        mut=None,
        actor_networks=None,
        critic_networks=None,
        device="cpu",
        accelerator=None,
        wrap=True,
    ):
        assert isinstance(state_dims, list), "State dimensions must be a list."
        assert isinstance(action_dims, list), "Action dimensions must be a list."
        assert isinstance(
            one_hot, bool
        ), "One-hot encoding flag must be boolean value True or False."
        assert isinstance(n_agents, int), "Number of agents must be an integer."
        assert isinstance(
            agent_ids, (tuple, list)
        ), "Agent IDs must be stores in a tuple or list."
        assert isinstance(
            discrete_actions, bool
        ), "Discrete actions flag must be a boolean value True or False."
        assert (
            isinstance(max_action, list) or max_action is None
        ), "Max action must be a list."
        assert (
            isinstance(min_action, list) or min_action is None
        ), "Min action must be a list."
        assert (max_action is not None) == (
            min_action is not None
        ), "Max and min actions must both be supplied, or both be None."
        if max_action is not None and min_action is not None:
            for x, n in zip(max_action, min_action):
                x, n = x[0], n[0]
                assert x > n, "Max action must be greater than min action."
                assert x > 0, "Max action must be greater than zero."
                assert n <= 0, "Min action must be less than or equal to zero."
        assert isinstance(index, int), "Agent index must be an integer."
        assert isinstance(batch_size, int), "Batch size must be an integer."
        assert batch_size >= 1, "Batch size must be greater than or equal to one."
        assert isinstance(lr_actor, float), "Actor learning rate must be a float."
        assert lr_actor > 0, "Actor learning rate must be greater than zero."
        assert isinstance(lr_critic, float), "Critic learning rate must be a float."
        assert lr_critic > 0, "Critic learning rate must be greater than zero."
        assert isinstance(learn_step, int), "Learn step rate must be an integer."
        assert learn_step >= 1, "Learn step must be greater than or equal to one."
        assert isinstance(gamma, float), "Gamma must be a float."
        assert isinstance(tau, float), "Tau must be a float."
        assert tau > 0, "Tau must be greater than zero."
        assert n_agents == len(
            agent_ids
        ), "Number of agents must be equal to the length of the agent IDs list."
        if (actor_networks is not None) != (critic_networks is not None):
            warnings.warn(
                "Actor and critic network lists must both be supplied to use custom networks. Defaulting to net config."
            )
        assert isinstance(
            wrap, bool
        ), "Wrap models flag must be boolean value True or False."

        self.algo = "MADDPG"
        self.state_dims = state_dims
        self.total_state_dims = sum(state_dim[0] for state_dim in self.state_dims)
        self.action_dims = action_dims
        self.one_hot = one_hot
        self.n_agents = n_agents
        self.multi = True
        self.agent_ids = agent_ids
        self.net_config = net_config
        self.batch_size = batch_size
        self.lr_actor = lr_actor
        self.lr_critic = lr_critic
        self.learn_step = learn_step
        self.gamma = gamma
        self.tau = tau
        self.mut = mut
        self.device = device
        self.accelerator = accelerator
        self.index = index
        self.scores = []
        self.fitness = []
        self.steps = [0]
        self.max_action = max_action
        self.expl_noise = expl_noise
        self.min_action = min_action
        self.discrete_actions = discrete_actions
        self.total_actions = sum(self.action_dims)
        self.actor_networks = actor_networks
        self.critic_networks = critic_networks

        if self.actor_networks is not None and self.critic_networks is not None:
            assert (
                len({type(net) for net in actor_networks}) == 1
            ), "'actor_networks' must all be the same type"
            assert (
                len({type(net) for net in critic_networks}) == 1
            ), "'critic_networks' must all be the same type"
            assert isinstance(
                actor_networks[0], type(critic_networks[0])
            ), "actor and critic networks must be the same type"
            self.actors = actor_networks
            self.critics = critic_networks
            if isinstance(self.actors[0], (EvolvableMLP, EvolvableCNN)) and isinstance(
                self.critics[0], (EvolvableMLP, EvolvableCNN)
            ):
                self.net_config = self.actors[0].net_config
            elif isinstance(self.actors[0], MakeEvolvable) and isinstance(
                self.critics[0], MakeEvolvable
            ):
                self.net_config = None
            else:
                assert (
                    False
                ), "'actor_networks' and 'critic_networks' must be lists of networks all of which must be the same  \
                                type and be of type EvolvableMLP, EvolvableCNN or MakeEvolvable"
        else:

            # model
            if self.net_config["arch"] == "mlp":  # Multi-layer Perceptron
                self.actors = []
                for idx, (action_dim, state_dim) in enumerate(
                    zip(self.action_dims, self.state_dims)
                ):
                    if "mlp_output_activation" not in self.net_config.keys():
                        if not self.discrete_actions:
                            if self.min_action[idx][0] < 0:
                                self.net_config["mlp_output_activation"] = "Tanh"
                            else:
                                self.net_config["mlp_output_activation"] = "Sigmoid"
                        else:
                            self.net_config["mlp_output_activation"] = "GumbelSoftmax"

                    self.actors.append(
                        EvolvableMLP(
                            num_inputs=state_dim[0],
                            num_outputs=action_dim,
                            device=self.device,
                            accelerator=self.accelerator,
                            **self.net_config,
                        )
                    )
                critic_net_config = copy.deepcopy(self.net_config)
                critic_net_config["mlp_output_activation"] = (
                    None  # Critic must have no output activation
                )
                self.critics = [
                    EvolvableMLP(
                        num_inputs=self.total_state_dims + self.total_actions,
                        num_outputs=1,
                        device=self.device,
                        accelerator=self.accelerator,
                        **critic_net_config,
                    )
                    for _ in range(self.n_agents)
                ]

            elif self.net_config["arch"] == "cnn":  # Convolutional Neural Network
                self.actors = []
                for idx, (action_dim, state_dim) in enumerate(
                    zip(self.action_dims, self.state_dims)
                ):
                    if "mlp_output_activation" not in self.net_config.keys():
                        if not self.discrete_actions:
                            if self.min_action[idx][0] < 0:
                                self.net_config["mlp_output_activation"] = "Tanh"
                            else:
                                self.net_config["mlp_output_activation"] = "Sigmoid"
                        else:
                            self.net_config["mlp_output_activation"] = "GumbelSoftmax"
                    self.actors.append(
                        EvolvableCNN(
                            input_shape=state_dim,
                            num_actions=action_dim,
                            multi=self.multi,
                            n_agents=self.n_agents,
                            device=self.device,
                            accelerator=self.accelerator,
                            **self.net_config,
                        )
                    )
                critic_net_config = copy.deepcopy(self.net_config)
                critic_net_config["mlp_output_activation"] = (
                    None  # Critic must have no output activation
                )
                self.critics = [
                    EvolvableCNN(
                        input_shape=state_dim,
                        num_actions=self.total_actions,
                        critic=True,
                        n_agents=self.n_agents,
                        multi=self.multi,
                        device=self.device,
                        accelerator=self.accelerator,
                        **critic_net_config,
                    )
                    for state_dim in self.state_dims
                ]

        # Assign architecture
        self.arch = (
            self.net_config["arch"]
            if self.net_config is not None
            else self.actors[0].arch
        )

        # Create target networks
        self.actor_targets = copy.deepcopy(self.actors)
        self.critic_targets = copy.deepcopy(self.critics)

        # Initialise target network parameters
        for actor, actor_target in zip(self.actors, self.actor_targets):
            actor_target.load_state_dict(actor.state_dict())
        for critic, critic_target in zip(self.critics, self.critic_targets):
            critic_target.load_state_dict(critic.state_dict())

        self.actor_optimizers = [
            optim.Adam(actor.parameters(), lr=self.lr_actor) for actor in self.actors
        ]
        self.critic_optimizers = [
            optim.Adam(critic.parameters(), lr=self.lr_critic)
            for critic in self.critics
        ]

        if self.accelerator is not None:
            if wrap:
                self.wrap_models()
        else:
            self.actors = [actor.to(self.device) for actor in self.actors]
            self.actor_targets = [
                actor_target.to(self.device) for actor_target in self.actor_targets
            ]
            self.critics = [critic.to(self.device) for critic in self.critics]
            self.critic_targets = [
                critic_target.to(self.device) for critic_target in self.critic_targets
            ]

        self.criterion = nn.MSELoss()

    def scale_to_action_space(self, action, idx):
        """Scales actions to action space defined by self.min_action and self.max_action.

        :param action: Action to be scaled
        :type action: numpy.ndarray
        """
        return np.where(
            action > 0,
            action * self.max_action[idx][0],
            action * -self.min_action[idx][0],
        )

    def getAction(self, states, epsilon=0, agent_mask=None, env_defined_actions=None):
        """Returns the next action to take in the environment.
        Epsilon is the probability of taking a random action, used for exploration.
        For epsilon-greedy behaviour, set epsilon to 0.

        :param state: Environment observations: {'agent_0': state_dim_0, ..., 'agent_n': state_dim_n}
        :type state: Dict[str, numpy.Array]
        :param epsilon: Probablilty of taking a random action for exploration, defaults to 0
        :type epsilon: float, optional
        :param agent_mask: Mask of agents to return actions for: {'agent_0': True, ..., 'agent_n': False}
        :type agent_mask: Dict[str, bool]
        :param env_defined_actions: Dictionary of actions defined by the environment: {'agent_0': np.array, ..., 'agent_n': np.array}
        :type env_defined_actions: Dict[str, np.array]
        """

        # Get agents, states and actions we want to take actions for at this timestep according to agent_mask
        if agent_mask is None:
            agent_ids = self.agent_ids
            actors = self.actors
            state_dims = self.state_dims
        else:
            agent_ids = [agent for agent in agent_mask.keys() if agent_mask[agent]]
            state_dims = [
                state_dim
                for state_dim, mask_flag in zip(self.state_dims, agent_mask.keys())
                if mask_flag
            ]
            action_dims_dict = {
                agent: action_dim
                for agent, action_dim in zip(self.agent_ids, self.action_dims)
            }
            states = {
                agent: states[agent] for agent in agent_mask.keys() if agent_mask[agent]
            }
            actors = [
                actor
                for agent, actor in zip(agent_mask.keys(), self.actors)
                if agent_mask[agent]
            ]

        # states = {key: np.vstack(value) for key, value in states.items()}

        # Convert states to a list of torch tensors
        states = [torch.from_numpy(state).float() for state in states.values()]

        # Configure accelerator
        if self.accelerator is None:
            states = [state.to(self.device) for state in states]

        if self.one_hot:
            states = [
                nn.functional.one_hot(state.long(), num_classes=state_dim[0])
                .float()
                .squeeze(1)
                for state, state_dim in zip(states, state_dims)
            ]

        if self.arch == "mlp":
            states = [
                state.unsqueeze(0) if len(state.size()) < 2 else state
                for state in states
            ]
        elif self.arch == "cnn":
            states = [state.unsqueeze(2) for state in states]

        action_dict = {}
        for idx, (agent_id, state, actor, action_dim) in enumerate(
            zip(agent_ids, states, actors, self.action_dims)
        ):
            if random.random() < epsilon:
                if self.discrete_actions:
                    action = (
                        np.random.dirichlet(np.ones(action_dim), size=state.size()[0])
                        .astype("float32")
                        .squeeze()
                    )
                else:
                    action = (
                        (self.max_action[idx][0] - self.min_action[idx][0])
                        * np.random.rand(state.size()[0], self.action_dims[idx])
                        .astype("float32")
                        .squeeze()
                    ) + self.min_action[idx][0]
            else:
                actor.eval()
                if self.accelerator is not None:
                    with actor.no_sync(), torch.no_grad():
                        action_values = actor(state)
                else:
                    with torch.no_grad():
                        action_values = actor(state)
                actor.train()
                if self.discrete_actions:
                    action = action_values.cpu().data.numpy().squeeze()
                else:
                    action = self.scale_to_action_space(
                        action_values.cpu().data.numpy().squeeze(), idx
                    )
                    action = (
                        action
                        + np.random.normal(
                            0, self.expl_noise, size=self.action_dims[idx]
                        ).astype(np.float32)
                    ).clip(self.min_action[idx][0], self.max_action[idx][0])
            action_dict[agent_id] = action

        if self.discrete_actions:
            discrete_action_dict = {}
            for agent, action in action_dict.items():
                if self.one_hot:
                    discrete_action_dict[agent] = action.argmax(axis=-1)
                else:
                    discrete_action_dict[agent] = action.argmax(axis=-1)
        else:
            discrete_action_dict = None

        if env_defined_actions is not None:
            for agent in env_defined_actions.keys():
                if not agent_mask[agent]:
                    if self.discrete_actions:
                        discrete_action_dict.update({agent: env_defined_actions[agent]})
                        action = env_defined_actions[agent]
                        action = (
                            nn.functional.one_hot(
                                torch.tensor(action).long(),
                                num_classes=action_dims_dict[agent],
                            )
                            .float()
                            .squeeze()
                        )
                        action_dict.update({agent: action})
                    else:
                        action_dict.update({agent: env_defined_actions[agent]})

        return (
            action_dict,
            discrete_action_dict,
        )

    def learn(self, experiences):
        """Updates agent network parameters to learn from experiences.

        :param experience: Tuple of dictionaries containing batched states, actions, rewards, next_states,
        dones in that order for each individual agent.
        :type experience: Tuple[Dict[str, torch.Tensor]]
        """
        loss_dict = {}
        for idx, (
            agent_id,
            actor,
            actor_target,
            critic,
            critic_target,
            actor_optimizer,
            critic_optimizer,
        ) in enumerate(
            zip(
                self.agent_ids,
                self.actors,
                self.actor_targets,
                self.critics,
                self.critic_targets,
                self.actor_optimizers,
                self.critic_optimizers,
            )
        ):
            states, actions, rewards, next_states, dones = experiences

            if self.one_hot:
                states = {
                    agent_id: nn.functional.one_hot(
                        state.long(), num_classes=state_dim[0]
                    )
                    .float()
                    .squeeze(1)
                    for (agent_id, state), state_dim in zip(
                        states.items(), self.state_dims
                    )
                }
                next_states = {
                    agent_id: nn.functional.one_hot(
                        next_state.long(), num_classes=state_dim[0]
                    )
                    .float()
                    .squeeze(1)
                    for (agent_id, next_state), state_dim in zip(
                        next_states.items(), self.state_dims
                    )
                }

            if self.arch == "mlp":
                action_values = list(actions.values())
                input_combined = torch.cat(list(states.values()) + action_values, 1)
                if self.accelerator is not None:
                    with critic.no_sync():
                        q_value = critic(input_combined)
                else:
                    q_value = critic(input_combined)
                next_actions = []
                for i, agent_id_label in enumerate(self.agent_ids):
                    unscaled_actions = self.actor_targets[i](
                        next_states[agent_id_label]
                    ).detach_()
                    if not self.discrete_actions:
                        scaled_actions = torch.where(
                            unscaled_actions > 0,
                            unscaled_actions * self.max_action[i][0],
                            unscaled_actions * -self.min_action[i][0],
                        )
                        next_actions.append(scaled_actions)
                    else:
                        next_actions.append(unscaled_actions)

            elif self.arch == "cnn":
                stacked_states = torch.stack(list(states.values()), dim=2)
                stacked_actions = torch.cat(list(actions.values()), dim=1)
                if self.accelerator is not None:
                    with critic.no_sync():
                        q_value = critic(stacked_states, stacked_actions)
                else:
                    q_value = critic(stacked_states, stacked_actions)
                next_actions = []
                for i, agent_id_label in enumerate(self.agent_ids):
                    unscaled_actions = self.actor_targets[i](
                        next_states[agent_id_label].unsqueeze(2)
                    ).detach_()
                    if not self.discrete_actions:
                        scaled_actions = torch.where(
                            unscaled_actions > 0,
                            unscaled_actions * self.max_action[i][0],
                            unscaled_actions * -self.min_action[i][0],
                        )
                        next_actions.append(scaled_actions)
                    else:
                        next_actions.append(unscaled_actions)

            if self.arch == "mlp":
                next_input_combined = torch.cat(
                    list(next_states.values()) + next_actions, 1
                )
                if self.accelerator is not None:
                    with critic_target.no_sync():
                        q_value_next_state = critic_target(next_input_combined)
                else:
                    q_value_next_state = critic_target(next_input_combined)
            elif self.arch == "cnn":
                stacked_next_states = torch.stack(list(next_states.values()), dim=2)
                stacked_next_actions = torch.cat(next_actions, dim=1)
                if self.accelerator is not None:
                    with critic_target.no_sync():
                        q_value_next_state = critic_target(
                            stacked_next_states, stacked_next_actions
                        )
                else:
                    q_value_next_state = critic_target(
                        stacked_next_states, stacked_next_actions
                    )

            y_j = (
                rewards[agent_id]
                + (1 - dones[agent_id]) * self.gamma * q_value_next_state
            )

            critic_loss = self.criterion(q_value, y_j.detach_())

            # critic loss backprop
            critic_optimizer.zero_grad()
            if self.accelerator is not None:
                self.accelerator.backward(critic_loss)
            else:
                critic_loss.backward()
            critic_optimizer.step()

            # update actor and targets
            if self.arch == "mlp":
                if self.accelerator is not None:
                    with actor.no_sync():
                        action = actor(states[agent_id])
                else:
                    action = actor(states[agent_id])
                if not self.discrete_actions:
                    action = torch.where(
                        action > 0,
                        action * self.max_action[idx][0],
                        action * -self.min_action[idx][0],
                    )
                detached_actions = copy.deepcopy(actions)
                detached_actions[agent_id] = action
                input_combined = torch.cat(
                    list(states.values()) + list(detached_actions.values()), 1
                )
                if self.accelerator is not None:
                    with critic.no_sync():
                        actor_loss = -critic(input_combined).mean()
                else:
                    actor_loss = -critic(input_combined).mean()

            elif self.arch == "cnn":
                if self.accelerator is not None:
                    with actor.no_sync():
                        action = actor(states[agent_id].unsqueeze(2))
                else:
                    action = actor(states[agent_id].unsqueeze(2))
                if not self.discrete_actions:
                    action = torch.where(
                        action > 0,
                        action * self.max_action[idx][0],
                        action * -self.min_action[idx][0],
                    )
                detached_actions = copy.deepcopy(actions)
                detached_actions[agent_id] = action
                stacked_detached_actions = torch.cat(
                    list(detached_actions.values()), dim=1
                )
                if self.accelerator is not None:
                    with critic.no_sync():
                        actor_loss = -critic(
                            stacked_states, stacked_detached_actions
                        ).mean()
                else:
                    actor_loss = -critic(
                        stacked_states, stacked_detached_actions
                    ).mean()

            # actor loss backprop
            actor_optimizer.zero_grad()
            if self.accelerator is not None:
                self.accelerator.backward(actor_loss)
            else:
                actor_loss.backward()
            actor_optimizer.step()

            loss_dict[f"{agent_id}"] = actor_loss.item(), critic_loss.item()

        for actor, actor_target, critic, critic_target in zip(
            self.actors, self.actor_targets, self.critics, self.critic_targets
        ):
            self.softUpdate(actor, actor_target)
            self.softUpdate(critic, critic_target)

        return loss_dict

    def softUpdate(self, net, target):
        """Soft updates target network."""
        for eval_param, target_param in zip(net.parameters(), target.parameters()):
            target_param.data.copy_(
                self.tau * eval_param.data + (1.0 - self.tau) * target_param.data
            )

    def test(self, env, swap_channels=False, max_steps=500, loop=3):
        """Returns mean test score of agent in environment with epsilon-greedy policy.

        :param env: The environment to be tested in
        :type env: Gym-style environment
        :param swap_channels: Swap image channels dimension from last to first [H, W, C] -> [C, H, W], defaults to False
        :type swap_channels: bool, optional
        :param max_steps: Maximum number of testing steps, defaults to 500
        :type max_steps: int, optional
        :param loop: Number of testing loops/episodes to complete. The returned score is the mean. Defaults to 3
        :type loop: int, optional
        """
        is_vectorised = (
            True if isinstance(env, PettingZooVectorizationParallelWrapper) else False
        )
        with torch.no_grad():
            rewards = []
            for i in range(loop):
                state, info = env.reset()
                agent_reward = {agent_id: 0 for agent_id in self.agent_ids}
                score = 0
                finished = False
                idx_step = 0
                while not finished:
                    idx_step += 1
                    if swap_channels:
                        if is_vectorised:
                            state = {
                                agent_id: np.moveaxis(s, [-1], [-3])
                                for agent_id, s in state.items()
                            }
                        else:
                            state = {
                                agent_id: np.moveaxis(np.expand_dims(s, 0), [-1], [-3])
                                for agent_id, s in state.items()
                            }
                    agent_mask = (
                        info["agent_mask"] if "agent_mask" in info.keys() else None
                    )
                    env_defined_actions = (
                        info["env_defined_actions"]
                        if "env_defined_actions" in info.keys()
                        else None
                    )
                    cont_actions, discrete_action = self.getAction(
                        state,
                        epsilon=0,
                        agent_mask=agent_mask,
                        env_defined_actions=env_defined_actions,
                    )
                    if self.discrete_actions:
                        action = discrete_action
                    else:
                        action = cont_actions
                    state, reward, done, trunc, info = env.step(action)
                    for agent_id, r in reward.items():
                        # agent_reward[agent_id] += r
                        agent_reward[agent_id] += (
                            r[0]
                            if isinstance(env, PettingZooVectorizationParallelWrapper)
                            else r
                        )
                    score = sum(agent_reward.values())
                    if not isinstance(env, PettingZooVectorizationParallelWrapper):
                        if any(done.values()) or all(trunc.values()):
                            finished = True
                    if idx_step == max_steps:
                        finished = True
                rewards.append(score)
        mean_fit = np.mean(rewards)
        self.fitness.append(mean_fit)
        return mean_fit

    def clone(self, index=None, wrap=True):
        """Returns cloned agent identical to self.

        :param index: Index to keep track of agent for tournament selection and mutation, defaults to None
        :type index: int, optional
        """
        input_args = self.inspect_attributes(input_args_only=True)
        input_args["wrap"] = wrap
        clone = type(self)(**input_args)

        if self.accelerator is not None:
            self.unwrap_models()
        actors = [actor.clone() for actor in self.actors]
        actor_targets = [actor_target.clone() for actor_target in self.actor_targets]
        critics = [critic.clone() for critic in self.critics]
        critic_targets = [
            critic_target.clone() for critic_target in self.critic_targets
        ]
        actor_optimizers = [
            optim.Adam(actor.parameters(), lr=clone.lr_actor) for actor in actors
        ]
        critic_optimizers = [
            optim.Adam(critic.parameters(), lr=clone.lr_critic) for critic in critics
        ]

        for (
            clone_actor_optimizer,
            actor_optimizer,
            clone_critic_optimizer,
            critic_optimizer,
        ) in zip(
            actor_optimizers,
            self.actor_optimizers,
            critic_optimizers,
            self.critic_optimizers,
        ):
            clone_actor_optimizer.load_state_dict(actor_optimizer.state_dict())
            clone_critic_optimizer.load_state_dict(critic_optimizer.state_dict())

        if self.accelerator is not None:
            if wrap:
                clone.actors = [self.accelerator.prepare(actor) for actor in actors]
                clone.actor_targets = [
                    self.accelerator.prepare(actor_target)
                    for actor_target in actor_targets
                ]
                clone.critics = [self.accelerator.prepare(critic) for critic in critics]
                clone.critic_targets = [
                    self.accelerator.prepare(critic_target)
                    for critic_target in critic_targets
                ]
                clone.actor_optimizers = [
                    self.accelerator.prepare(actor_optimizer)
                    for actor_optimizer in actor_optimizers
                ]
                clone.critic_optimizers = [
                    self.accelerator.prepare(critic_optimizer)
                    for critic_optimizer in critic_optimizers
                ]
            else:
                (
                    clone.actors,
                    clone.actor_targets,
                    clone.critics,
                    clone.critic_targets,
                    clone.actor_optimizers,
                    clone.critic_optimizers,
                ) = (
                    actors,
                    actor_targets,
                    critics,
                    critic_targets,
                    actor_optimizers,
                    critic_optimizers,
                )
        else:
            clone.actors = [actor.to(self.device) for actor in actors]
            clone.actor_targets = [
                actor_target.to(self.device) for actor_target in actor_targets
            ]
            clone.critics = [critic.to(self.device) for critic in critics]
            clone.critic_targets = [
                critic_target.to(self.device) for critic_target in critic_targets
            ]
            clone.actor_optimizers = actor_optimizers
            clone.critic_optimizers = critic_optimizers

        for attribute in self.inspect_attributes().keys():
            if hasattr(self, attribute) and hasattr(clone, attribute):
                attr, clone_attr = getattr(self, attribute), getattr(clone, attribute)
                if isinstance(attr, torch.Tensor) or isinstance(
                    clone_attr, torch.Tensor
                ):
                    if not torch.equal(attr, clone_attr):
                        setattr(
                            clone, attribute, copy.deepcopy(getattr(self, attribute))
                        )
                else:
                    if attr != clone_attr:
                        setattr(
                            clone, attribute, copy.deepcopy(getattr(self, attribute))
                        )
            else:
                setattr(clone, attribute, copy.deepcopy(getattr(self, attribute)))

        if index is not None:
            clone.index = index

        return clone

    def inspect_attributes(self, input_args_only=False):
        # Get all attributes of the current object
        attributes = inspect.getmembers(self, lambda a: not (inspect.isroutine(a)))
        guarded_attributes = [
            "actors",
            "critics",
            "actor_targets",
            "critic_targets",
            "actor_optimizers",
            "critic_optimizers",
        ]

        # Exclude private and built-in attributes
        attributes = [
            a for a in attributes if not (a[0].startswith("__") and a[0].endswith("__"))
        ]

        if input_args_only:
            constructor_params = inspect.signature(self.__init__).parameters.keys()
            attributes = {
                k: v
                for k, v in attributes
                if k not in guarded_attributes and k in constructor_params
            }
        else:
            # Remove the algo specific guarded variables
            attributes = {k: v for k, v in attributes if k not in guarded_attributes}

        return attributes

    def wrap_models(self):
        if self.accelerator is not None:
            self.actors = [self.accelerator.prepare(actor) for actor in self.actors]
            self.actor_targets = [
                self.accelerator.prepare(actor_target)
                for actor_target in self.actor_targets
            ]
            self.critics = [self.accelerator.prepare(critic) for critic in self.critics]
            self.critic_targets = [
                self.accelerator.prepare(critic_target)
                for critic_target in self.critic_targets
            ]
            self.actor_optimizers = [
                self.accelerator.prepare(actor_optimizer)
                for actor_optimizer in self.actor_optimizers
            ]
            self.critic_optimizers = [
                self.accelerator.prepare(critic_optimizer)
                for critic_optimizer in self.critic_optimizers
            ]

    def unwrap_models(self):
        if self.accelerator is not None:
            self.actors = [
                self.accelerator.unwrap_model(actor) for actor in self.actors
            ]
            self.actor_targets = [
                self.accelerator.unwrap_model(actor_target)
                for actor_target in self.actor_targets
            ]
            self.critics = [
                self.accelerator.unwrap_model(critic) for critic in self.critics
            ]
            self.critic_targets = [
                self.accelerator.unwrap_model(critic_target)
                for critic_target in self.critic_targets
            ]
            self.actor_optimizers = [
                unwrap_optimizer(actor_optimizer, actor, self.lr_actor)
                for actor_optimizer, actor, in zip(self.actor_optimizers, self.actors)
            ]
            self.critic_optimizers = [
                unwrap_optimizer(critic_optimizer, critic, self.lr_critic)
                for critic_optimizer, critic in zip(
                    self.critic_optimizers, self.critics
                )
            ]

    def saveCheckpoint(self, path):
        """Saves a checkpoint of agent properties and network weights to path.

        :param path: Location to save checkpoint at
        :type path: string
        """
        attribute_dict = self.inspect_attributes()

        network_info = {
            "actors_init_dict": [actor.init_dict for actor in self.actors],
            "actors_state_dict": [actor.state_dict() for actor in self.actors],
            "actor_targets_init_dict": [
                actor_target.init_dict for actor_target in self.actor_targets
            ],
            "actor_targets_state_dict": [
                actor_target.state_dict() for actor_target in self.actor_targets
            ],
            "critics_init_dict": [critic.init_dict for critic in self.critics],
            "critics_state_dict": [critic.state_dict() for critic in self.critics],
            "critic_targets_init_dict": [
                critic_target.init_dict for critic_target in self.critic_targets
            ],
            "critic_targets_state_dict": [
                critic_target.state_dict() for critic_target in self.critic_targets
            ],
            "actor_optimizers_state_dict": [
                actor_optimizer.state_dict()
                for actor_optimizer in self.actor_optimizers
            ],
            "critic_optimizers_state_dict": [
                critic_optimizer.state_dict()
                for critic_optimizer in self.critic_optimizers
            ],
        }

        attribute_dict.update(network_info)

        torch.save(
            attribute_dict,
            path,
            pickle_module=dill,
        )

    def loadCheckpoint(self, path):
        """Loads saved agent properties and network weights from checkpoint.

        :param path: Location to load checkpoint from
        :type path: string
        """
        network_info = {
            "actors_init_dict",
            "actors_state_dict",
            "actor_targets_init_dict",
            "actor_targets_state_dict",
            "critics_init_dict",
            "critics_state_dict",
            "critic_targets_init_dict",
            "critic_targets_state_dict",
            "actor_optimizers_state_dict",
            "critic_optimizers_state_dict",
            "net_config",
            "lr_actor",
            "lr_critic",
        }
        checkpoint = torch.load(path, map_location=self.device, pickle_module=dill)
        self.net_config = checkpoint["net_config"]
        if self.net_config is not None:
            self.arch = checkpoint["net_config"]["arch"]
            if self.arch == "mlp":
                network_class = EvolvableMLP
            elif self.arch == "cnn":
                network_class = EvolvableCNN
        else:
            network_class = MakeEvolvable

        self.actors = [
            network_class(**checkpoint["actors_init_dict"][idx])
            for idx, _ in enumerate(self.agent_ids)
        ]
        self.actor_targets = [
            network_class(**checkpoint["actor_targets_init_dict"][idx])
            for idx, _ in enumerate(self.agent_ids)
        ]
        self.critics = [
            network_class(**checkpoint["critics_init_dict"][idx])
            for idx, _ in enumerate(self.agent_ids)
        ]
        self.critic_targets = [
            network_class(**checkpoint["critic_targets_init_dict"][idx])
            for idx, _ in enumerate(self.agent_ids)
        ]

        self.lr_actor = checkpoint["lr_actor"]
        self.lr_critic = checkpoint["lr_critic"]
        self.actor_optimizers = [
            optim.Adam(actor.parameters(), lr=self.lr_actor) for actor in self.actors
        ]
        self.critic_optimizers = [
            optim.Adam(critic.parameters(), lr=self.lr_critic)
            for critic in self.critics
        ]
        actor_list = []
        critic_list = []
        actor_target_list = []
        critic_target_list = []
        actor_optimizer_list = []
        critic_optimizer_list = []

        for idx, (
            actor,
            actor_target,
            critic,
            critic_target,
            actor_optimizer,
            critic_optimizer,
        ) in enumerate(
            zip(
                self.actors,
                self.actor_targets,
                self.critics,
                self.critic_targets,
                self.actor_optimizers,
                self.critic_optimizers,
            )
        ):
            actor.load_state_dict(checkpoint["actors_state_dict"][idx])
            actor_list.append(actor)
            actor_target.load_state_dict(checkpoint["actor_targets_state_dict"][idx])
            actor_target_list.append(actor_target)
            critic.load_state_dict(checkpoint["critics_state_dict"][idx])
            critic_list.append(critic)
            critic_target.load_state_dict(checkpoint["critic_targets_state_dict"][idx])
            critic_target_list.append(critic_target)
            actor_optimizer.load_state_dict(
                checkpoint["actor_optimizers_state_dict"][idx]
            )
            actor_optimizer_list.append(actor_optimizer)
            critic_optimizer.load_state_dict(
                checkpoint["critic_optimizers_state_dict"][idx]
            )
            critic_optimizer_list.append(critic_optimizer)

        self.actors = actor_list
        self.actor_targets = actor_target_list
        self.critics = critic_list
        self.critic_targets = critic_target_list
        self.actor_optimizers = actor_optimizer_list
        self.critic_optimizers = critic_optimizer_list

        for attribute in checkpoint.keys():
            if attribute not in network_info:
                setattr(self, attribute, checkpoint[attribute])

    @classmethod
    def load(cls, path, device="cpu", accelerator=None):
        """Creates agent with properties and network weights loaded from path.

        :param path: Location to load checkpoint from
        :type path: string
        :param device: Device for accelerated computing, 'cpu' or 'cuda', defaults to 'cpu'
        :type device: str, optional
        :param accelerator: Accelerator for distributed computing, defaults to None
        :type accelerator: accelerate.Accelerator(), optional
        """
        checkpoint = torch.load(path, map_location=device, pickle_module=dill)
        for idx, _ in enumerate(checkpoint["agent_ids"]):
            checkpoint["actors_init_dict"][idx]["device"] = device
            checkpoint["actor_targets_init_dict"][idx]["device"] = device
            checkpoint["critics_init_dict"][idx]["device"] = device
            checkpoint["critic_targets_init_dict"][idx]["device"] = device

        actors_init_dict = checkpoint.pop("actors_init_dict")
        actor_targets_init_dict = checkpoint.pop("actor_targets_init_dict")
        actors_state_dict = checkpoint.pop("actors_state_dict")
        actor_targets_state_dict = checkpoint.pop("actor_targets_state_dict")
        actor_optimizers_state_dict = checkpoint.pop("actor_optimizers_state_dict")
        critics_init_dict = checkpoint.pop("critics_init_dict")
        critic_targets_init_dict = checkpoint.pop("critic_targets_init_dict")
        critics_state_dict = checkpoint.pop("critics_state_dict")
        critic_targets_state_dict = checkpoint.pop("critic_targets_state_dict")
        critic_optimizers_state_dict = checkpoint.pop("critic_optimizers_state_dict")

        checkpoint["device"] = device
        checkpoint["accelerator"] = accelerator

        constructor_params = inspect.signature(cls.__init__).parameters.keys()
        class_init_dict = {
            k: v for k, v in checkpoint.items() if k in constructor_params
        }

        if checkpoint["net_config"] is not None:
            agent = cls(**class_init_dict)
            agent.arch = checkpoint["net_config"]["arch"]
            if agent.arch == "mlp":
                agent.actors = [
                    EvolvableMLP(**actors_init_dict[idx])
                    for idx, _ in enumerate(agent.agent_ids)
                ]
                agent.actor_targets = [
                    EvolvableMLP(**actor_targets_init_dict[idx])
                    for idx, _ in enumerate(agent.agent_ids)
                ]
                agent.critics = [
                    EvolvableMLP(**critics_init_dict[idx])
                    for idx, _ in enumerate(agent.agent_ids)
                ]
                agent.critic_targets = [
                    EvolvableMLP(**critic_targets_init_dict[idx])
                    for idx, _ in enumerate(agent.agent_ids)
                ]
            elif agent.arch == "cnn":
                agent.actors = [
                    EvolvableCNN(**actors_init_dict[idx])
                    for idx, _ in enumerate(agent.agent_ids)
                ]
                agent.actor_targets = [
                    EvolvableCNN(**actor_targets_init_dict[idx])
                    for idx, _ in enumerate(agent.agent_ids)
                ]
                agent.critics = [
                    EvolvableCNN(**critics_init_dict[idx])
                    for idx, _ in enumerate(agent.agent_ids)
                ]
                agent.critic_targets = [
                    EvolvableCNN(**critic_targets_init_dict[idx])
                    for idx, _ in enumerate(agent.agent_ids)
                ]
        else:
            class_init_dict["actor_networks"] = [
                MakeEvolvable(**actors_init_dict[idx])
                for idx, _ in enumerate(checkpoint["agent_ids"])
            ]
            class_init_dict["critic_networks"] = [
                MakeEvolvable(**critics_init_dict[idx])
                for idx, _ in enumerate(checkpoint["agent_ids"])
            ]
            agent = cls(**class_init_dict)
            agent.actor_targets = [
                MakeEvolvable(**actor_targets_init_dict[idx])
                for idx, _ in enumerate(checkpoint["agent_ids"])
            ]
            agent.critic_targets = [
                MakeEvolvable(**critic_targets_init_dict[idx])
                for idx, _ in enumerate(checkpoint["agent_ids"])
            ]

        agent.actor_optimizers = [
            optim.Adam(actor.parameters(), lr=agent.lr_actor) for actor in agent.actors
        ]
        agent.critic_optimizers = [
            optim.Adam(critic.parameters(), lr=agent.lr_critic)
            for critic in agent.critics
        ]

        actor_list = []
        critic_list = []
        actor_target_list = []
        critic_target_list = []
        actor_optimizer_list = []
        critic_optimizer_list = []
        for idx, (
            actor,
            actor_target,
            critic,
            critic_target,
            actor_optimizer,
            critic_optimizer,
        ) in enumerate(
            zip(
                agent.actors,
                agent.actor_targets,
                agent.critics,
                agent.critic_targets,
                agent.actor_optimizers,
                agent.critic_optimizers,
            )
        ):
            actor.load_state_dict(actors_state_dict[idx])
            actor_list.append(actor)
            actor_target.load_state_dict(actor_targets_state_dict[idx])
            actor_target_list.append(actor_target)
            critic.load_state_dict(critics_state_dict[idx])
            critic_list.append(critic)
            critic_target.load_state_dict(critic_targets_state_dict[idx])
            critic_target_list.append(critic_target)
            actor_optimizer.load_state_dict(actor_optimizers_state_dict[idx])
            actor_optimizer_list.append(actor_optimizer)
            critic_optimizer.load_state_dict(critic_optimizers_state_dict[idx])
            critic_optimizer_list.append(critic_optimizer)

        agent.actors = actor_list
        agent.actor_targets = actor_target_list
        agent.critics = critic_list
        agent.critic_targets = critic_target_list
        agent.actor_optimizers = actor_optimizer_list
        agent.critic_optimizers = critic_optimizer_list

        if accelerator is not None:
            agent.wrap_models()

        for attribute in agent.inspect_attributes().keys():
            setattr(agent, attribute, checkpoint[attribute])

        return agent
