from django.urls import path, include
from django.contrib import admin
from .views import index
# ou from .views import index , le point signifiant le dossier en cours 'mercadonaProject'

urlpatterns = [
    # ajout d'un chemin avec un 1er paramètre vide. Donc la page d'accueil de lappli
    # On préfixe index par blog (généralement tout en minuscule) pour ne pas confondre avec l'index du projet mercadonaProject'
    path('', index, name="blog-index"),
    # Puisque les urls django  n'ont qu'une seule entrée et c'est à partir des setting de notre projet donc il faudra  inclure avec include un path pour les urls de notre appli dans  les urls de notre projet'
    path('blog/', include("blog.urls")),
    path('admin/', admin.site.urls),
    # path('Bonjour/', server_error) ligne pour expliquer l'importance du / et la redirection auto gràce à APPEND_SLASH en true
]
