# -*- coding: utf-8 -*-

# 非原创，转自莫烦大神的教程，有微小修改
# https://morvanzhou.github.io/tutorials/machine-learning/reinforcement-learning/

import time
import numpy as np
import pandas as pd


N_STATES = 10  # 状态数量， 1维世界长度
ACTIONS = ['left', 'right']  # 可做动作
EPSILON = 0.1
ALPHA = 0.1  # 学习率
GAMMA = 0.9  # discounting
MAX_EPISODES = 20
FRESH_TIME = 0.3  # 移动间隔时间


def init_q_table(n_states, actions):
    # table = [[[0]*len(actions)] for _ in range(len(n_states))]
    table = pd.DataFrame(
        np.zeros((n_states, len(actions))),  # 初始化全部为0
        columns=actions  # 列对应动作
    )
    return table


def select_action(state, q_table):
    state_actions = q_table.iloc[state, :]  # 当前状态可做动作
    # epsilon 随机探索
    if np.random.uniform() < EPSILON or state_actions.all() == 0:
        action_name = np.random.choice(ACTIONS)
    else:
        action_name = state_actions.idxmax()
    return action_name


def get_env_response(S, A):
    """ env  respond to input state & action

    Args:
        S: current state
        A: action

    Returns: next state S_, reward R

    """
    if A == 'right':
        if S == N_STATES - 2:
            S_ = 'terminal'
            R = 1
        else:
            S_ = S + 1
            R = 0
    else:
        R = 0
        if S == 0:
            S_ = S
        else:
            S_ = S - 1
    return S_, R


def update_env(S, episode, step_counter):
    env_list = ['-']*(N_STATES-1)+['T']
    if S == 'terminal':

        print(f'\rEpisode {episode + 1}: total_steps = {step_counter}', end='')
        time.sleep(2)
    else:
        env_list[S] = 'o'
        print('\r{}'.format(''.join(env_list)), end='')
        time.sleep(FRESH_TIME)


def rl_train():
    q_table = init_q_table(N_STATES, ACTIONS)
    for episode in range(MAX_EPISODES):
        step_counter = 0
        S = 0
        is_terminal = False
        update_env(S, episode, step_counter)
        while not  is_terminal:
            A = select_action(S, q_table)
            S_, R = get_env_response(S, A)
            q_predict = q_table.loc[S, A]
            if S_ != 'terminal':
                q_target = R + GAMMA * q_table.iloc[S_, :].max()
            else:
                q_target = R
                is_terminal = True
            q_table.loc[S, A] += ALPHA * (q_target - q_predict)
            S = S_
            step_counter += 1
            update_env(S, episode, step_counter)
    return q_table


if __name__ == '__main__':
    q_table = rl_train()
    print(q_table)