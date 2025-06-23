import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

# Display menu and return user's choice
def display_menu():
   print("\nType 'highs' to display the high temperatures")
   print("Type 'lows' to display the low temperatures")
   print("Type 'exit' to exit the program")
   return input("Enter your choice: ").strip().lower()

# Read weather from .csv
def read_weather(file, weather_type='highs'):
    dates, temps = [], []
    # Use col 5 if high temps, 6 if low temps
    index = 5 if weather_type == 'highs' else 6
    with open(file) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            temp = int(row[index])
            temps.append(temp)

    return dates, temps

# Plot temperature data
def plot(dates, temps, weather_type='highs'):
    color = 'red' if weather_type == 'highs' else 'blue'
    label = 'High' if weather_type == 'highs' else 'Low'

    fig, ax = plt.subplots()
    ax.plot(dates, temps, color=color)

    # Format plot.
    plt.title(f"Daily {label} temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

# Main loop
if __name__ == '__main__':
    while True:
        user_input = display_menu()

        if user_input == 'exit':
            print("Goodbye")
            sys.exit()
        elif user_input == 'highs':
            dates, highs = read_weather(filename, weather_type='highs')
            plot(dates, highs, weather_type='highs')
        elif user_input == 'lows':
            dates, lows = read_weather(filename, weather_type='lows')
            plot(dates, lows, weather_type='lows')
        else:
            print("Please enter a valid choice (highs, lows, exit).")