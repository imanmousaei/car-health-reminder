import json
import telegram

from consts import LIFETIME
from telegram_config import BOT_TOKEN, CHAT_ID


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

    return should_check


def get_formatted(should_check):
    from prettytable import PrettyTable
    table = PrettyTable(['Name', 'KM'])

    for key in should_check:
        row = [key, should_check[key]]
        table.add_row(row)
    
    return f'<pre>{table}</pre>'

def telegram_reminder(should_check):
    bot = telegram.Bot(token=BOT_TOKEN)
    bot.sendMessage(chat_id=CHAT_ID, text=get_formatted(should_check), parse_mode=telegram.ParseMode.HTML)


if __name__ == '__main__':
    should_check = check_car()
    telegram_reminder(should_check)
