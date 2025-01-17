from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from User.models import UserProfile

class Command(BaseCommand):
    help = 'Create missing UserProfile objects for existing users'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        created_profiles = 0

        for user in User.objects.all():
            if not hasattr(user, 'profile'):  # 프로필이 없는 사용자 확인
                UserProfile.objects.create(user=user)
                created_profiles += 1

        self.stdout.write(self.style.SUCCESS(
            f'{created_profiles} missing UserProfile(s) created successfully.'
        ))
