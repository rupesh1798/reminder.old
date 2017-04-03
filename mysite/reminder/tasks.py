#from celery import shared_task
from django.conf import settings
from twilio.rest import TwilioRestClient
#import arrow
from .models import Reminder
account_sid = "ACa6d4cb06b269945f34462a435110511f"
auth_token = "4c74480dcf8daab2fc8a078e5ca40d43"
client = TwilioRestClient(account_sid, auth_token)

#@shared_task
def send_sms_reminder(reminder_id=1):
    try:
        reminder = Reminder.objects.get(pk=reminder_id)
        print(reminder)
    except Reminder.DoesNotExist:

        return

    #reminder_time = arrow.get(reminder.time)
    #reminder_message = arrow.get(reminder.message)
    body = 'Hi '+ reminder.name +'. You have a remininder for' + reminder.message

    message = client.messages.create(
        body='rupesh',
        to="+917610002521",
        from_="+13176224171",
    )
