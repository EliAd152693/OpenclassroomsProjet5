README
PROJET 5 

Fonctionnement de l'API

Le modèle développé pour le projet 5 est exploitable via une API déployée sur Heroku.

Deux façons d'utiliser l'API 
1 - Via une interface web disponible à l'adresse :
http://127.0.0.1:5000/

2 - l'API est également disponible via le point d'entrée suivant :
http://127.0.0.1:5000/api/

	Pour utiliser l'API, la requête se fait en Python.
	Il est nécessaire d'importer les librairies json et requests.

	Code Python :

	A adapter : data => string qui servira d'input pour la prédiction par le modèle


	import json, requests
	j_data=json.dumps(data)
	headers= {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
	r = requests.post('http://127.0.0.1:5000/api/', data=j_data, headers=headers)
	print(r.text)