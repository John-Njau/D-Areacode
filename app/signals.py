from .models import Profile
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    

    # subject = 'Welcome to AreaCode'
    # sender= 'johnnjauv@gmail.com'
    
    # # passing in the context variables
    # text_content = render_to_string('email/newsemail.txt')
    # html_content = render_to_string('email/newsemail.html')
    
    # msg = EmailMultiAlternatives(subject, text_content, sender, [receiver])
    # msg.attach_alternative(html_content, "text/html")
    # msg.send()
    
    
        
         
            
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     try:
#         instance.profile.save()
#     except ObjectDoesNotExist:
#         Profile.objects.create(user=instance)
        

# @receiver(post_save, sender=User)
