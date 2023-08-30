from django.apps import AppConfig

import django.dispatch 

from .utilities import send_activation_notification, send_password_reset_instruction

user_registered = django.dispatch.Signal(['instance'])
password_reset = django.dispatch.Signal(['instance'])

def user_registered_dispatcher(sender, **kwargs):
    print('dispatcher1')
    send_activation_notification(kwargs['instance']) 

def password_reset_dispatcher(sender, **kwargs):
    print('dispatcher2')
    send_password_reset_instruction(kwargs['instances']) 

user_registered.connect(user_registered_dispatcher)
password_reset.connect(password_reset_dispatcher)


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
