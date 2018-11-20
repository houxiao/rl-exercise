#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import numpy as np
import pandas as pd


class QLearningTable(object):
    def __init__(self, actions, alpha=0.01, gamma=0.9, epsilon=0.1):
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)

    def select_action(self, observation):
        self.check_state_exist(observation)
        if np.random.uniform() < self.epsilon:  # random action
            action = np.random.choice(self.actions)
        else:
            state_action = self.q_table.loc[observation, :]
            action = np.random.choice(state_action[state_action == np.max(state_action)].index)
        return action

    def train(self, s, a, s_, r):
        self.check_state_exist(s_)
        q_predict = self.q_table.loc[s, a]
        if s_ != 'termianl':
            q_target = r
        else:
            q_target = r + self.gamma * self.q_table.loc[s_, :].max()
        self.q_table.loc[s, a] += self.alpha * (q_target - q_predict)

    def check_state_exist(self, s):
        if s not in list(self.q_table.index):
            self.q_table = self.q_table.append(
                pd.Series(
                    [0]*len(self.actions),
                    index=self.q_table.columns,
                    name=s,
                )
            )