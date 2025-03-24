from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Updates admin user and password for testing"

    def add_arguments(self, parser):
        parser.add_argument("-p", nargs="?", dest="password", const=str)
        parser.add_argument("-u", nargs="?", dest="username", const=str, default="admin")

    def handle(self, *args, **options):
        print("updated username/password for user:", options.get("username"), options.get("password"))

        User = get_user_model()
        try:
            user = User.objects.get(username=options.get("username"))
            user.set_password(options.get("password"))
            user.save()
        except User.DoesNotExist:
            user = User.objects.create(username=options.get("username"),
                                       is_superuser=True,
                                       is_staff=True)
            user.set_password(options.get("password"))
            user.save()
