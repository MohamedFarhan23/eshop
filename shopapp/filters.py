import django_filters
from .models import *
from .forms import *

class Filter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['title']