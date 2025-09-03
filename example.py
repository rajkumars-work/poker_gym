import gymnasium as gym

import poker_gym

env = gym.make("KuhnTwoPlayer-v0", disable_env_checker=True)

env.unwrapped.register_agents([poker_gym.agent.kuhn.NashKuhnAgent(0.3)] * 2)

obs, info = env.reset()

while True:
    bet = env.unwrapped.act(obs)
    obs, rewards, done, truncated, info = env.step(bet)

    if all(done):
        break

env.close()

print(rewards)
