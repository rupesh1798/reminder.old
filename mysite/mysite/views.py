from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
import datetime
from django.shortcuts import render
from mysite.forms import ContactForm
from django.core.mail import send_mail

def hello(request):
    return HttpResponse("Hello world")
def home(request):
    return HttpResponse("This is Home page")
def time(request):
    time = datetime.datetime.now()
    return render(request,'time.html',{'current_date':time})
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hour(s), it will be  %s." % (offset, dt)
    return HttpResponse(html)
def html(request):
    return render(request,'home1.html')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':
form})
