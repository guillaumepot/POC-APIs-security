#src/routes/vuln1.py


# Lib
from fastapi import APIRouter



"""
Router Declaration
"""
vulnerability1 = APIRouter()



"""
Routes Declaration
"""

# Route that raises an exception

@vulnerability1.get('/user/{id:int}', tags=["Vuln I"])
def get_user_information(id:int):
    return {"Done:", id}


# - Route permettant d'accéder à des infos utilisateurs
#     - /user/info/<int:id>

# La route retourne des informations sur l'utilisateur en fonction de l'ID. Si l'ID n'existe pas, la route retourne une erreur 404.


# Mitigation:
#     - Utiliser un système d'authentification avec un access token (JWT) pour certaines routes (avec un /toekn pour obtenir un token par exemple)
#     - utiliser un système de roles pour les utilisateurs