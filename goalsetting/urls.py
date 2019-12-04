from django.conf.urls import url
from goalsetting import views

# 
urlpatterns = [
    url(r'^$', views.index, name='index' ),
    # url(r'^appraisal_homepage/$', views.appraisal_homepage, name='appraisal_homepage' ),
    url(r'^login/$', views.login_process, name='login_process' ),
    url(r'^homepage/$', views.goal_handler, name='homepage'),
    url(r'^success_page/$', views.success_page, name='success_page'),
    url(r'^approval_page/$', views.appr_suc_page, name='approval_page'),
    url(r'^approved_submission/$', views.final_suc_page, name='approved_submission'),
    # url(r'^update_record/(?P<pk>\d+)/$', views.update_rec, name='update_record'),
    # url(r'^update_rec/(?P<pk>\d+)/$', views.update_rec2, name='update_rec'),
    # url(r'^confirm/(?P<user>[\d+]+)/(?P<period_from>[\d\w\s\-]+)/(?P<period_to>[\d\w\s\-]+)/$', views.get_details, name='confirm'),
    # url(r'^approve/(?P<user>[\d+]+)/(?P<period_from>[\d\w\s\-]+)/(?P<period_to>[\d\w\s\-]+)/$', views.approve, name='approve'),
    # url(r'^review/(?P<user>[\d+]+)/(?P<period_from>[\d\w\s\-]+)/(?P<period_to>[\d\w\s\-]+)/$', views.get_details_reviewer, name='review'),
    # url(r'^final_approval/(?P<user>[\d+]+)/(?P<period_from>[\d\w\s\-]+)/(?P<period_to>[\d\w\s\-]+)/$', views.final_approval, name='final_approval'),
    # url(r'^final-form/(?P<user>[\d+]+)/(?P<period_from>[\d\w\s\-]+)/(?P<period_to>[\d\w\s\-]+)/$', views.get_details_form, name='final-form'),
    # url(r'^logout/$', views.logOut, name='log_out'),

    #url(r'^form_submission/$', views.goal_handler, name='goal_form_submission' ),
 ]