import matplotlib.pyplot as plt


categories = ['A', 'B', 'C', 'D']
bar_values = [10, 15, 7, 12]
scatter_values = [5, 7, 4, 6]  

x_pos = range(len(categories))

plt.figure(figsize=(8, 6))


plt.bar(x_pos, bar_values, color='skyblue', label='Bar Values')


plt.scatter(x_pos, scatter_values, color='red', s=80, label='Scatter Points', zorder=5)


plt.xticks(x_pos, categories)


plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Merged Bar and Scatter Plot")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()
