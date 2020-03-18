.. documentation_stage_cerema documentation master file, created by
   sphinx-quickstart on Fri Mar 13 15:42:42 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Bienvenue dans la documentation med-data
========================================

Dans ce repertoire vous pourrez retrouver une documentation détaillé de la stack med-data. Elle est réalisé par les stagières de **Simplon.co** l'ors de leurs formation en la qualité de deveuloppers.se Data dans le cadre de leurs stage en **deeplearning** à la **Cerema**.

L'équipe est composé : Hachem Mosbah, Daniel Kaddous et Joshua Harris.

`Readme <https://github.com/hachem13/StageCerema/blob/master/README.md>`_ | 
`Trello <https://trello.com/b/oE3T8HdO/stage-cerema>`_

Réseau Neuronal
---------------

Un réseau de neurones artificiels, ou réseau neuronal artificiel1, est un système dont la conception est à l'origine schématiquement inspirée du fonctionnement des neurones biologiques, et qui par la suite s'est rapproché des méthodes statistiques3.

Les réseaux de neurones sont généralement optimisés par des méthodes d’apprentissage de type probabiliste, en particulier bayésien. Ils sont placés d’une part dans la famille des applications statistiques, qu’ils enrichissent avec un ensemble de paradigmes4 permettant de créer des classifications rapides (réseaux de Kohonen en particulier), et d’autre part dans la famille des méthodes de l’intelligence artificielle auxquelles ils fournissent un mécanisme perceptif indépendant des idées propres de l'implémenteur, et fournissant des informations d'entrée au raisonnement logique formel (voir Deep Learning).

En modélisation des circuits biologiques, ils permettent de tester quelques hypothèses fonctionnelles issues de la neurophysiologie, ou encore les conséquences de ces hypothèses pour les comparer au réel.


* **Sampling**:
  :doc:`Neat-EO <reseau-neuronal/neat-eo>`

* **Reconnaissance**:
  :doc:`YOLO <reseau-neuronal/yolo>` |
  :doc:`YOLT <reseau-neuronal/yolt>`

* **In progress**:
  :doc:`Senas <reseau-neuronal/senas>`


.. toctree::
   :maxdepth: 3
   :hidden:
   :caption: Réseau neuronal

   reseau-neuronal/neat-eo
   reseau-neuronal/yolo
   reseau-neuronal/yolt	
   reseau-neuronal/senas  

Logiciel Géospatial
-------------------

Un système d'information géographique ou SIG (en anglais, geographic information system ou GIS) est un système d'information conçu pour recueillir, stocker, traiter, analyser, gérer et présenter tous les types de données spatiales et géographiques. L’acronyme SIG est parfois utilisé pour définir les « sciences de l’information géographiques » ou « études sur l’information géospatiales ». Cela se réfère aux carrières ou aux métiers qui impliquent l'usage de systèmes d’information géographique et, dans une plus large mesure, qui concernent les disciplines de la géo-informatique (ou géomatique). Ce que l’on peut observer au-delà du simple concept de SIG a trait aux données de l’infrastructure spatiale.

Dans un sens plus général, le terme de SIG décrit un système d’information qui intègre, stocke, analyse et affiche l’information géographique. Les applications liées aux SIG sont des outils qui permettent aux utilisateurs de créer des requêtes interactives, d’analyser l’information spatiale, de modifier et d’éditer des données par l'entremise de cartes et d’y répondre cartographiquement. La science de l’information géographique est la science qui sous-tend les applications, les concepts et les systèmes géographiques.

Le SIG est un terme général qui se réfère à un certain nombre de technologies, de processus et de méthodes. Celles-ci sont étroitement liées à l’aménagement du territoire, la gestion des infrastructures et réseaux, le transport et la logistique, l’assurance, les télécommunications, l’ingénierie, la planification, l’éducation et la recherche, etc. C’est pour cette raison que les SIG sont à l’origine de nombreux services de géolocalisation basés sur l’analyse des données et leur visualisation.

Les SIG permettent également une mise en relation de données qui peuvent, sur le papier, sembler très éloignées. Quelle que soit la façon d’identifier et de représenter les objets et événements qui illustrent notre environnement (coordonnées, latitude & longitude, adresse, altitude, temps, médias sociaux, etc.), les SIG permettent de réunir toutes ces dimensions autour d’un même référentiel, véritable colonne vertébrale du système d’information.

Cette caractéristique clé du SIG permet d’imaginer de nouvelles applications et de nouveaux débouchés en matière de recherche scientifique.

* **Sampling**:
  :doc:`PostGIS <geospatial/postgis>`

* **Data Mapping**:
  :doc:`QGIS <geospatial/qgis>`
  :doc:`API Overpass Turbo <geospatial/overpass_turbo>` |

* **Database Geographique**:
  :doc:`PostgreSQL <geospatial/postgresql>`


.. toctree::
   :maxdepth: 3
   :hidden:
   :caption: Logiciel Géospatial

   geospatial/postgis
   geospatial/qgis
   geospatial/overpass_turbo
   geospatial/postgresql




