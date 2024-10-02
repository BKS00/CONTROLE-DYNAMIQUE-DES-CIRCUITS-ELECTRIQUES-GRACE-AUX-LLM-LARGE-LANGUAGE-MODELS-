# CONTROLE-DYNAMIQUE-DES-CIRCUITS-ELECTRIQUES-GRACE-AUX-LLM-LARGE-LANGUAGE-MODELS-
# Test des Performances des Modèles LLM sur les Instructions de Contrôle Dynamique des Circuits Électriques

Ce dépôt GitHub contient le code et les données utilisés pour tester les performances de différents Grands Modèles de Langage (LLM) dans le cadre du contrôle dynamique de circuits électriques par le langage naturel.  Ce travail a été réalisé pour le mémoire de recherche intitulé "CONTRÔLE INTER-ACTIF ET DYNAMIQUE D'UN CIRCUIT ÉLECTRIQUE PAR LE LANGAGE NATUREL GRACE AUX GRANDS MODÈLES DE LANGAGE".

## Contexte

Ce projet explore l'utilisation des LLM pour permettre aux utilisateurs de contrôler des circuits électriques à l'aide d'instructions en langage naturel.  L'objectif est de créer une interface intuitive et conviviale pour les ingénieurs et les techniciens, leur permettant de surveiller et de manipuler des dispositifs électromécaniques et électriques tels que des machines, des robots, des capteurs, des LEDs et des systèmes embarqués.

## Méthodologie

Le système de contrôle utilise un kit Arduino UNO R3 pour piloter les composants électriques.  Une interface interactive a été développée en Python pour permettre la communication entre l'utilisateur, le LLM et l'Arduino.  Différents LLM, tels que GPT-4o, GPT-4o mini, Mistral Large, Mistral 8X7B, Mistral 7B, Mistral Nemo, Codestral et Gemma 2 9B, ont été évalués.

Le processus de contrôle se déroule comme suit :

1. L'utilisateur fournit une instruction en langage naturel.
2. Le LLM génère du code Python correspondant à l'instruction.
3. Le code Python est exécuté et envoie des commandes à l'Arduino via le port série USB (grâce à la bibliothèque PySerial).
4. L'Arduino exécute les commandes et renvoie un feedback au LLM.

## Contenu du dépôt

* **`data/`**: Contient le jeu de données des instructions en langage naturel utilisées pour les tests, ainsi que les résultats obtenus pour chaque LLM.  Vous trouverez notamment :
    * `instructions.csv`:  Le jeu de données des 25 instructions de contrôle dynamique.
    * `resultats_gpt4o.csv`, `resultats_mistral.csv`, etc. :  Les résultats des tests pour chaque LLM, incluant le taux de succès, l'erreur temporelle, et le coût d'inférence.
* **`arduino/`**: Contient le code Arduino utilisé pour contrôler les composants du circuit.
* **`python/`**: Contient le code Python de l'interface interactive, incluant la communication avec les LLM et l'Arduino.  Vous trouverez des scripts séparés pour chaque LLM testé, par exemple :
    * `controle_gpt4o.py`
    * `controle_mistral.py`
    * `controle_codestral.py`
* **`schema_circuit.fzz`**:  Schéma Fritzing du circuit électrique utilisé pour les expériences.


## Installation

1. Clonez ce dépôt : `git clone https://github.com/BKS00/CONTROLE-DYNAMIQUE-DES-CIRCUITS-ELECTRIQUES-GRACE-AUX-LLM-LARGE-LANGUAGE-MODELS-.git`
2. Installez les dépendances Python : `pip install -r requirements.txt`
3. Installez l'IDE Arduino et configurez-le pour votre carte Arduino UNO R3.
4. Configurez l'accès aux API des LLM (si nécessaire) en suivant les instructions spécifiques à chaque modèle.

## Exécution des tests

1. Téléchargez le code Arduino sur votre carte Arduino UNO.
2. Exécutez le script Python correspondant au LLM que vous souhaitez tester, par exemple : `python python/controle_gpt4o.py`
3. Suivez les instructions affichées dans le terminal pour interagir avec le système.

## Résultats

Les résultats des tests sont disponibles dans le dossier `data/`.  Vous pouvez les analyser pour comparer les performances des différents LLM.  Le mémoire de recherche fournit une analyse détaillée de ces résultats.


## Licence

Ce code est mis à disposition sous la licence [MIT](LICENSE).

## Contact

Pour toute question, veuillez contacter [balembasalomon2003@gmail.com].


## Remerciements

Remerciements aux développeurs des différents LLM utilisés dans ce projet, ainsi qu'à la communauté open-source pour les bibliothèques et outils mis à disposition.
