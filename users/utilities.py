from django.template.loader import render_to_string
from django.core.signing import Signer

from tmanager.settings import ALLOWED_HOSTS


signer = Signer()
def send_activation_notification(user):
    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:9000'
    context = {'user': user, 'host': host, 'sign': signer.sign(user.username)}
    subject = render_to_string('email/activation_letter_subject.txt', context)
    body_text = render_to_string('email/activation_letter_body.txt', context)
    print("Письмо отправлено")
    user.email_user(subject, body_text)
    
def send_password_reset_instruction(user):
    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:9000'
    context = {'user': user, 'host': host, 'sign': signer.sign(user.username)}
    subject = render_to_string('email/password_reset_letter_subject.txt', context)
    body_text = render_to_string('email/password_reset_letter_body.txt', context)
    return [subject, body_text]