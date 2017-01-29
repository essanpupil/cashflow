import django_tables2 as table

from cash.models import Activity


class ActivityListTable(table.Table):
    class Meta:
        model = Activity
        attrs = {'id': 'activity_list'}