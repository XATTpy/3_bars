import json


def load_data(filepath):
    with open(filepath, "r") as json_file:
        return (json.loads(json_file.read()))["features"]


def get_biggest_bar(bars):
    biggest_bar = max(bars, key=lambda seats_count: seats_count["properties"]["Attributes"]["SeatsCount"])
    return biggest_bar["properties"]["Attributes"]["Name"]


def get_smallest_bar(bars):
    smallest_bar = min(bars, key=lambda seats_count: seats_count["properties"]["Attributes"]["SeatsCount"])
    return smallest_bar["properties"]["Attributes"]["Name"]


def get_closest_bar(bars, longitude, latitude):
    x, y = longitude, latitude
    closest_bar = min(bars, key=lambda geo: abs(sum(geo["geometry"]["coordinates"]) - (x+y)))
    return closest_bar["properties"]["Attributes"]["Name"]


if __name__ == "__main__":
    file_path = input("Введите путь к файлу json: ")
    bars = load_data(file_path)
    longitude = float(input("Введите вашу геопозицию(долготу): "))
    latitude = float(input("Введите вашу геопозицию(широту): "))

    print("Самый большой бар - {}.".format(get_biggest_bar(bars)))
    print("Самый маленький бар - {}.".format(get_smallest_bar(bars)))
    print("Самый близкий бар - {}.".format(get_closest_bar(bars, longitude, latitude)))
