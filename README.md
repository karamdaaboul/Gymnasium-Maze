[![Python](https://img.shields.io/pypi/pyversions/gymnasium-maze.svg)](https://badge.fury.io/py/gymnasium-maze)
[![PyPI](https://badge.fury.io/py/gymnasium-maze.svg)](https://badge.fury.io/py/gymnasium-maze)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<p align="center">
  <a href = "https://robotics.farama.org/" target = "_blank"> <img src="https://raw.githubusercontent.com/Farama-Foundation/Gymnasium-Robotics/main/docs/gymnasium-maze.png" width="500px"/> </a>
</p>

This library contains a collection of Reinforcement Learning maze environments that use the [Gymnasium](https://gymnasium.farama.org/) API. The environments run with the [MuJoCo](https://mujoco.org/) physics engine and the maintained [mujoco python bindings](https://mujoco.readthedocs.io/en/latest/python.html).

## Installation

These environments require the MuJoCo engine from Deepmind to be installed. Instructions to install the physics engine can be found at the [MuJoCo website](https://mujoco.org/) and the [MuJoCo Github repository](https://github.com/deepmind/mujoco).

We support and test for Linux and macOS. We will accept PRs related to Windows, but do not officially support it.

## Environments

`Gymnasium-Maze` includes maze environments where an agent has to navigate through a maze to reach certain goal position. Two different agents can be used: a 2-DoF force-controlled ball, or the classic `Ant` agent from the [Gymnasium MuJoCo environments](https://gymnasium.farama.org/environments/mujoco/ant/). The environment can be initialized with a variety of maze shapes with increasing levels of difficulty.

### Available Maze Types

* **UMaze** - Simple U-shaped maze
* **Open** - Open area with walls around the perimeter
* **Medium** - Medium complexity maze
* **Large** - Large, complex maze
* **Dangerous** - maze with dangerous states

### Agent Types

* **Point** - A 2-DoF force-controlled ball that can move in x and y directions
* **Ant** - The classic Ant agent with 8 degrees of freedom

### Environment Variations

Each maze type comes in different variations:
* **Standard** - Single goal and reset location
* **Diverse_G** - Multiple possible goal locations
* **Diverse_GR** - Multiple possible goal and reset locations

## Multi-goal API

The maze environments use an extension of the core Gymnasium API by inheriting from [GoalEnv](https://robotics.farama.org/content/multi-goal_api/) class. The new API forces the environments to have a dictionary observation space that contains 3 keys:

* `observation` - The actual observation of the environment
* `desired_goal` - The goal that the agent has to achieved
* `achieved_goal` - The goal that the agent has currently achieved instead. The objective of the environments is for this value to be close to `desired_goal`

This API also exposes the function of the reward, as well as the terminated and truncated signals to re-compute their values with different goals. This functionality is useful for algorithms that use Hindsight Experience Replay (HER).

The following example demonstrates how the exposed reward, terminated, and truncated functions
can be used to re-compute the values with substituted goals. The info dictionary can be used to store
additional information that may be necessary to re-compute the reward, but that is independent of the
goal, e.g. state derived from the simulation.

```python
import gymnasium as gym

env = gym.make("PointMaze_UMaze-v3")
env.reset()
obs, reward, terminated, truncated, info = env.step(env.action_space.sample())

# The following always has to hold:
assert reward == env.compute_reward(obs["achieved_goal"], obs["desired_goal"], info)
assert truncated == env.compute_truncated(obs["achieved_goal"], obs["desired_goal"], info)
assert terminated == env.compute_terminated(obs["achieved_goal"], obs["desired_goal"], info)

# However goals can also be substituted:
substitute_goal = obs["achieved_goal"].copy()
substitute_reward = env.compute_reward(obs["achieved_goal"], substitute_goal, info)
substitute_terminated = env.compute_terminated(obs["achieved_goal"], substitute_goal, info)
substitute_truncated = env.compute_truncated(obs["achieved_goal"], substitute_goal, info)
```

The `GoalEnv` class can also be used for custom environments.

## Project Maintainers
Main Contributors: [Rodrigo Perez-Vicente](https://github.com/rodrigodelazcano), [Kallinteris Andreas](https://github.com/Kallinteris-Andreas), [Jet Tai](https://github.com/jjshoots)

Modified by: [Karam Daaboul](https://github.com/karamdaaboul)
