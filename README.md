#  CréditScore AI — Prédiction d'Accord de Prêt Bancaire

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red?style=flat-square&logo=streamlit)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.4-orange?style=flat-square&logo=scikit-learn)
![Status](https://img.shields.io/badge/Status-Deployed-brightgreen?style=flat-square)

> Application de Machine Learning permettant de prédire l'accord ou le refus d'un prêt bancaire à partir du profil financier et personnel d'un demandeur.

---

##  Objectif

Ce projet a été réalisé dans le cadre de la formation **Data Scientist** chez **GoMyCode Côte d'Ivoire**.  
Il couvre l'ensemble du cycle de vie d'un modèle ML : exploration des données, nettoyage, entraînement, évaluation et déploiement.

---

##  Démonstration

 **[Accéder à l'application]([(https://creditscoreai.streamlit.app/))]**




## Structure du projet

creditscore-ai/
│
├── app.py                  # Application Streamlit (interface utilisateur)
├── model.pkl               # Modèle Random Forest entraîné
├── scaler.pkl              # StandardScaler ajusté sur les données d'entraînement
├── requirements.txt        # Dépendances Python
├── Prédiction_de_crédit.py # Notebook complet : EDA + entraînement + évaluation
└── README.md               # Documentation du projet
```

---

##  Modèle Machine Learning

### Algorithme
**Random Forest Classifier** — choisi pour sa robustesse sur les données tabulaires bancaires et sa résistance naturelle aux valeurs aberrantes.

### Pipeline complet

```
Données brutes
    │
    ├── Nettoyage
    │     ├── Valeurs manquantes catégorielles → Mode
    │     ├── Valeurs manquantes numériques   → Médiane
    │     └── Valeurs aberrantes              → Winsorisation (1% – 99%)
    │
    ├── Feature Engineering
    │     └── Total_Income = ApplicantIncome + CoapplicantIncome
    │
    ├── Encodage & Normalisation
    │     ├── LabelEncoder  (variables catégorielles)
    │     └── StandardScaler (variables numériques)
    │
    ├── Rééquilibrage des classes
    │     └── SMOTE — génération synthétique de la classe minoritaire (Refusé)
    │
    └── Entraînement
          ├── RandomForestClassifier(class_weight='balanced')
          └── Seuil de décision ajusté à 0.30 (contexte bancaire)
```

### Performances du modèle

| Métrique | Refusé (0) | Accordé (1) |
|---|---|---|
| Precision | 95% | 82% |
| Recall | 53% | 99% |
| F1-Score | 68% | 90% |
| **Accuracy globale** | | **84.55%** |

> **Note :** Le recall de la classe minoritaire (Refusé) est limité par la taille réduite du dataset (38 cas refusés vs 85 accordés). Sur un dataset de production plus large, SMOTE et `class_weight='balanced'` produiraient des gains significatifs.

---

##  Technologies utilisées

| Outil | Usage |
|---|---|
| `pandas` / `numpy` | Manipulation et analyse des données |
| `scikit-learn` | Modélisation ML, encodage, normalisation |
| `imbalanced-learn` | SMOTE pour le rééquilibrage des classes |
| `ydata-profiling` | Rapport automatique d'exploration des données |
| `matplotlib` / `seaborn` | Visualisations EDA |
| `streamlit` | Interface web de déploiement |
| `joblib` | Sérialisation du modèle |

---

##  Installation locale

```bash
# 1. Cloner le dépôt
git clone https://github.com/votre-username/creditscore-ai.git
cd creditscore-ai

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer l'application
streamlit run app.py
```

---

##  Variables utilisées par le modèle

| Variable | Description |
|---|---|
| `Gender` | Genre du demandeur |
| `Married` | Situation matrimoniale |
| `Dependents` | Nombre de personnes à charge |
| `Education` | Niveau d'études |
| `Self_Employed` | Statut d'emploi |
| `LoanAmount` | Montant du prêt demandé |
| `Loan_Amount_Term` | Durée de remboursement (mois) |
| `Credit_History` | Historique de crédit (0 = mauvais, 1 = bon) |
| `Property_Area` | Zone d'habitation (Urban / Semiurban / Rural) |
| `Total_Income` | Revenu total du foyer (demandeur + co-demandeur) |

---

##  Auteur

**N'Gbla Eric Lionel Kouakou**  
Process Owner & Data Scientist en formation  
📍 Abidjan, Côte d'Ivoire

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connexion-0077B5?style=flat-square&logo=linkedin)](https://linkedin.com/in/votre-profil)
[![GitHub](https://img.shields.io/badge/GitHub-Portfolio-181717?style=flat-square&logo=github)](https://github.com/votre-username)

---

## Licence

Ce projet est réalisé à des fins éducatives dans le cadre de la formation GoMyCode.  
Données issues de [Kaggle — Loan Prediction Dataset](https://www.kaggle.com/).
