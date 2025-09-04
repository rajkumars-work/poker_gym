<div align="center">

<img src="./poker_gym/resources/images/black_red_logo.svg" alt="Logo" width=200px>

</div>

# poker_gym


poker_gym is a [gymnasium](https://gymnasium.farama.org/) wrapper around the [clubs](https://github.com/fschlatt/clubs) python poker library. [clubs](https://github.com/fschlatt/clubs) is used for running arbitrary configurations of community card poker games. This includes anything from simple Leduc or [Kuhn](https://en.wikipedia.org/wiki/Kuhn_poker) poker to full n-player [No Limit Texas Hold'em](https://en.wikipedia.org/wiki/Texas_hold_%27em) or [Pot Limit Omaha](https://en.wikipedia.org/wiki/Omaha_hold_%27em#Pot-limit_Omaha).
## Install

Install using `pip install poker-gym`.

# How to use

By running `import poker_gym`, several pre-defined clubs poker configurations are registered with gymnasium (call `poker_gym.ENVS` for a full list). Custom environments can be registered with `poker_gym.envs.register({"{environment_name}": {config_dictionary})}`. Environment names must follow the gymnasium environment name convention ({title-case}-v{version_number}). Check the [clubs documentation](https://clubs.readthedocs.io/en/latest/index.html) for additional information about the structure of a configuration dictionary.

Since [gymnasium](https://gymnasium.farama.org/) isn't designed for multi-agent games, the api is extended to enable registering agents. This is not required, but ensures each agent only receives the information it's supposed to. An agent needs to inherit from the `poker_gym.agent.base.BaseAgent` class and implement the `act` method. `act` receives a game state dictionary and needs to output an integer bet size. A list of agents the length of the number of players can then be registered with the environment using `env.unwrapped.register_agents`. By calling `env.unwrapped.act({observation_dictionary})`, the observation dictionary is passed to the correct agent and the agent's bet is returned. This can then be passed on the `env.step` function. An example with an optimal Kuhn agent (`poker_gym.agent.kuhn.NashKuhnAgent`) is given below.

## Example

```python
import gymnasium as gym

import poker_gym

env = gym.make("KuhnTwoPlayer-v0", disable_env_checker=True)
env.unwrapped.register_agents([poker_gym.agent.kuhn.NashKuhnAgent(0.3)] * 2)
obs, info = env.reset()

while True:
    bet = env.unwrapped.act(obs)
    obs, rewards, terminated, truncated, info = env.step(bet)

    if all(terminated) or all(truncated):
        break

print(rewards)
```
