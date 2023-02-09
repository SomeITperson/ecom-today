from django_filters import rest_framework as filters
from todo.models import Todo
# from .filters import DateExactRangeFilter

class TodoFilter(filters.FilterSet):
    created = filters.RangeFilter()

    class Meta:
        model = Todo
        fields = ('created',)