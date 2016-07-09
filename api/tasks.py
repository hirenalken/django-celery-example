from api.models import User
from celery.task import task
from celery_demo import settings
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template


@task(name='api.tasks.user_welcome_mail')
def user_welcome_mail(user_id):
    user = User.objects.get(id=user_id)
    html_template = get_template('welcome_mail.html')
    content_passed_to_template = Context({'full_name': user.full_name})
    html_content = html_template.render(content_passed_to_template)
    send_email = EmailMessage(
        'Confirm Registration',
        html_content,
        settings.EMAIL_HOST_USER,
        [user.email],
    )
    send_email.content_subtype = "html"
    send_email.send()