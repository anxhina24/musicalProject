import codecs
import csv
import urllib
from django.http import HttpResponseRedirect
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from .serializers import WorksSerializer
from .models import Works
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'navbar/mainpage.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['works'] = Works.objects.all()
        return context

# class WorksViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet,):
#     serializer_class = WorksSerializer
#     queryset = Works.objects.all()

def upload(request):
    if request.method == 'POST':
        file = request.FILES['file']
        if file.content_type == 'text/csv':
            handle_uploaded_file(file)
            args = {"status": True}
            return HttpResponseRedirect("/?{}".format(urllib.parse.urlencode(args)))
        else:
            args = {"status": False}
            return HttpResponseRedirect("/?{}".format(urllib.parse.urlencode(args)))


def handle_uploaded_file(file):
    for row in csv.reader(codecs.iterdecode(file, 'utf-8')):
        if row != ['title', 'contributors', 'iswc']:
            try:
                obj = {
                    'title': row[0],
                    'contributors': row[1].split('|'),
                    'iswc': row[2]
                }
                work = Works.objects.get(iswc=row[2])
                Works.objects.filter(iswc=row[2]).update(
                    contributors=work.contributors + list(set(obj['contributors']) - set(work.contributors)))
            except Works.DoesNotExist:
                if Works.objects.filter(title=obj['title'], contributors=obj['contributors']):
                    Works.objects.filter(title=obj['title'], contributors=obj['contributors']).update(iswc=obj['iswc'])
                else:
                    work = Works.objects.create(**obj)
                    work.save()