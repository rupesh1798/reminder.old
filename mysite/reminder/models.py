#from __future__ import unicode_literals
import datetime, time
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from threading import Timer
#from .tasks import send_sms_reminder
# Create your models here.
class Reminder(models.Model):
    name = models.CharField(max_length=150)
    time = models.DateTimeField()
    phone_number = models.CharField(max_length=15)
    message = models.CharField(max_length=150)
    task_id = models.CharField(max_length=50, blank=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    def schedule_reminder(self):
        #Schedules a Celery task to send a reminder

        ''' Calculate the correct time to send this reminder
        appointment_time = arrow.get(self.time, self.time_zone.zone)
        reminder_time = appointment_time.replace(minutes=-settings.REMINDER_TIME)'''
        sec = (self.time - datetime.datetime.now()).total_seconds()
        print(sec)
        # Schedule the Celery task
        from .tasks import send_sms_reminder
        t = Timer(5, send_sms_reminder)
        t.start()
        '''t = datetime.datetime.strptime(self.time, '%Y-%m-%dT%H:%M')
        result = send_sms_reminder.apply_async((self.pk,), eta=t)

        return result.id
    def save(self, *args, **kwargs):
        Custom save method which also schedules a reminder

        # Check if we have scheduled a reminder for this appointment before
        if self.task_id:
            # Revoke that task in case its time has changed
            celery_app.control.revoke(self.task_id)

        # Save our appointment, which populates self.pk,
        # which is used in schedule_reminder
        super(Reminder, self).save(*args, **kwargs)

        # Schedule a new reminder task for this appointment
        self.task_id = self.schedule_reminder()

        # Save our appointment again, with the new task_id
        super(Appointment, self).save(*args, **kwargs)'''
