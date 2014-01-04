from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'example.app.views.home', name='home'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout',
        kwargs={'next_page': '/'}),
    url(r'^local-and-social-signup/$',
        'example.app.views.demo_feature_1',
        name='demo_feature_1'),
    url(r'^connecting-more-than-one-social-account/$',
        'example.app.views.demo_feature_2',
        name='demo_feature_2'),
    url(r'^disconnecting-a-social-account/$',
        'example.app.views.demo_feature_3',
        name='demo_feature_3'),
    url(r'^instant-signup/$',
        'example.app.views.demo_feature_4',
        name='demo_feature_4'),
    url(r'^email-verification-flow/$',
        'example.app.views.demo_feature_5',
        name='demo_feature_5'),
    url(r'^email-management/$',
        'example.app.views.demo_feature_6',
        name='demo_feature_6'),

    url(r'^email-sent/$', 'example.app.views.validation_sent'),
    url(r'^email-primary/(?P<usa_id>\d+)/$', 'example.app.views.primary_email',
        name='primary_email'),

    url(r'', include('social.apps.django_app.urls', namespace='social'))
)
