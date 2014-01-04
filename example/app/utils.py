from functools import wraps

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User

from social.apps.django_app.default.models import UserSocialAuth


def render_to(tpl):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            out = func(request, *args, **kwargs) or {}
            if isinstance(out, dict):
                out['request'] = request
                out = render_to_response(tpl, out, RequestContext(request))
            return out
        return wrapper
    return decorator


def clear_all_social_accounts():
    for usa in UserSocialAuth.objects.all():
        usa.delete()
    User.objects.exclude(username='foobar').delete()
