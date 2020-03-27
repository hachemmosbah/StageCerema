QGIS
====

Intro
-----

QGIS est un logiciel SIG libre multiplate-forme publié sous licence GPL. Le développement a débuté en mai 2002 et est sorti en tant que projet sur SourceForge en juin 2002. Il était également appelé Quantum GIS jusqu'en septembre 2013.

Echantillionnage d'élement non parkings
---------------------------------------

Vérification des données parkings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Je vois l'aire maximale des parkings sur Bouches du Rhône

Vue > Statistiques

	$area :
	
	Statistique	Valeur
	Moyenne	1493.8
	Médiane	639.879
	Minimum	7.15668
	Maximum	86399.6
	Plage	86392.5
	Minorité	7.15668
	Majorité	2583.67
	Variété	5877
	Q1	270.35
	Q3	1509.46
	IQR	1239.11
	Valeurs (null) manquantes	0

Liste des classes
~~~~~~~~~~~~~~~~~

	Vecteur > Outils d'analyse > Lister les valeurs uniques


Sélection des objets à échantillonner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Traitement > Extraire par expression

.. code-block:: bash

	"LIB4_17" NOT ILIKE '%parking%'
	and "LIB4_17" NOT IN (
	'Cours et voies d?eau', 
	'Ripisylves',
	'Réseau routier et bâtis techniques associés', 
	'Réseau ferroviaire et bâtis techniques associés', 
	'Chemins, Digues et Interstices agricoles', 
	'Canal',
	'Espaces associés aux réseaux routier et/ou ferroviaire')
	and $area <= 83000

Echantillonnage stratifié
~~~~~~~~~~~~~~~~~~~~~~~~~

	Traitement > Extraire aléatoirement parmi des sous ensembles > choisir colonne LIB4_17

Vérification du nb d'objets dans chaque classe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	Vecteur > Group Stats 

pour avoir le nb d'éléments par classes

Sauvegarde de la couche
~~~~~~~~~~~~~~~~~~~~~~~

	Couche > Exporter sous > Sauvegarder les entités sous > GeoPackage ou GeoJSON (pour Daniel)

Réglages pour atlas
~~~~~~~~~~~~~~~~~~~

Je coche seulement ortho

Je crée un réglage/thème pour mémoriser ortho cochée

Je fais l'atlas sur ces objets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Echantillionnage d'éléments parkings
------------------------------------

Ouvrir couche communes et la filtrer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	Couche > Filtrer

.. code-block:: bash
	
	CODE_DEPT = '13'

Extraire par localisation
~~~~~~~~~~~~~~~~~~~~~~~~~

	Traitement > Extraire par localisation

Choisir les objets parkings qui intersectent les communes du 13

Echantillonnage
~~~~~~~~~~~~~~~

	Traitement > Extraire aléatoirement

Choisir 4000 objets parkings au hasard pour l'atlas Parking

Atlas
~~~~~

Atlas parking

`Wiki <https://fr.wikipedia.org/wiki/QGIS>`_ | 
`Documentation <https://docs.qgis.org/3.10/fr/docs/user_manual/>`_ | 
`Website <https://www.qgis.org/fr/docs/index.html>`_


.. toctree::
    :maxdepth: 3