from django.core.management.base import BaseCommand
from myapp2.models import User
# запуск командой python manage.py get_user_by_id 2 # 2 это id юзера,который нам нужен

class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        user = User.objects.get(id=id)
        self.stdout.write(f'{user}')