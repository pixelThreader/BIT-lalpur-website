from django.core.mail import send_mail

send_mail(
    "Subject here",
    "This is test form Django",
    "piyush@piyush.com",
    ["piyush31032005@gmail.com"],
    fail_silently=False,
)