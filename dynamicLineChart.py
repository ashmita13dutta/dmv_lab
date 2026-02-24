import matplotlib.pyplot as plt

n = int(input("Enter number of data points: "))

y = []
for i in range(n):
    value = float(input(f"Enter value {i+1}: "))
    y.append(value)

plt.plot(y, marker='o')
plt.xlabel("Data Point")
plt.ylabel("Value")
plt.title("Simple Line Chart")
plt.grid(True)
plt.show()
