#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Xiao Hou
# Time: 19-7-11 下午11:33


from math import ceil

def print_matrix(matrix):
    for i in matrix:
        print(*i)
    print()


def update(matrix, prob):
    # 如果不能移动（边界），则原地罚站
    new_matrix = [[0.0]*4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            if i==j==0 or i==j==3:
                pass
            else:
                n_val = 0
                if i>0:
                    n_val += prob*(-1.0+matrix[i-1][j])
                else:
                    n_val += prob*(matrix[i][j]+-1.0)
                if i<3:
                    n_val += prob*(-1.0+matrix[i+1][j])
                else:
                    n_val += prob*(matrix[i][j]+-1.0)
                if j > 0:
                    n_val += prob*(-1.0+matrix[i][j-1])
                else:
                    n_val += prob * (matrix[i][j] + -1.0)
                if j<3:
                    n_val += prob*(-1.0+matrix[i][j+1])
                else:
                    n_val += prob*(matrix[i][j]+-1.0)

                # 这里没太明白书上保留量为有效数字是怎么保留的。但实际计算应该就是round吧
                # UPDATE 看了这书作者在知乎上的文章，里面给了代码，居然是用6.2f...
                # new_matrix[i][j] = float(str(n_val)[:4])
                # new_matrix[i][j] = ceil(n_val*10)/10
                new_matrix[i][j] = float('{0:>6.2f}'.format(n_val))
                # new_matrix[i][j] = float('%6.2f' % n_val)
                # new_matrix[i][j] = n_val

    return new_matrix

def main():
    # init
    matrix = [[0.0]*4 for i in range(4)]
    prob = 0.25

    for k in range(0,1000):
        print(f'k={k}')
        print_matrix(matrix)
        n_matrix = update(matrix, prob)

        if n_matrix!= matrix:
            matrix = n_matrix
        else:
            break


if __name__ == '__main__':
    main()

"""
output example (k from 0 to 10):

k=0
0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0

k=1
0.0 -1.0 -1.0 -1.0
-1.0 -1.0 -1.0 -1.0
-1.0 -1.0 -1.0 -1.0
-1.0 -1.0 -1.0 0.0

k=2
0.0 -1.8 -2.0 -2.0
-1.8 -2.0 -2.0 -2.0
-2.0 -2.0 -2.0 -1.8
-2.0 -2.0 -1.8 0.0

k=3
0.0 -2.5 -3.0 -3.0
-2.5 -2.9 -3.0 -3.0
-3.0 -3.0 -2.9 -2.5
-3.0 -3.0 -2.5 0.0

k=4
0.0 -3.1 -3.9 -4.0
-3.1 -3.8 -4.0 -3.9
-3.9 -4.0 -3.8 -3.1
-4.0 -3.9 -3.1 0.0

k=5
0.0 -3.7 -4.8 -5.0
-3.7 -4.5 -4.8 -4.8
-4.8 -4.8 -4.5 -3.7
-5.0 -4.8 -3.7 0.0

k=6
0.0 -4.2 -5.6 -5.9
-4.2 -5.2 -5.7 -5.6
-5.6 -5.7 -5.2 -4.2
-5.9 -5.6 -4.2 0.0

k=7
0.0 -4.8 -6.3 -6.8
-4.8 -6.0 -6.4 -6.3
-6.4 -6.4 -6.0 -4.8
-6.8 -6.4 -4.8 0.0

k=8
0.0 -5.3 -7.1 -7.5
-5.3 -6.6 -7.2 -7.1
-7.1 -7.2 -6.6 -5.3
-7.6 -7.1 -5.3 0.0

k=9
0.0 -5.8 -7.8 -8.3
-5.8 -7.2 -7.8 -7.8
-7.8 -7.8 -7.2 -5.8
-8.3 -7.8 -5.8 0.0

k=10
0.0 -6.2 -8.4 -9.1
-6.2 -7.8 -8.5 -8.4
-8.4 -8.5 -7.8 -6.2
-9.1 -8.4 -6.2 0.0
"""