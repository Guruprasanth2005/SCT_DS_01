import matplotlib.pyplot as plt

# Create the bar chart
plt.figure(figsize=(12, 6))  # Adjust figure size for better readability
plt.bar(df['Year'], df['Population'], color='skyblue')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Population", fontsize=12)
plt.title("India's Population over the Years", fontsize=14)
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels if they overlap
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()  # Adjust layout to prevent labels from overlapping
plt.show()