import matplotlib.pyplot as plt

# Given data
x_given = [1, 2, 3, 4, 5]
y_given = [5, 7, 4, 6, 8]

# Plot scatter
plt.scatter(x_given, y_given, color='blue', label='Given Data')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Given Data Scatter Plot")
plt.legend()
plt.grid(True)
plt.show()
