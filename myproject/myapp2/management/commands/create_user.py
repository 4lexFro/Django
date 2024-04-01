from django.core.management.base import BaseCommand
from myapp2.models import User
# запуск командой python manage.py create_user

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        #user = User(name='John', email='john@example.com', password='secret', age=25)
        #user = User(name='Neo', email='neo@example.com', password='secret', age=58)
        #user = User(name='Jack', email='jjj@example.com', password='secret', age=78)
        user = User(name='Alyosha', email='4lexfro@example.com', password='qwerty', age=46)
        user.save()
        self.stdout.write(f'{user}')
