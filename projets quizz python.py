"""c'est un quiz capital du monde 
  Comment pouvez-vous stocker les pays et les capitales dans un dictionnaire?
  Comment pouvez-vous obtenir un pays aléatoire à partir du dictionnaire?
  Comment pouvez-vous demander à l'utilisateur de deviner la capitale d'un pays donné?
  Comment pouvez-vous vérifier si la réponse de l'utilisateur est correcte ou non?
  Comment pouvez-vous mettre à jour le score de l'utilisateur en fonction de sa réponse ?
"""
"""
  1 étape c'est la question
  2 étape c'est de récuprer la réponse
  3 étape vérifier si la réponse est vrai ou fausse
  4 étape faire un score
"""
"""
  bonus
  1) plus de pays dans le dictionnaire
  2) random.randint(0, len())
  3) message avec print différent
  4) l'orthographe et cordination avec le masculin (du maroc et pas de maroc)
  5) creer un deuxieme dict avec les capitales comme clés et leur histoire et monuments etc
  6) montrer la documentation avec le readme
  
"""
import random


def quiz():
  pays = {
    'la france': 'paris',
    "l'espagne": 'madrid',
    "l'angleterre": 'londre',
    'du maroc': 'rabat',
    'la hongrie': 'budapest',
    'de la russie' : 'moscou',
    'des etats unies' : 'washington',
    'du japon' : 'tokyo',
    "de l'allemagne" : 'berlin'
  }

  monuments = {
    'paris' : 'tour effeil',
    'madrid' : 'le palais royal',
    "londre" : 'big ben',
    'rabat' : 'tour hassan',
    'budapest' : 'hosok tere',
    'moscou' : 'place rouge',
    'washington' : 'maison blanche',
    'tokyo' : 'Meiji-jingu',
    'berlin' : 'porte de Brandebourg',
    
  }
  

  score = 0
  while True:
    liste_pays = list(pays.keys())
    indice_random_pays = random.randint(0, len(liste_pays)-1)
    print("Quelle est la capitale de", liste_pays[indice_random_pays], ":")
    reponse_pays = input()
    if reponse_pays == pays[liste_pays[indice_random_pays]]:
      print("C'est bon")
      score += 1
      print("voici le monument le plus connu :",monuments[pays[liste_pays[indice_random_pays]]])  
    else:
      print("C'est faux")
    print("Voulez-vous arrêter?")
    
    reponse = input()
    if reponse == "oui":
      print('Votre score est:', score)
      break
quiz()