from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
                path('', views.sessions_list, name='session_list'),
                path('registration', views.registration, name = 'registration'),
                path('login/', views.login_view, name = 'login'),
                path('logout/', views.logout_view, name = 'logout'),
                path('ses_det/', views.session_detail, name = 'session_detail'),
                path('film_det/<int:film_id>/', views.film_detail, name = 'film_detail'),
                path('purchase_ticket/<int:ses_id>/', views.purchase_ticket, name='purchase_ticket'),
                path('your_page/<int:user_id>/', views.page_user, name = 'your_page'),
                path('actor/<int:id>/', views.actor_info, name = 'actor_info')


                ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)