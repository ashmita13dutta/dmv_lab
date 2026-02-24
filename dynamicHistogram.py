import matplotlib.pyplot as plt

n = int(input("Enter number of values: "))

data = []
for i in range(n):
    value = float(input(f"Enter value {i+1}: "))
    data.append(value)

plt.hist(data, bins=5) 
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("User Input Histogram")
plt.grid(True)
plt.show()
