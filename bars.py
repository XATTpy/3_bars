import json
import sys
from sys import argv

# Functions
def load_data(filepath):
    with open(filepath, "r") as json_file:
        return (json.loads(json_file.read()))["features"]


def get_biggest_bar(bars):
    biggest_bar = max(bars, key=bar_size)
    return biggest_bar["properties"]["Attributes"]


def get_smallest_bar(bars):
    smallest_bar = min(bars, key=bar_size)
    return smallest_bar["properties"]["Attributes"]


def get_closest_bar(bars, longitude, latitude):
    closest_bar = min(bars, key=bar_distance)
    return closest_bar["properties"]["Attributes"]


# Keys
def bar_size(bars): return bars["properties"]["Attributes"]["SeatsCount"]
def bar_distance(bars): return abs(sum(bars["geometry"]["coordinates"]) - (x+y))


# Exeptions and variable initialization
try:
    file_path = argv[1]
    bars = load_data(file_path)
except (IndexError, IsADirectoryError, FileNotFoundError):
    sys.exit("Введите путь к файлу в качестве аргумента при запуске. Прим.: python3 bars.py /path_to_file/file_name.json")
except ValueError:
    sys.exit("Файл имеет неверный формат.")

try:
    x = float(input("Введите вашу геолокацию(долготу): "))
    y = float(input("Введите вашу геолокацию(широту): "))
except ValueError:
    sys.exit("Неверный формат геолокации. Вводите координаты в числовом формате.")


if __name__ == "__main__":
    print("Самый большой бар - {}.".format(get_biggest_bar(bars)["Name"]))
    print("Самый маленький бар - {}.".format(get_smallest_bar(bars)["Name"]))
    print("Самый близкий бар - {}.".format(get_closest_bar(bars, x, y)["Name"]))
