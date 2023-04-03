**Projet Flask et Google Sheets** 


Ce projet est une application Flask qui récupère des données à partir de l'API OMDB et les stocke dans un Google Spreadsheet.
L'application dispose de deux endpoints : /films pour récupérer les films Fast & Furious au format JSON
et /stock-film pour stocker les films Pirates des caraïbes dans une feuille de calcul Google Sheets.

**Comment il est construit ?** 


L'application est écrite en Python et utilise Flask pour la gestion des routes HTTP.
Les données sont récupérées à partir de l'API OMDB à l'aide de la bibliothèque requests.
Pour la communication avec Google Sheets, l'application utilise la bibliothèque gspread qui permet d'interagir avec les API Google.

**Comment faire fonctionner le projet ?**
Cloner le repository GitHub sur votre ordinateur.

Installer les dépendances requises à l'aide de la commande suivante :

```bash
pip install -r requirements.txt
```

Créer un fichier credentials.json qui contient les informations d'authentification pour l'API Google Sheets.
Pour plus d'informations sur la création de ce fichier, consultez la documentation de gspread.

Exécuter l'application à l'aide de la commande suivante :

```bash
python app.py
```

L'application est maintenant accessible à l'adresse http://localhost:5000.

**Comment tu envisages la partie hébergement ?**
L'application peut être hébergée sur une plateforme de cloud computing comme Heroku ou Google Cloud Platform. Pour stocker les données, il est recommandé d'utiliser une base de données comme MySQL ou PostgreSQL.

**Comment tu vois une éventuelle montée en charge du système ?**
Pour une montée en charge du système, il est possible d'utiliser un service de mise en cache comme Redis pour améliorer les performances de l'application.


**Forces**
L'application est facile à utiliser et à déployer.
Les données sont stockées de manière sécurisée dans un Google Spreadsheet.
La mise en cache des données permet d'améliorer les performances de l'application.

**Faiblesses**
La sécurité de l'application est limitée à une simple authentification de base.
L'application peut être ralentie en cas de forte demande.

**NEXT STEPS pour la mise en prod**
Ajouter une authentification plus robuste à l'application.
Ajouter des tests unitaires pour garantir la qualité du code.
Utiliser une base de données pour stocker les données à long terme.
