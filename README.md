# TD Crack AES

## Démarrer

Depuis la racine du dépôt (les chemins `data/...` sont relatifs à elle) :

```
python3 -m venv env
source env/bin/activate        # Windows : env\Scripts\activate
pip install -r requirements.txt
python src/DPA_AES.py
```

Au premier lancement, le script s'arrête sur le premier `assert` : c'est normal, c'est à vous de compléter les fonctions.

## À faire

- Compléter le fichier python en suivant les instructions
- Écrire un rapport contenant :
    - un compte rendu du travail réalisé
        - résultat
        - combien de traces sont nécessaires pour retrouver la clé complète (figure : nombre d'octets justes en fonction du nombre de traces)
        - comment améliorer les résultats ?
    - les réponses aux questions posées dans le .py
    - plots & screenshots de vos résultats

Code python dans un .zip + rapport à remettre par mail
