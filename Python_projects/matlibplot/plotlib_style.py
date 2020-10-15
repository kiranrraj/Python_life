from matplotlib import pyplot as plt
plt.style.use('dark_background')
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200,56000, 62316, 64928, 67317, 68748, 73752]
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(dev_x, dev_y, label="All Developers")
plt.plot(dev_x, py_dev_y,label="Python")
plt.plot(dev_x, js_dev_y,label="Javascript")

plt.xlabel('Ages')
plt.ylabel('Salary in USD')
plt.title('Ages vs US Dollar')
plt.legend()
plt.grid(True)
# print(plt.style.available)

plt.show()