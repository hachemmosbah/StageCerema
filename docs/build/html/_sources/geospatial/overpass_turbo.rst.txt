Overpass Turbo
==============

Intro
-----

L'API Overpass peut être un excellent outil pour la cartographie, car il est très puissant en filtrant les données OSM. Avec Overpass Turbo, il est facile d'exécuter rapidement des requêtes Overpass et d'inspecter les résultats d'une manière conviviale. Voici quelques exemples où Overpass turbo" peut être un outil cartographique pratique :

Rechercher, sur une grande surface, de (rares) fautes d'orthographe et des erreurs de casse en respectant une convention de nommage.
Rechercher des POI spéciaux qui ne sont pas dessinés sur la carte.
Analyser des POI (par exemple, les nœuds "place") pour vérifier s'ils sont uniformément répartis sur de grandes surfaces.
Afficher spatialement de grandes entités (les frontières, les rivières, les autoroutes complètes, points de connexion, ...) puis les charger directement dans un éditeur.
Filtrer les données OSM que vous souhaitez visualiser.

Pour nous développeurs : 


Tester ou développer des requêtes avec l'API Overpass plus ou moins complexes.
Convertir des données OSM au format geoJSON.
Création de prototype cartographique cliquable ou statique contenant les entités OSM mises en surbrillance.

Extraction de data
------------------

On utilise cette querie pour extraire la position des parkings sur la région paca, on va l'extraire en format geoJSON de sorte à pouvoir en faire un layer dans QGIS pour le sampling d'ortho. 
Voici la querie que nous avons utiliser :

.. code-block:: sql

    [timeout:40000];
    (
     //area(3601403916); // France métropolitaine 1403916
     area(3600008654); // Paca 8654
    )->.zone;

    (
     node[amenity=parking](area.zone);
     (
      way[amenity=parking](area.zone);
      (._;>;);
     );
    );
    out meta;


`Wiki <https://wiki.openstreetmap.org/wiki/FR:Overpass_turbo>`_ | 
`API Explorer <https://overpass-turbo.eu/>`_

.. toctree::
    :maxdepth: 3
