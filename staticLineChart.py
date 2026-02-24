import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]


plt.plot(x, y, marker='o', linestyle='-', color='blue')

plt.title("Simple Line Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")


plt.grid(True)

plt.show()
