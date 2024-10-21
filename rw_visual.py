import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    """只要程序处于活动状态，就不断的模拟随机游走"""
    # 创建一个RandomWalk实例
    rw = RandomWalk()
    rw.fill_walk()

    # 将所有的点都绘制出来
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, s=15, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none')
    ax.set_aspect('equal')

    #突出起点和终点
    ax.scatter(0, 0, s=100, c='green', edgecolors='none')
    ax.scatter(rw.x_values[-1], rw.y_values[-1], s=100, c='red', edgecolors='none')

    #隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
