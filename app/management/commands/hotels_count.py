from django.core.management.base import BaseCommand
from app.models import Hotel

class Command(BaseCommand):
    help = 'посчитать число отелей в базе'

    def handle(self, *args, **kwargs):
        hotels = Hotel.objects.count()
        self.stdout.write(u'Всего в базе "%s" отелей' % hotels)