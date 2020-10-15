from matplotlib import pyplot as plt

dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200,56000, 62316, 64928, 67317, 68748, 73752]

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

#creating plot 
plt.plot(dev_x, dev_y, label='All Dev', linewidth=3, color="#444444")
plt.plot(dev_x, py_dev_y, label = 'Python', color="#ff5623", linestyle="--" )

#labels
plt.xlabel('Ages')
plt.ylabel('Median Salary')
plt.title('Salary Vs Age')
plt.grid(True)

# plt.legend(['All Dev', 'Python'])
plt.legend()

plt.show()