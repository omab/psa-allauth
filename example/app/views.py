from django.shortcuts import redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required

from .utils import render_to, clear_all_social_accounts


@render_to('home.html')
def home(request):
    # Ensure logged out session for propper demo testing
    if request.GET.get('reset') == '1':
        clear_all_social_accounts()
        if request.user.is_authenticated():
            logout(request)


@render_to('demo_feature_1.html')
def demo_feature_1(request):
    pass


@render_to('demo_feature_2.html')
def demo_feature_2(request):
    # Login a local user (user is created if doesn't exists)
    user = authenticate(username='foobar', password='passwd')
    login(request, user)


@render_to('demo_feature_3.html')
def demo_feature_3(request):
    pass


@render_to('demo_feature_4.html')
def demo_feature_4(request):
    pass


@render_to('demo_feature_5.html')
def demo_feature_5(request):
    pass


@render_to('demo_feature_6.html')
def demo_feature_6(request):
    pass


@render_to('validation_sent.html')
def validation_sent(request):
    return {'email': request.session.get('email_validation_address')}


@login_required
def primary_email(request, usa_id):
    usa_id = int(usa_id)
    for usa in request.user.social_auth.filter(provider='email'):
        usa.set_extra_data({'primary': usa.id == usa_id})
        usa.save()
    return redirect('demo_feature_6')
