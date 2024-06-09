from django.conf import settings
from django.core.mail import send_mail


def send_single_mail():
    subject="Testing Mail System!!"
    message="Testing Mail System built with Django in 2024!!"
    from_email = settings.EMAIL_HOST_USER
    recipient = ['pr987rana@gmail.com']
    obj ={}

    try:
        send_mail(
            subject=subject, 
            message=message, 
            from_email=from_email, 
            recipient_list= recipient
            )
        obj['status'] = 200
        obj['status_desc'] = 'Success'
        obj['desc'] = 'Email Sent Successfully!'
    except Exception as e:
        obj['status'] = 500
        obj['status_desc'] = 'Internal Server Error'
        obj['desc'] = e
    return obj