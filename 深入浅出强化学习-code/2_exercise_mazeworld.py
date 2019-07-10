#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Xiao Hou
# Time: 19-7-10 下午10:07

"""
    注意，rendering里的坐标原点在左下！！！
"""

import gym
import random
from gym.utils import seeding


class MazeWorld(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 2
    }

    def __init__(self):
        self.states = list(range(1, 26))

        self.x = list(range(140, 461, 80))*5
        self.y = [460]*5+[380]*5+[300]*5+[220]*5+[140]*5

        self.actions = ['n', 's', 'w', 'e']
        self.terminate_states = [15]

        self._set_rewards()
        self._set_transition()

        self.gamma = 0.8
        self.viewer = None
        self.state = None

    def _set_rewards(self):
        self.rewards = dict()
        self.rewards['10_s'] = 1.0
        self.rewards['14_e'] = 1.0
        self.rewards['20_n'] = 1.0

        self.rewards['3_e'] = -1.0
        self.rewards['8_e'] = -1.0
        self.rewards['14_n'] = -1.0
        self.rewards['5_w'] = -1.0
        self.rewards['10_w'] = -1.0

        self.rewards['6_s'] = -1.0
        self.rewards['7_s'] = -1.0
        self.rewards['13_w'] = -1.0
        self.rewards['16_n'] = -1.0
        self.rewards['17_n'] = -1.0

        self.rewards['22_e'] = -1.0
        self.rewards['18_s'] = -1.0
        self.rewards['19_s'] = -1.0
        self.rewards['20_s'] = -1.0

    def _set_transition(self):
        self.transition = dict()
        for i in range(1, 6):
            for j in range(1, 6):
                idx = (i - 1) * 5 + j
                if idx - 5 in self.states and (i-2)<=(idx-5)//5:
                    self.transition[f'{idx}_n'] = idx-5
                if idx + 5 in self.states and (idx-5)//5<=(i):
                    self.transition[f'{idx}_s'] = idx + 5
                if idx - 1 in self.states and (idx-1)%5!=0:
                    self.transition[f'{idx}_w'] = idx - 1
                if idx + 1 in self.states and (idx+1)%5!=1:
                    self.transition[f'{idx}_e'] = idx + 1

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def reset(self):
        self.state = random.choice(self.states)
        return self.state

    def step(self, action):
        state = self.state
        if state in self.terminate_states:
            return state, 0, True, {}
        key= f'{state}_{action}'

        # 状态转移
        if key in self.transition:
            next_state = self.transition[key]
        else:
            next_state = state
        self.state = next_state

        # 检查是否结束
        is_termianl = True if next_state in self.terminate_states else False
        # 查表得到回报值
        r = 0.0 if key not in self.rewards else self.rewards[key]

        # 返回： 下一状态，回报，是否结束，调试信息
        return next_state, r, is_termianl, {}

    def render(self, mode='human', close=False):
        if close:
            if self.viewer:
                self.viewer.close()
                self.viewer = None
            return

        screen_width = 600
        screen_height = 600

        if self.viewer is None:
            from gym.envs.classic_control import rendering
            self.viewer = rendering.Viewer(screen_width, screen_height)

            # 创建网格界面

            for i in range(100, 501, 80):
                line = rendering.Line((100, i), (500, i))
                line.set_color(0,0,0)
                self.viewer.add_geom(line)

                line = rendering.Line((i,100), (i,500))
                line.set_color(0, 0, 0)
                self.viewer.add_geom(line)
            for i in [4,9,11,12,23,24,25]:
                cp = [self.x[i-1], self.y[i-1]]
                wall = rendering.make_polygon([(cp[0]-40,cp[1]-40),(cp[0]-40,cp[1]+40),(cp[0]+40,cp[1]+40),(cp[0]+40,cp[1]-40)], filled=True)
                wall.set_color(0,0,0)
                self.viewer.add_geom(wall)

            exit = rendering.make_circle(40)
            exit_id=15
            exit.add_attr(rendering.Transform(translation=([self.x[exit_id-1], self.y[exit_id-1]])))
            exit.set_color(1, 0.9, 0)
            self.viewer.add_geom(exit)

            robot = rendering.make_circle(30)
            self.robotrans = rendering.Transform()
            robot.add_attr(self.robotrans)
            robot.set_color(0.8, 0.6, 0.4)
            self.viewer.add_geom(robot)

        if self.state is None:
            return None
        self.robotrans.set_translation(self.x[self.state - 1], self.y[self.state - 1])

        return self.viewer.render(return_rgb_array=mode=='rgb_array')

    def close(self):
        if self.viewer:
            self.viewer.close()
            self.viewer = None


if __name__ == '__main__':
    # env = gym.make('MazeWorld-v0')
    env = MazeWorld()
    env.reset()
    while 1:
        env.render()
