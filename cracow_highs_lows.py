import csv

import matplotlib.pyplot as plt

from datetime import datetime

filename = 'project_2/chapter_16/Cracow_High_Lows_Temp/2985622.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')

    # Downloading maximum temperatures from file .csv
    highs = []
    lows = []
    dates = []
    place_name = ''
    for row in reader:  
        current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
        if not place_name:
            place_name = row[name_index]
        try:     
            high = float(row[high_index])
            low = float(row[low_index])
        except ValueError:
            print(f"No data found for {current_date}.")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

# Chart data
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', linewidth=0.7, alpha=0.9)
ax.plot(dates, lows, c='blue', linewidth=0.7, alpha=0.9)
ax.fill_between(dates, highs, lows, facecolor='orange', alpha=0.3)

# Chart formatting
ax.set_title(f"Highest and lowest temperature by day at station "
    f"{place_name}, 2021", fontsize=12)
ax.set_xlabel("Time", fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel('Temperature [$^\circ$C]', fontsize=10) #LaTeX interpreter
ax.tick_params(axis='both', which='major', labelsize=10)
plt.ylim(-10, 60)

plt.show()



