# DA_Python_P10 - Créez une API sécurisée RESTful en utilisant Django REST

Créez une API sécurisée RESTful en utilisant Django REST

# Table des matières<a name="Table_of_Contents"></a>
- [DA_Python_P10 - Créez une API sécurisée RESTful en utilisant Django REST](#da_python_p10---créez-une-api-sécurisée-restful-en-utilisant-django-rest)
- [Table des matières<a name="Table_of_Contents"></a>](#table-des-matières)
  - [INTRODUCTION <a name="INTRODUCTION"></a>](#introduction-)
  - [Objectifs du projet <a name="objectifs"></a>](#objectifs-du-projet-)
  - [FEATURES <a name="FEATURES"></a>](#features-)
  - [REQUIREMENTS <a name="REQUIREMENTS"></a>](#requirements-)
    - [Récupération du projet <a name="Recup_projet"></a>](#récupération-du-projet-)
    - [Création d'un environnement virtuel Python <a name="Env_Virtuel_Python"></a>](#création-dun-environnement-virtuel-python-)
    - [Installation des packages Python nécessaire <a name="Installation_package"></a>](#installation-des-packages-python-nécessaire-)
  - [Création de la base de données <a name="create_db"></a>](#création-de-la-base-de-données-)
  - [Lancement du serveur web  <a name="Validateur_HTML_no_charged"></a>](#lancement-du-serveur-web--)
  - [Documentation de l'API <a name="doc_api"></a>](#documentation-de-lapi-)


## INTRODUCTION <a name="INTRODUCTION"></a>

SoftDesk, une société d'édition de logiciels de développement et de collaboration, a décidé de publier une application permettant de remonter et suivre des problèmes techniques (issue tracking system). Cette solution s’adresse à des entreprises clientes, en B2B.


## Objectifs du projet <a name="objectifs"></a>

L'objectif est créer un back-end performant et sécurisé, devant servir les applications sur toutes les plateformes. 

Présentation de cette application : 

- Une application de suivi des problèmes pour les trois plateformes (site web, applications Android et iOS).
- L'application permettra essentiellement aux utilisateurs de créer divers projets, d'ajouter des utilisateurs à des projets spécifiques, de créer des problèmes au sein des projets et d'attribuer des libellés à ces problèmes en fonction de leurs priorités, de balises, etc.
- Les trois applications exploiteront les points de terminaison d'API qui serviront les données.


[<div align="center">[Table of Contents]</div>](#Table_of_Contents) 

## FEATURES <a name="FEATURES"></a>

- Authentification des utilisateurs
- Concernant les objets de type projet, les utilisateurs ont accè aux actions basiques de type CRUD sur des projets.
- Chaque projet peut se voir associer des problèmes qui lui sont liés; l'utilisateur ne peut pas appliquer le processus CRUD aux problèmes du projet que si il ou elle figure sur la liste des contributeurs.
- Chaque problème a un titre, une description, un assigné (l’assigné par défaut étant l'auteur lui-même), une priorité (FAIBLE, MOYENNE ou ÉLEVÉE), une balise (BUG, AMÉLIORATION ou TÂCHE), un statut (À faire, En cours ou Terminé), le project_id auquel il est lié et un created_time (horodatage), ainsi que d'autres attributs mentionnés dans le diagramme de classe.
- Les problèmes peuvent faire l'objet de commentaires de la part des contributeurs au projet auquel ces problèmes appartiennent. Chaque commentaire doit être assorti d'une description, d'un author_user_id, d'un issue_id, et d'un comment_id.
- Il est interdit à tout utilisateur autorisé autre que l'auteur d'émettre des requêtes d'actualisation et de suppression d'un problème/projet/commentaire.


[<div align="center">[Table of Contents]</div>](#Table_of_Contents)

## REQUIREMENTS <a name="REQUIREMENTS"></a>
  - Une version de Python doit être installée sur votre poste, au moins la version 3.8.8 est conseillée. 
  - Voici un wiki pour installer Python selon votre système d'exploitation : https://fr.wikihow.com/installer-Python

  - Il est recommander de récupérer le projet en utilisant "git clone" ou en téléchargeant directement le projet.
  - Une connexion internet fonctionnelle est nécessaire pour la partie installation.

** Dans cette documention, nous donnons les commandes pour un système d'exploitation Linux (fonctionne aussi pour Mac). Si vous êtes sous Windows, il faut adapter les commandes à votre OS.


### Récupération du projet <a name="Recup_projet"></a>

  
```ssh
git clone https://github.com/chrisopenclass/SoftDeskApi.git
```


[<div align="center">[Table of Contents]</div>](#Table_of_Contents) 



### Création d'un environnement virtuel Python <a name="Env_Virtuel_Python"></a>

Se positionner dans le dossier de votre choix et qui hébergera le projet Django.

Si le module python "venv" n'est pas installé sur votre système, il est nécessaire de l'installer comme ci-dessous :

  - Installation du module "venv"

```ssh

$ pip install venv

```

  - Création de l'environnement virtuel Python

```ssh

$ cd SoftDeskApi
$ python3 -m venv .venv

```

  - Activation de l'environnement virtuel Python

```ssh

$ source ./.venv/bin/activate

```

[<div align="center">[Table of Contents]</div>](#Table_of_Contents) 

### Installation des packages Python nécessaire <a name="Installation_package"></a>

l'installation de ces packages sont nécessaire pour la bonne éxécution du script.

- Django==4.0.4
- djangorestframework==3.13.1
- djangorestframework-simplejwt==5.1.0
- requests==2.27.1

    - Installation automatique des packages ( se positionner dans le dossier du projet)

```ssh

$ pip install -r requirements.txt

```


[<div align="center">[Table of Contents]</div>](#Table_of_Contents) 

## Création de la base de données <a name="create_db"></a>

Se positionner dans le dossier de l'application récupérée sur Gihub .

```ssh

$ cd project
$ python manage.py migrate

```

Se positionner dans le dossier de l'application récupérée sur Gihub .

```ssh

$ cd project
$ python manage.py createsuperuser

Nom d’utilisateur (leave blank to use 'example'): admin
Adresse électronique: example@django.fr
Password: 
Password (again): 
Superuser created successfully.

```

[<div align="center">[Table of Contents]</div>](#Table_of_Contents)


## Lancement du serveur web  <a name="Validateur_HTML_no_charged"></a>

Lançons le serveur de développement, démarrez-le comme ceci :

Se positionner dans le dossier de l'application récupérée sur Gihub .

```ssh

$ cd project
$ python manage.py runserver

```

Exemple de sortie:

```ssh
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 28, 2022 - 23:19:44
Django version 4.0.4, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

[<div align="center">[Table of Contents]</div>](#Table_of_Contents)

## Documentation de l'API <a name="doc_api"></a>

Pour utiliser l'API, vous pouvez consulter la documentation de cette dernière sur l'URL suivant:

- https://documenter.getpostman.com/view/19321113/VUjLM7Td


[<div align="center">[Table of Contents]</div>](#Table_of_Contents)

## Arborescence du projet <a name="Tree_project"></a>

Voici l'arborescence du projet.
