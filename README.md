# CONTRÔLE INTERACTIF ET DYNAMIQUE D'UN CIRCUIT ÉLECTRIQUE PAR LE LANGAGE NATUREL GRÂCE AUX GRANDS MODÈLES DE LANGAGE

Ce dépôt contient le code source et les données expérimentales du projet de recherche "CONTRÔLE INTERACTIF ET DYNAMIQUE D'UN CIRCUIT ÉLECTRIQUE PAR LE LANGAGE NATUREL GRÂCE AUX GRANDS MODÈLES DE LANGAGE".

Le système permet de contrôler un circuit Arduino (LEDs, servomoteur) en donnant des instructions en français. Un Grand Modèle de Langage (LLM) interprète l'instruction, génère le code Python nécessaire, et l'exécute pour piloter le matériel en temps réel.

![Schéma du circuit](hardware/shema_Experimentale_des_circuits.png)

## 🚀 Fonctionnalités

*   **Interface en Langage Naturel** : Contrôlez des composants électroniques avec des phrases simples en français.
*   **Génération de Code Dynamique** : Le LLM génère du code Python à la volée pour exécuter des tâches complexes (boucles, conditions, synchronisation).
*   **Validation Manuelle** : Une étape de sécurité permet de valider le code généré avant son exécution.
*   **Contrôle Arduino** : Communication série avec une carte Arduino UNO via la bibliothèque PySerial.

## ⚙️ Comment ça marche ?

Le processus se déroule en plusieurs étapes :
1.  L'utilisateur lance l'application `main.py` et saisit une instruction (ex: "Fais clignoter la LED 1 cinq fois").
2.  L'application envoie cette instruction, ainsi qu'un prompt système détaillé (contenant le contexte, le code Arduino de base, et des exemples) à un LLM via l'API Hugging Face.
3.  Le LLM renvoie un bloc de code Python conçu pour accomplir la tâche.
4.  L'application affiche le code à l'utilisateur et demande une confirmation.
5.  Si l'utilisateur valide, le code est exécuté. Il envoie des commandes formatées (`device,action,params`) au port série de l'Arduino.
6.  Le code statique sur l'Arduino (`arduino_controller.ino`) lit ces commandes et pilote les composants (LEDs, servomoteur) en conséquence.

## 🛠️ Matériel Requis

*   Carte Arduino UNO R3
*   3x LEDs (couleurs au choix)
*   1x Servomoteur (ex: SG90)
*   3x Résistances (ex: 220Ω)
*   Une breadboard et des câbles de connexion.

Le schéma de câblage est disponible dans le dossier `hardware/`.

## 📦 Installation

1.  **Cloner le dépôt :**
    ```bash
    git clone https://github.com/BKS00/CONTROLE-DYNAMIQUE-DES-CIRCUITS-ELECTRIQUES-GRACE-AUX-LLM-LARGE-LANGUAGE-MODELS-.git
    cd CONTROLE-DYNAMIQUE-DES-CIRCUITS-ELECTRIQUES-GRACE-AUX-LLM-LARGE-LANGUAGE-MODELS-
    ```

2.  **Installer les dépendances Python :**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configurer l'Arduino :**
    *   Ouvrez le fichier `hardware/arduino_controller.ino` avec l'IDE Arduino.
    *   Téléversez le code sur votre carte Arduino UNO.

4.  **Configurer les variables d'environnement :**
    *   Créez un fichier `.env` à la racine du projet.
    *   Ajoutez votre token Hugging Face dans ce fichier :
        ```
        HF_TOKEN="hf_votre_token_secret"
        ```

## ▶️ Utilisation

Lancez l'application principale depuis la racine du projet :
```bash
python src/main.py
```
Suivez les instructions dans le terminal pour donner des ordres à l'Arduino. Tapez `exit` pour quitter.

**⚠️ Avertissement de Sécurité :** Ce projet utilise la fonction `exec()` pour exécuter le code généré par le LLM, ce qui présente un risque de sécurité. Ne validez l'exécution que si vous comprenez parfaitement le code proposé. Ce projet est une preuve de concept et n'est pas destiné à un usage en production sans un environnement d'exécution sécurisé (sandbox).

## 🧪 Le Carnet d'Expérimentation

Le fichier `notebooks/tests_manuels_llms.ipynb` n'est pas une partie de l'application. Il s'agit du journal de bord utilisé pour les tests manuels des 25 instructions de contrôle sur les différents LLM (GPT-4o, Mistral, etc.) dans le cadre du mémoire de recherche.

## 📊 Données et Résultats

Le dossier `data/` contient :
*   `instructions_controle_dynamique.xlsx` : Le jeu de 25+ instructions de test utilisées pour évaluer les modèles.
*   Les résultats qualitatifs et quantitatifs (taux de succès, erreur temporelle) sont détaillés dans le mémoire associé à ce projet. Les expériences montrent une excellente performance de modèles comme GPT-4o mini (100% de succès) et GPT-4o (96% de succès avec la meilleure précision temporelle).

## Auteur

*   **BALEMBA MWAMI Salomon** - [balembasalomon2003@gmail.com]

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.
