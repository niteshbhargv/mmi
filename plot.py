import matplotlib.pyplot as plt
from datetime import datetime

# Read and parse the file
dates = []
values = []

with open('demofile2.txt', 'r') as file:
    for line in file:
        if ':' in line:
            date_str, value_str = line.strip().split(':')
            date = datetime.strptime(date_str.strip(), "%Y-%m-%d")
            value = float(value_str.strip())
            dates.append(date)
            values.append(value)

# Plotting the data
plt.figure(figsize=(10, 5))
plt.plot(dates, values, marker='o', linestyle='-', color='blue')
plt.title('Date vs Value Chart')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)
plt.show()

