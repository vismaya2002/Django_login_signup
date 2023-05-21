import os
from dotenv import load_dotenv, find_dotenv
from twilio.rest import Client
load_dotenv(find_dotenv())


def sms(tonum,data):

    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

    client = Client(account_sid, auth_token)
    client.messages.create(from_=os.environ.get('TWILIO_PHONE_NUMBER'),
                       to=tonum,
                       body=data)