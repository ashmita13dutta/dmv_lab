import matplotlib.pyplot as plt

# User input
n = int(input("Enter number of categories: "))

user_labels = []
user_values = []

for i in range(n):
    label = input(f"Enter label {i+1}: ")
    value = float(input(f"Enter value for {label}: "))
    user_labels.append(label)
    user_values.append(value)

# Plot pie chart
plt.pie(user_values, labels=user_labels, autopct='%1.1f%%')
plt.title("User Input Pie Chart")
plt.show()
