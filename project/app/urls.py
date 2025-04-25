from django.urls import path
from app import views

urlpatterns = [
    path('',views.home),
    path('clo',views.c_login,name='log'),
    path('ulo',views.u_login,name='logi'),
    path('clog',views.c_login),
    path('creg',views.c_reg),
    path('ulog',views.u_login),
    path('ureg',views.u_reg),
    path('cdetails',views.c_details),
    path('forms',views.form),
    path('profile',views.company_profiles),
    path('cpro',views.u_profile),
    path('update',views.update),
    path('change',views.change_password),
    path('updates',views.u_update),
    path('uchange',views.uchange_password),
    path('jobs',views.cjob_list),
    path('job',views.u_job),
    path('search',views.search),
    path('single<str:pk>',views.job_view,name='detail'),
    path('uform<str:pk>',views.u_form,name='uforms'),
    path('table<str:pk>',views.applicant_details,name='table'),
    path('udetails',views.applied_job,name='udetails'),
    path('thks',views.thanks),
    path('log',views.logout_user),
    path('resum<str:pk>',views.resume,name='resum'),
    path('delete',views.delete),

]   