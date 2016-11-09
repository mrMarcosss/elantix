from django.db.models.query_utils import Q
from django.views.generic import ListView
from rest_framework.generics import ListAPIView
from persons.models import Person
from persons.serializers import PersonsListSerializer


class PersonListView(ListView):
    template_name = 'persons/person.html'

    def get_queryset(self):
        return Person.objects.all()


class PersonsListView(ListAPIView):
    serializer_class = PersonsListSerializer

    def get_queryset(self):
        word = self.request.query_params.get('word')
        if word:
            return Person.objects.filter(
                Q(name__startswith=word) |
                Q(last_name__startswith=word) |
                Q(phone_number__startswith='+'+str(word).strip()) |
                Q(address__startswith=word)
            )
        else:
            return Person.objects.order_by('-name')
