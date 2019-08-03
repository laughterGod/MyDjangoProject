from django.urls import path

from . import views

app_name = 'HiMyserver'
urlpatterns = [
    path('index/', views.index, name='index'),
    # ex: /HiMyserver/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /HiMyserver/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /HiMyserver/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('translate/<str:content>/', views.translateyoudao, name='translate'),

    path('ks3/storage/', views.ks3_storage, name='ks3_storage'),
    path('ks3/archive/', views.ks3_storage_archive, name='ks3_storage_archive'),
    path('ks3/storage/submit/', views.ks3_storage_submit, name='ks3_storage_submit'),

    path('eip/day_transfer/', views.eip_day_transfer, name='eip_day_transfer'),
    path('bws/day_transfer/', views.bws_day_transfer, name='bws_day_transfer'),
    path('eip/submit/', views.eip_submit, name='eip_submit'),

    path('csv/', views.csv_file_view, name='csv_file'),

]