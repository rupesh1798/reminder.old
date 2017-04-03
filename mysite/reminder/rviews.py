import datetime, time
from threading import Timer
from django.shortcuts import render
from django.http import HttpResponse, Http404
from reminder.forms import ReminderForm
from reminder.models import Reminder
#from reminder.tasks import send_sms_reminder
# Create your views here.
def reminder_home(request):
    if request.method == 'POST':

        #print("valid")
        #form = ReminderForm(request.POST)

        #if form.is_valid():  # All the data is valid
        #    print("valid2")
        name = request.POST.get('name', '')
        time = request.POST.get('time', '')
        message = request.POST.get('message', '')
        phone_number = request.POST.get('phone_number', '')
        user_obj = Reminder(name=name, time=time, phone_number=phone_number, message=message)
        user_obj.save()
        #sec = (time - datetime.datetime.now()).total_seconds()
        #print(sec)
        # Schedule the Celery task
        from .tasks import send_sms_reminder
        t = Timer(5, send_sms_reminder)
        t.start()
        return render(request, 'reminder/reminder.html', {'user_obj': user_obj,'is_registered':True })
    else:
        form = ReminderForm()  # an unboundform

        return render(request, 'reminder/reminder.html', {'form': form})
def reminder_result(request):
    name = request.POST['name']
    time = request.POST['time']
    date = request.POST['date']
    message = request.POST['message']
    return render(request, 'reminder/reminder_result.html', {'name': name,'time': time, 'date':date, 'message': message})
