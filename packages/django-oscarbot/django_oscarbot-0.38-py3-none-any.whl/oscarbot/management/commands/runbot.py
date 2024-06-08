import json

import requests
from django.conf import settings
from django.core.management import BaseCommand

from oscarbot.services import get_bot_model
from oscarbot.views import handle_content


class Command(BaseCommand):

    def handle(self, *args, **options):
        bot_model = get_bot_model()
        bot = bot_model.objects.all().first()
        if bot:
            bot_token = bot.token
        else:
            bot_token = settings.TELEGRAM_BOT_TOKEN
        offset = 0
        try:
            while True:
                url = f'{settings.TELEGRAM_URL}{bot_token}/getUpdates?offset={offset}'
                response = requests.get(url, timeout=60)
                total_message = b''
                for message in response:
                    total_message += message
                body = total_message.decode('utf-8')
                body = body.replace('\n', '')
                content = json.loads(body)
                if content.get('ok'):
                    if len(content['result']) > 0:
                        offset = int(content['result'][0]['update_id']) + 1
                        if offset > 0:
                            handle_content(bot.token, content['result'][0])
                else:
                    raise ValueError
        except ValueError as e:
            print(f'Token from Telegram not found\n{e}')
        except AttributeError as e:
            print(f'Add the bot token to the database in {bot_model}\n{e}')
        except KeyboardInterrupt:
            print('Exit bot server')
