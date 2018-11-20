#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Maze env for rl demo...

red block: agent
black block: r = -1
yellow block: r = +1
other blocks(white): r = 0
"""

import sys
import time
import numpy as np
import tkinter as tk

UNIT = 40  # pixel size
MAZE_H = 4  # maze height
MAZE_W = 4  # maze weidth


class Maze(tk.Tk):
    def __init__(self):
        super(Maze, self).__init__()
        self.action_space = ['n', 's', 'w', 'e']
        self.n_actions = len(self.action_space)

        self.title('maze')
        self.geometry(f'{MAZE_H * UNIT}x{MAZE_W * UNIT}')
        self._build_maze()

    def _build_maze(self):
        self.canvas = tk.Canvas(self,
                                height=MAZE_H * UNIT, width=MAZE_W * UNIT,
                                bg='white')
        for c in range(MAZE_W):
            x0, y0, x1, y1 = c * UNIT, 0, c * UNIT, MAZE_W * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(MAZE_H):
            x0, y0, x1, y1 = 0, r * UNIT, MAZE_H * UNIT, r * UNIT
            self.canvas.create_line(x0, y0, x1, y1)

        origin = np.array([20, 20])
        self.agent = self.canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 15, origin[1] + 15,
            fill='red'
        )

        hell_center1 = origin + np.array([UNIT * 2, UNIT])
        hell_center2 = origin + np.array([UNIT, UNIT * 2])

        self.hell1 = self.canvas.create_rectangle(
            hell_center1[0] - 15, hell_center1[1] - 15,
            hell_center1[0] + 15, hell_center1[1] + 15,
            fill='black'
        )
        self.hell2 = self.canvas.create_rectangle(
            hell_center2[0] - 15, hell_center2[1] - 15,
            hell_center2[0] + 15, hell_center2[1] + 15,
            fill='black'
        )

        target = origin + UNIT * 2
        self.target = self.canvas.create_oval(
            target[0] - 15, target[1] - 15,
            target[0] + 15, target[1] + 15,
            fill='yellow'
        )

        self.canvas.pack()

    def reset(self):
        self.update()
        time.sleep(0.5)
        self.canvas.delete(self.agent)
        origin = np.array([20, 20])
        self.agent = self.canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 15, origin[1] + 15,
            fill='red'
        )
        return self.canvas.coords(self.agent)

    def step(self, action):
        s = self.canvas.coords(self.agent)
        tmp_r = 0
        base_action = np.array([0, 0])
        if action == 0:  # n
            if s[1] > UNIT:
                base_action[1] -= UNIT
            else:
                tmp_r = -1
        elif action == 1:  # s
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
            else:
                tmp_r = -1
        elif action == 2:  # w
            if s[0] > UNIT:
                base_action[0] -= UNIT
            else:
                tmp_r = -1
        elif action == 3:  # e
            if s[0] <= (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
            else:
                tmp_r = -1

        self.canvas.move(self.agent, base_action[0], base_action[1])
        s_ = self.canvas.coords(self.agent)

        if s_ == self.canvas.coords(self.target):
            reward = 1
            terminate = True
            s_ = 'terminal'
        elif s_ == self.canvas.coords(self.hell1) or s_ == self.canvas.coords(self.hell2):
            reward = -1
            terminate = True
            s_ = 'terminal'
        else:
            reward = tmp_r
            terminate = False

        return s_, reward, terminate

    def render(self):
        time.sleep(0.1)
        self.update()


def update():
    for t in range(10):
        s = env.reset()
        while True:
            env.render()
            a = 3
            s, r, terminate = env.step(a)
            if terminate:
                break


if __name__ == '__main__':
    env = Maze()
    env.after(100, update)
    env.mainloop()
