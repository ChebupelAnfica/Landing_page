from django.core.mail import send_mail
from django.template.loader import render_to_string

def send_application_email(subject: str, template_name: str, context: dict, recipient_list: list):
    """
    Отправляет письмо на указанные адреса, рендеря шаблон.
    """
    message = render_to_string(template_name, context)
    send_mail(
        subject=subject,
        message='',
        html_message=message,
        from_email=None,  # используем DEFAULT_FROM_EMAIL
        recipient_list=recipient_list,
        fail_silently=False,
    )
