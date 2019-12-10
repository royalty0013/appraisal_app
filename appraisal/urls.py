from django.conf.urls import url
from goalsetting import views
from appraisal import views
# 
urlpatterns = [
    url(r'^$', views.index, name='index' ),
    url(r'^login/$', views.login_process, name='login_process' ),
    url(r'^page/$', views.page, name='page' ),
    url(r'^appraisal_homepage/$', views.appr_handler, name='appraisal_homepage'),
    url(r'^appr_success_page/$', views.appr_success_page, name='appr_success_page'),
    url(r'^appr_approval_page/$', views.appraiser_suc_page, name='appr_approval_page'),
    url(r'^appr_approved_submission/$', views.reviewer_suc_page, name='appr_approved_submission'),
    url(r'^update_record/(?P<pk>\d+)/$', views.update_rec, name='update_record'),
    url(r'^update_rec/(?P<pk>\d+)/$', views.update_rec2, name='update_rec'),
    url(r'^appr_confirm/(?P<user>[\d+]+)/(?P<period_from>[\d\w\s\-]+)/(?P<period_to>[\d\w\s\-]+)/$', views.get_appr_details, name='appr_confirm'),
    url(r'^appr_approve/(?P<user>[\d+]+)/(?P<period_from>[\d\w\s\-]+)/(?P<period_to>[\d\w\s\-]+)/$', views.appr_approve, name='appr_approve'),
    url(r'^appr_review/(?P<user>[\d+]+)/(?P<period_from>[\d\w\s\-]+)/(?P<period_to>[\d\w\s\-]+)/$', views.get_appr_details_reviewer, name='appr_review'),
    url(r'^appr_final_approval/(?P<user>[\d+]+)/(?P<period_from>[\d\w\s\-]+)/(?P<period_to>[\d\w\s\-]+)/$', views.appr_final_approval, name='appr_final_approval'),
    url(r'^appr_final-form/(?P<user>[\d+]+)/(?P<period_from>[\d\w\s\-]+)/(?P<period_to>[\d\w\s\-]+)/$', views.get_appr_details_form, name='appr_final-form'),
    url(r'^logout/$', views.logOut, name='log_out'),
 ]