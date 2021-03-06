# RTM
from slackclient import SlackClient
from slacker import Slacker
from botengine import make_reply
import time


slack_token = '슬랙토큰'
channel = '#채널명'
sc = SlackClient(slack_token)


def notification(message):
    global slack_token
    global channel
    slack = Slacker(slack_token)
    slack.chat.post_message(channel, message)


if sc.rtm_connect():
    print('Connected from slack')

    while True:
        receive_data = sc.rtm_read()

        if len(receive_data):
            keys = list(receive_data[0].keys())
            if 'type' in keys and 'text' in keys and 'user' in keys:
                print(receive_data[0])
                message = receive_data[0]['text']
                new_sentence =  make_reply(message)
                notification(new_sentence)
        time.sleep(1)

else:
    print ("Connection Failed")