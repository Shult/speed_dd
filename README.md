# README

## Description

Ce script Python appuie automatiquement sur les touches 1 et 2 à intervalles réguliers (toutes les 4 secondes) pour lancer des émotes dans Dofus.
L’objectif est d’enchaîner rapidement les émotes Bisous et Lâcher les gaz lorsqu’elles sont respectivement assignées aux raccourcis 1 et 2.

## Pré-requis

1. Python 3.6+ installé sur votre ordinateur.
2. Le module PyAutoGUI :

```bash
pip install pyautogui
```

3. Un clavier configuré en AZERTY (France) de préférence, pour que les touches correspondent correctement.

## Configuration avant lancement

1. Ouvrir Dofus et se connecter à son personnage.
2. Placer l’émote Bisous sur la touche 1 de la barre de raccourcis (en position 1).
3. Placer l’émote Lâcher les gaz sur la touche 2 de la barre de raccourcis (en position 2).
4. Mettre la fenêtre Dofus au premier plan (activez la fenêtre du jeu).

## Lancement du script

1. Placez-vous dans le dossier où se trouve le script, par exemple :

```bash
cd C:/chemin/vers/le/script
```

2. Exécutez le script Python :

```bash
python nom_du_script.py
```
(ou python3 nom_du_script.py selon votre configuration)

3. Le script va attendre 5 secondes avant de commencer à appuyer sur les touches 1 et 2 en alternance.

- Cela vous laisse le temps de cliquer sur la fenêtre Dofus pour être sûr qu’elle soit bien active.

## Utilisation
- Une fois lancé, le script tapera automatiquement :

    - Touche 1 → Émote « Bisous »
    - Pause de 4 secondes
    - Touche 2 → Émote « Lâcher les gaz »
    - Pause de 4 secondes
    - Et ainsi de suite en boucle…
- Pour arrêter le script, retournez dans la console et appuyez sur Ctrl + C (ou fermez la fenêtre du script).