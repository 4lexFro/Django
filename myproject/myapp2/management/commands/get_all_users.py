from django.core.management.base import BaseCommand
from myapp2.models import User
# запуск командой python manage.py get_all_users

class Command(BaseCommand):
    help = "Get all users."

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        self.stdout.write(f'{users}')
 