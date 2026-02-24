import matplotlib.pyplot as plt

n = int(input("Enter number of points: "))

x_values = []
y_values = []

for i in range(n):
    x = float(input(f"Enter x value for point {i+1}: "))
    y = float(input(f"Enter y value for point {i+1}: "))
    x_values.append(x)
    y_values.append(y)

# Plot scatter
plt.scatter(x_values, y_values, color='red', label='User Input Data')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("User Input Scatter Plot")
plt.legend()
plt.grid(True)
plt.show()
