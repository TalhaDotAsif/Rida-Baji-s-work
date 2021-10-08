#!/usr/bin/env python
# coding: utf-8

# In[31]:



import random
from typing import List

class SampleEnvironment:
    def __init__(self):
        self.steps_left = 20

    def get_observation(self) -> List[float]:
        return [0.0, 0.0, 0.0]

    def get_actions(self) -> List[int]:
        return [0, 1]

    def is_done(self) -> bool:
        return self.steps_left == 0

    def action(self, action: int) -> float:
        if self.is_done():
            raise Exception("Game is over")
        self.steps_left -= 1
        return random.random()


# In[32]:


class Agent:
    def __init__(self):
        self.total_reward = 0.0

    def step(self, env: SampleEnvironment):
        current_obs = env.get_observation()
        print("Observation {}".format(current_obs))
        actions = env.get_actions()
        print(actions)
        reward = env.action(random.choice(actions))
        self.total_reward += reward
        print("Total Reward {}".format(self.total_reward))


# In[33]:



if __name__ == "__main__":
    env = SampleEnvironment()
    agent = Agent()
    i=0

    while not env.is_done():
        i=i+1
        print("Steps {}".format(i))
        agent.step(env)

    print("Total reward got: %.4f" % agent.total_reward)


# In[ ]:




