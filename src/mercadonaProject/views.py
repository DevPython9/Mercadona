# from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
# def index(request):
#     return HttpResponse("<h1>Bienvenue sur Mercado Store </h1>")

# def index(request):
#     return render(request, "index.html")

# Insérer des données dans notres templates via des variables
def index(request):
    date = datetime.today()
    # Pour éviter le conflit de template index.html de blog et mercadona, on a créé un sous dossier des deux dossiers précités avec comme nom de dossier pareil à leurs parents à eux mêmes (mercadonaProject et blog
    return render(request, "mercadonaProject/index.html", context={"prenom":"Patrick","date_du_Jour": date})
# On pouvait insérer directement datetime.today() dans le context sans créer de variable date.
