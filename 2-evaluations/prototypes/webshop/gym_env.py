import gym
from web_agent_site.envs import WebAgentTextEnv

env = gym.make("WebAgentTextEnv-v0", observation_mode="text", num_products=1000, num_users=1000)