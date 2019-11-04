from django.apps import AppConfig


class PrivateProfilesConfig(AppConfig):
    name = 'private_profiles'

    def ready(self):
        import private_profiles.signals