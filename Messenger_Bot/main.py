import urllib.request
import ssl

from fbchat import Client
from fbchat.models import *

from Messenger_Bot import data

email = data.email
password = data.password


class Bot(Client):

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        Bot.game_thread_id = thread_id
        Bot.game_thread_type = thread_type

        if message_object.text is None:
            return
        mess = message_object.text.upper()

        if mess == 'TURN ON THE LAMP':
            client.send(Message(text='Turning the lamp on!'), thread_id=thread_id, thread_type=thread_type)

            content = urllib.request.urlopen("https://10.106.0.225/gpio/1", context=ssl.SSLContext()).read()

        if mess == 'TURN OFF THE LAMP':
            client.send(Message(text='Turning the lamp off!'), thread_id=thread_id, thread_type=thread_type)

            content = urllib.request.urlopen("https://10.106.0.225/gpio/0", context=ssl.SSLContext()).read()

        else:
            super(Bot, self).onMessage(author_id=author_id, message_object=message_object, thread_id=thread_id,
                                       thread_type=thread_type, **kwargs)


client = Bot(email, password)
client.listen()
