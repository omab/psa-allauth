from django.template import RequestContext
from django.shortcuts import render_to_response

from social.pipeline.partial import partial


@partial
def password_check(strategy, user, *args, **kwargs):
    if not user.has_usable_password() and user.social_auth.count() == 1:
        if strategy.request.POST.get('password'):
            user.set_password(strategy.request.POST['password'])
            user.save()
        else:
            return render_to_response('require_password.html', {
                'request': strategy.request,
                'next': strategy.request.POST.get('next') or ''
            }, RequestContext(strategy.request))


def set_password(strategy, backend, user, response, is_new=False,
                 *args, **kwargs):
    if backend.name in ('email', 'username') and is_new and \
       response.get('password'):
        user.set_password(response['password'])
        user.save()
