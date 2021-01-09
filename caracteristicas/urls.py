from django.urls import path
from .views import *
#from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from rest_framework_jwt.views import RefreshJSONWebToken,ObtainJSONWebToken

urlpatterns = [
    path('sendEmail/', sendEmail),
    path('login/', LoginUser.as_view()),
    path(r'auth/refresh/', obtain_jwt_token),

    path('profile/',ProfielView.as_view()),
    path('ingresar/', llenar_base),
    path('observaciones/', getObservaciones),
    path('misobs/', getObservacionesUser),
    path('provincias/', get_provincias),
    path('cantones/', get_cantones),
    path('parroquias/', get_parroquias),
    path('postObservaciones/', postObservaciones),

    path('crear_usuario/', postCreateUser),
    path('get_usuario/', get_usuario),
    path('put_usuario/<str:username>', put_usuario2),
    path('putUser/', put_usuario),##Post que se lo utiliza como put ojo
    path('borrar_observacion/<str:username>', borrar_observacion),





    path('crear_estacion/', crear_estacion),
    path('estacion/', get_estacion),
    path('borrar_estacion/<int:idEstacion>', borrar_estacion),
    path('actualizar_estacion/<int:idEstacion>', actualizar_estacion),

    path('crear_provincia/', crear_provinvia),
    path('actua_provincia/', update_provinvia),
    path('borrar_provincia/', delete_provincia),
    path('crear_canton/', crear_canton),
    path('actua_canton/', update_canton),
    path('borrar_canton/', delete_canton),
    path('crear_parroquia/', crear_parroquia),
    path('actua_parroquia/', update_parroquia),
    path('borrar_parroquia/', delete_parroquia),
]