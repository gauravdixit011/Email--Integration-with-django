from django.db.models.signals import post_save 
from django.dispatch import receiver

from myapp.models import Student

@receiver(post_save, sender=Student)
def student_created(sender, instance, created, **kwargs):
        if created:
                print("New Student Added")
