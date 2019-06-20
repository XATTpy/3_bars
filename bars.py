import json
from sys import argv
from functools import partial


def load_data(filepath):
    with open(filepath, "r") as json_file:
        return (json.loads(json_file.read()))["features"]


def get_biggest_bar(bars):
    biggest_bar = max(bars, key=get_bar_sizes)
    return biggest_bar


def get_smallest_bar(bars):
    smallest_bar = min(bars, key=get_bar_sizes)
    return smallest_bar


def get_closest_bar(bars, longitude, latitude):
    x, y = longitude, latitude
    calculation = partial(get_distances_to_bars, longitude=x, latitude=y)
    closest_bar = min(bars, key=calculation)
    return closest_bar


def get_bar_sizes(bars):
    return bars["properties"]["Attributes"]["SeatsCount"]


def get_distances_to_bars(bars, longitude, latitude):
    return abs(sum(bars["geometry"]["coordinates"]) - (longitude+latitude))


def show_bar(bar):
    print (bar["properties"]["Attributes"]["Name"])


def main():
    try:
        file_path = argv[1]
        bars = load_data(file_path)
        longitude = float(input("Введите вашу геолокацию(долготу): "))
        latitude = float(input("Введите вашу геолокацию(широту): "))
        return bars, longitude, latitude
    except (IndexError, IsADirectoryError):
        quit("Введите путь к файлу в качестве аргумента при запуске.")
    except FileNotFoundError:
        quit("Такого файла не существует")
    except json.decoder.JSONDecodeError:
        quit("Файл имеет неверный формат.")
    except ValueError:
        quit("Координата имеет неверный формат.")


if __name__ == "__main__":
    bars, longitude, latitude = main()

    print("Самый большой бар - ", end="")
    show_bar(get_biggest_bar(bars))
    print("Самый маленький бар - ", end="")
    show_bar(get_smallest_bar(bars))
    print("Самый близкий бар - ", end="")
    show_bar(get_closest_bar(bars, longitude, latitude))
