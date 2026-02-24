import matplotlib.pyplot as plt

# Given data
given_labels = ['Apples', 'Bananas', 'Cherries']
given_values = [30, 20, 50]

# Plot pie chart
plt.pie(given_values, labels=given_labels, autopct='%1.1f%%')
plt.title("Given Data Pie Chart")
plt.show()
