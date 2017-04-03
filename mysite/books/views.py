from django.shortcuts import render
from django.http import HttpResponse, Http404
from books.models import Book
# Create your views here.

#def search_form(request):
#    return render(request, 'search_form.html')
def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_result.html',
                          {'books': books, 'query': q})
    return render(request, 'search_form.html', {'error': errors})
def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
