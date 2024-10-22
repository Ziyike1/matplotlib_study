from random import choice


class RandomWalk:
    """一个生成随机游走数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机游走的属性"""
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机游走包含的所有点"""

        # 不断游走，直到列表达指定的长度
        while len(self.x_values) < self.num_points:

            x_step = self._get_step()
            y_step = self._get_step()

            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的坐标值
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def _get_step(self):
        # 决定前进的方向和距离
        x_y_direction = choice([1, -1])
        x_y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        x_y_step = x_y_direction * x_y_distance
        return x_y_step
