from django.apps import AppConfig


class MyinventoryUsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "myinventory_users"

    def ready(self):
        import myinventory_users.signals