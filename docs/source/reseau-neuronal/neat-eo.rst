Neat-EO
=======

Installation 
------------

L'installation de neat-eo est très simple et c'est passé sans acoup avec  

.. code-block:: bash

    pip3 install https://neat-eo.pink/latest

Il faut quand même faire attention que CUDA et le Driver Nvidia soi bien installé sinon une erreur vous disant que vous n'avez aucun GPU surviendrait durant l'entrainement.



Préparation  
-------------

IL y'a deux façon de preparer votre dataset : 

1. Soit par téléchargement grâce "neo download" et un serveur Web en WMS ou XYZ, pour télécharger directement les tiles mais attention il vous faudra un fichier cover  .tiles ou un .csv.  (Cette façon est en progression...)

2. Soit vous avez déjà une Ortophoto que vous avez déjà en votre possesion et que vous découperez en utilisant "neo tile". Mais attention il vous faudra le geojson correspondant à l'image.

Il vous faudra donc une Ortophoto (ou des tiles suivant la méthode que vous allez pouvoir découper en tiles grâce a NEAT, un geojson contenant les "Labels" qui vous intéressent (Building , Parking etc...)

Ainsi qu'un .csv qui regroupera les infos permettant au tiles d'avoir un ordre et de pouvoir s'assembler correctement ,  mais ce dernier peut être générer avec NEAT.


`Ici le config.toml <https://github.com/hachem13/StageCerema/blob/master/docs/source/external-files/config_neat.toml>`_ qui est le file config de neat-eo pour votre entrainement d'entrainement, on peux y regler de nombreux paramètre comme la couleur , le nom des labels... 

N'oubliez pas d'utiliser :

.. code-block:: bash
    
    export NEO_CONFIG=config_neat.toml

Pour utiliser votre fichier en Config.


J'ai eu un problème lors de l'entrainement , je n'avais pas assez de mémoire GPU , car j'ai 6 GO et 8go sont recomandé , pour résoudre mon problème j'ai reglé le "bs" (batch size) du config file sur 3 au lieu de 4, et l'entraînement à pu être éffectuer.

Utilisation 
-------------

Je précise bien que neo s'utilise avec le terminal 

La première methode avec neo download est encore en phase test je ne peux donc pas compléter cette partie.


La deuxième méthode avec une ortophoto déjà présente commence par le neo tile

.. code-block:: bash

    neo tile --zoom 19 --bands 1,2,3 --nodata_threshold 25 --rasters [CHEMIN VERS VOTRE IMAGE] --out [CHEMIN DE SORTIE]

Après ça vous génererez le fichier cover :

.. code-block:: bash

    neo cover --dir [CHEMIN DE VOS IMAGE] --out [CHEMIN DE SORTIE ET EXTENSIONS SOUHAITEZ]

Ensuite vous "pixeliserais" le geojson en utilisant votre fichier cover :

.. code-block:: bash

    neo rasterize --geojson [CHEMIN VERS VOTRE GEOJSON] --type [FEATURES SOUHAITEZ (ex. Parking, Building..)] --cover [CHEMIN VERS VOTRE COVER] --out [CHEMIN DE SORTIE]

Quand ces étapes sont faites on va pouvoir entrainer le model :

.. code-block:: bash

    neo train --dataset [CHEMIN VERS VOTRE DATASET D'ENTRAINEMENT] --epochs [Nombre d'epoch à Entrainer] --out [CHEMIN DE SORTIE]

    neo eval --checkpoint [CHEMIN VERS VOTRE DERNIER CHECKPOINT] --dataset train

    neo eval lance une evaluation à partir du checkpoint souhaitez

Après avoir entrainer votre model on va découpez l'image de prédiction avec neo tiles et les même paramètre que utiliser au début.

Après ça on lance la prédiction : 

.. code-block:: bash

    neo predict --checkpoint model/checkpoint-00005.pth --dataset predict --metatiles --out predict/masks

La prédiction terminé on réutilise neo cover et neo rasterize sur la prediction :

.. code-block:: bash

    neo cover --dir predict/masks --out predict/cover.csv
    neo rasterize --geojson predict/*/*-labels/*.geojson --type Building --cover predict/cover.csv --out predict/labels

On fait les comparaisons 

.. code-block:: bash

    neo compare --mode stack --images predict/images predict/labels predict/masks --cover predict/cover.csv --out predict/compare

    neo compare --mode list --labels predict/labels --masks predict/masks --max Building QoD 0.80 --cover predict/cover.csv --geojson --out predict/compare/tiles.json

    neo compare --mode side --images predict/images predict/compare --cover predict/cover.csv --out predict/compare_side

Et finalement on vectorize les résultats

.. code-block:: bash

    neo vectorize --masks predict/masks --type Building --out predict/building.json

Vous pourrez retrouver un entrainement très sympas sur le repo de NEAT-EO

Les outils 
------------

Pour plus de précisions sur les outils rendez vous sur la Doc `tools <https://datapink.io/datapink/neat-EO/src/branch/master/docs/tools.md>`_  de NEAT-EO

`Source <https://datapink.io/datapink/neat-EO/src/branch/master/README.md>`_


.. toctree::
    :maxdepth: 3