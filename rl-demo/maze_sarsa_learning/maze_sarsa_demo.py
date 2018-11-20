#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from maze_env import Maze
from sarsa_base import SarsaTable


def sarsa():
    def update():
        for episode in range(300):
            env.set_title(f'sarsa-ep{episode}')
            print("episode", episode)
            observation = env.reset()
            while True:
                env.render()
                action = agent.select_action(str(observation))
                observation_, reward, terminate = env.step(action)
                action_ = agent.select_action(str(observation_))
                agent.train(str(observation), action, reward, str(observation_), action_)
                observation = observation_
                if terminate:
                    print(agent.q_table)
                    break
        print("DONE")
        env.destroy()

    env = Maze()

    agent = SarsaTable(actions=list(range(env.n_actions)))
    env.after(100, update)
    env.mainloop()


if __name__ == '__main__':
    sarsa()
