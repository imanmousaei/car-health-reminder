import json

from consts import LIFETIME


def load_config():
    f = open('config.json')
    config = json.load(f)
    return config


def check_car():
    should_check = dict()
    config = load_config()
    last_changes = config["last_changes"]

    for key in last_changes:
        value = last_changes[key]
        should_check[key] = value + LIFETIME[key]

    should_check = dict(sorted(should_check.items(), key=lambda item: item[1]))
    json.dump(should_check, open('should_check.json', 'w'), indent=4)

    for key in should_check:
        print(f"You should check {key} at {should_check[key]} km")


if __name__ == '__main__':
    check_car()
