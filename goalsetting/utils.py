from django.contrib.auth.models import User
import ldap
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def ldapLogin(username, password):
    con = ldap.initialize('ldap://dc.abujaelectricity.com', bytes_mode=False)
    try:
        con.simple_bind_s(username, password)
    except Exception as e:
        return e
    return True


def checkUser(username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return False
    return True


def createOrGetUser(username):
    if checkUser(username):
        return User.objects.get(username=username)
    else:
        first_name = username.split('@')[0].split('.')[0]
        last_name = username.split('@')[0].split('.')[1]
        user = User(first_name=first_name, last_name=last_name, email=username, username=username)
        user.save()
        return user


def build_email(from_address, to_address, subject, txt_template, html_template, context, cc=None):
    msg_html = render_to_string(html_template, context)
    msg_plain = render_to_string(txt_template, context)
    msg_plain = strip_tags(msg_plain)
    email = {}
    email['from'] = from_address
    email['to'] = to_address
    email['subject'] = subject
    email['txt_message'] = msg_plain.strip()
    email['html_message'] = msg_html
    if cc is not None:
        email['cc'] = cc
    return email


def send_emailv2(e_build):
    try:
        msg = EmailMultiAlternatives(e_build['subject'], e_build['txt_message'], e_build['from'], [e_build['to']],
                                     cc=e_build['cc'])
        msg.attach_alternative(e_build['html_message'], "text/html")
        msg.send()
    except Exception as e:
        print(e)
        pass


def send_email(e_build):
    try:
        send_mail(e_build['subject'], e_build['txt_message'], e_build['from'], [e_build['to']], fail_silently=False,
                  html_message=e_build['html_message'])
    except Exception as e:
        print(e)
        pass


def build_and_send_email(from_address, to_address, subject, txt_template, html_template, context, cc):
    e_build = build_email(from_address, to_address, subject, txt_template, html_template, context, cc)
    send_emailv2(e_build)
