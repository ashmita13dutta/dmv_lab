import matplotlib.pyplot as plt

n = int(input("Enter number of categories: "))

labels = []
values = []

for i in range(n):
    label = input(f"Enter label {i+1}: ")
    value = int(input(f"Enter value for {label}: "))
    labels.append(label)
    values.append(value)

plt.bar(labels, values, color='orange')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart (User Input Data)')
plt.show()
