import urllib.request
import ssl
import requests

from threading import Timer
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

        if mess == 'TURN BED':
            client.send(Message(text='Turning on the lamp!'), thread_id=thread_id, thread_type=thread_type)

            content = urllib.request.urlopen("https://10.106.0.225/lamp1/1", context=ssl.SSLContext()).read()

        if mess == 'TURN OFF BED':
            client.send(Message(text='Turning off the lamp!'), thread_id=thread_id, thread_type=thread_type)

            content = urllib.request.urlopen("https://10.106.0.225/lamp1/0", context=ssl.SSLContext()).read()

        if mess == 'TURN HALL':
            client.send(Message(text='Turning on the lamp!'), thread_id=thread_id, thread_type=thread_type)

            content = urllib.request.urlopen("https://10.106.7.2/lamp2/1", context=ssl.SSLContext()).read()

        if mess == 'TURN OFF HALL':
            client.send(Message(text='Turning off the lamp!'), thread_id=thread_id, thread_type=thread_type)

            content = urllib.request.urlopen("https://10.106.7.2/lamp2/0", context=ssl.SSLContext()).read()

        if mess == 'CURRENT TEMPERATURE':

            url = "http://10.106.7.80/"
            f = requests.get(url)

            html = requests.get(url).text

            list = html.splitlines()

            print(list[3])
            print(list[6])

            client.send(Message(text='Temperature: '+list[3]+'°C'+'\nHumidity: '+list[6]+'%'), thread_id=thread_id, thread_type=thread_type)

        else:
            super(Bot, self).onMessage(author_id=author_id, message_object=message_object, thread_id=thread_id,
                                       thread_type=thread_type, **kwargs)


client = Bot(email, password)
client.listen()
