import json
from time import sleep
import telegram
import asyncio
from prettytable import PrettyTable

from consts import INTERVAL_IN_S, LIFETIME
from telegram_config import BOT_TOKEN, CHAT_ID


def load_config():
    f = open('config.json')
    config = json.load(f)
    return config


def check_car():
    should_check = dict()

    config = load_config()
    last_changes = config["last_changes"]
    check_intervals = config["check_intervals"]

    for key in check_intervals:
        should_check_km = last_changes.get(key, 0) + check_intervals[key]
        if config["only_write_should_be_checked_items"]:
            if should_check_km <= config["now_km"]:
                should_check[key] = should_check_km
        else:
            should_check[key] = should_check_km

    should_check = dict(sorted(should_check.items(), key=lambda item: item[1]))
    json.dump(should_check, open('should_check.json', 'w'), indent=4)

    return should_check


def get_formatted(should_check):
    table = PrettyTable(['Name', 'KM'])

    for key in should_check:
        row = [key, should_check[key]]
        table.add_row(row)
    
    return f'<pre>{table}</pre>'

def telegram_reminder(should_check):
    bot = telegram.Bot(token=BOT_TOKEN)
    asyncio.run(bot.sendMessage(chat_id=CHAT_ID, text=get_formatted(should_check), parse_mode="HTML"))


if __name__ == '__main__':
    should_check = check_car()
    telegram_reminder(should_check)
    # sleep(INTERVAL_IN_S)
