from django.urls import path, reverse_lazy
from PatinhadoWeb import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import (
    LoginView, PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
)

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/editar/', views.EditProfileView.as_view(), name='edit_profile'),
    path('profile/excluir/', views.DeleteProfileView.as_view(), name='delete_profile'),
    path('login/', LoginView.as_view(template_name="PatinhadoWeb/auth/Login.html"), name='login'),
    path('register/', views.registro, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='PatinhadoWeb/auth/password_change_form.html',
        success_url=reverse_lazy('password_change_done')
    ), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(
        template_name='PatinhadoWeb/auth/password_change_done.html'
    ), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='PatinhadoWeb/auth/password_reset_form.html',
        email_template_name='PatinhadoWeb/auth/password_reset_email.html',
        success_url=reverse_lazy('password_reset_done')
    ), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='PatinhadoWeb/auth/password_reset_done.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='PatinhadoWeb/auth/password_reset_confirm.html',
        success_url=reverse_lazy('password_reset_complete')
    ), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='PatinhadoWeb/auth/password_reset_complete.html'
    ), name='password_reset_complete'),
    path('aboutus/', views.about, name='about'),
    path('list/', views.home, name='list'),
    path('contact/', views.contact, name='contact'),
    path('pets/', views.PetListView.as_view(), name='listapets'),
    path('pets/<int:pk>/', views.PetDetailView.as_view(), name='detalhepet'),
    path('pets/<int:pk>/adotar/', views.PedidoAdocaoCreateView.as_view(), name='adotar_pet'),
    path('pedidos/<int:pk>/', views.PedidoAdocaoDetailView.as_view(), name='detalhe_pedido'),
    path('pedidos/<int:pk>/editar/', views.PedidoAdocaoUpdateView.as_view(), name='edit_pedido'),
    path('pedidos/<int:pk>/cancelar/', views.PedidoAdocaoDeleteView.as_view(), name='cancela_pedido'),
    path('pedidos/<int:pk>/aprovar/', views.PedidoAdocaoAprovarView.as_view(), name='aprova_pedido'),
    path('pedidos/<int:pk>/rejeitar/', views.PedidoAdocaoRejeitarView.as_view(), name='rejeita_pedido'),
    path('pets/add/', views.PetCreateView.as_view(), name='addpet'),
    path('pets/<int:pk>/editar/', views.PetUpdateView.as_view(), name='editapet'),
    path('pets/<int:pk>/excluir/', views.PetDeleteView.as_view(), name='excluipet'),
]