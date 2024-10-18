import matplotlib.pyplot as plt

# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('ggplot')
fig, ax = plt.subplots()
# ax.scatter(x_values,y_values, s=5, color=(0,0.8,0))

#使用颜色映射
ax.scatter(x_values,y_values, s=5, c=y_values, cmap=plt.cm.Reds)
#设置图题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#设置刻度标记的样式
ax.tick_params(labelsize=7)

#设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])

#强制使用常规表示法
ax.ticklabel_format(style='plain')

# plt.show()
plt.savefig('squares.png', bbox_inches='tight')
