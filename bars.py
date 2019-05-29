import json


def load_data(filepath):
    with open(filepath, "r") as f:
        return json.load(f)


def get_biggest_bar(data):
    seats_count = []
    for i in range(len(data["features"])):
        seats_count.append(data["features"][i]["properties"]['Attributes']["SeatsCount"])

    biggest = seats_count.index(max(seats_count))
    name = data["features"][biggest]["properties"]['Attributes']['Name']
    print("Самый большой бар - %s." % name)


def get_smallest_bar(data):
    seats_count = []
    for i in range(len(data["features"])):
        seats_count.append(data["features"][i]["properties"]['Attributes']["SeatsCount"])

    smallest = seats_count.index(min(seats_count))
    name = data["features"][smallest]["properties"]['Attributes']['Name']
    print("Самый маленький бар - %s." % name)


def get_closest_bar(data, longitude, latitude):
    x, y = longitude, latitude
    geo = []
    for i in range(len(data["features"])):
        place = data["features"][i]["geometry"]["coordinates"]
        distance = abs(x-place[0]) + abs(y-place[1])
        geo.append(distance)

    closest = geo.index(min(geo))
    name = data["features"][closest]["properties"]['Attributes']['Name']
    print("Самый близкий бар - %s" % name)


if __name__ == '__main__':
    data = load_data('1796.json')
    longitude = float(input("Введите вашу геопозицию(долготу): "))
    latitude = float(input("Введите вашу геопозицию(широту): "))

    get_biggest_bar(data)
    get_smallest_bar(data)
    get_closest_bar(data, longitude, latitude)
