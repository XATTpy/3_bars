import json


def load_data(filepath):
    with open(filepath, "r") as json_file:
        return json.load(json_file)


def get_biggest_bar(bars):
    seats_count = []
    for bar_number in range(len(bars["features"])):
        seats_count.append(bars["features"][bar_number]["properties"]["Attributes"]["SeatsCount"])

    biggest = seats_count.index(max(seats_count))
    bar_name = bars["features"][biggest]["properties"]["Attributes"]["Name"]
    return bar_name


def get_smallest_bar(bars):
    seats_count = []
    for bar_number in range(len(bars["features"])):
        seats_count.append(bars["features"][bar_number]["properties"]["Attributes"]["SeatsCount"])

    smallest = seats_count.index(min(seats_count))
    bar_name = bars["features"][smallest]["properties"]["Attributes"]["Name"]
    return bar_name


def get_closest_bar(bars, longitude, latitude):
    x, y = longitude, latitude
    geo = []
    for bar_number in range(len(bars["features"])):
        place = bars["features"][bar_number]["geometry"]["coordinates"]
        distance = abs(x-place[0]) + abs(y-place[1])
        geo.append(distance)

    closest = geo.index(min(geo))
    bar_name = bars["features"][closest]["properties"]["Attributes"]["Name"]
    return bar_name


if __name__ == "__main__":
    bars = load_data("1796.json")
    longitude = float(input("Введите вашу геопозицию(долготу): "))
    latitude = float(input("Введите вашу геопозицию(широту): "))

    get_biggest_bar(bars)
    get_smallest_bar(bars)
    get_closest_bar(bars, longitude, latitude)
