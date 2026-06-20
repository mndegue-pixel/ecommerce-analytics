Super ! On va mettre à jour le README ensemble. Voici la version finale complète et professionnelle :

---

## 📝 README.md (Version finale)

**Copie-colle ce contenu** dans ton fichier `README.md` :

```markdown
# 🛒 E-Commerce Analytics Pipeline

[![CI/CD Pipeline](https://github.com/mndegue-pixel/ecommerce-analytics/actions/workflows/ci-cd.yml/badge.svg?branch=master)](https://github.com/mndegue-pixel/ecommerce-analytics/actions/workflows/ci-cd.yml)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/)
[![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=flat&logo=databricks&logoColor=white)](https://databricks.com/)

## 📋 Description

Ce projet met en place un pipeline de données complet sur **Azure Databricks** avec l'architecture médaillon (Bronze/Silver/Gold). Il inclut :

- ✅ Pipeline ETL avec **PySpark** et **Delta Lake**
- ✅ Modèle de prédiction de **churn** avec **MLflow**
- ✅ Dashboard **Power BI** interactif
- ✅ CI/CD avec **GitHub Actions**

---

## 🏗️ Architecture du projet

### Architecture Médaillon

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         ARCHITECTURE MÉDAILLON                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   🥉 Bronze (Raw Data)    🥈 Silver (Cleaned)    🥇 Gold (Aggregated)  │
│                                                                         │
│   ┌─────────────────┐     ┌──────────────────┐    ┌──────────────────┐  │
│   │  customers      │     │  customers_clean │    │  monthly_sales   │  │
│   │  products       │ ──▶ │  products_clean  │ ──▶│  top_products    │  │
│   │  transactions   │     │  transactions_   │    │  customer_seg    │  │
│   └─────────────────┘     │  clean           │    │  churn_predict   │  │
│                           │  transactions_   │    └──────────────────┘  │
│                           │  enriched        │                         │
│                           └──────────────────┘                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Flux des données

1. **Bronze** : Ingestion des données brutes (CSV → Delta Lake)
2. **Silver** : Nettoyage, transformation et enrichissement
3. **Gold** : Agrégations, KPIs et données prêtes pour la BI

---

## 🛠️ Technologies utilisées

| Technologie | Utilisation |
|-------------|-------------|
| **Azure Databricks** | Plateforme de traitement des données |
| **PySpark** | Transformations de données distribuées |
| **Delta Lake** | Stockage ACID avec time travel |
| **MLflow** | Tracking des modèles ML |
| **Power BI** | Visualisation des données |
| **GitHub Actions** | CI/CD Pipeline |
| **Python 3.9** | Langage principal |

---

## 📁 Structure du projet

```
ecommerce-analytics/
├── .github/
│   └── workflows/
│       └── ci-cd.yml              # Pipeline CI/CD GitHub Actions
├── notebooks/
│   ├── 01_generate_data.py        # Génération des données de test
│   ├── 02_silver_cleaning.py      # Nettoyage (couche Silver)
│   ├── 03_gold_aggregations.py    # Agrégations (couche Gold)
│   ├── 04_mlflow_churn_model.py   # Modèle ML avec MLflow
│   └── 05_export_powerbi.py       # Export pour Power BI
├── tests/
│   ├── test_cleaning.py           # Tests unitaires - Nettoyage
│   └── test_aggregations.py       # Tests unitaires - Agrégations
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🚀 Installation et exécution

### 1. Cloner le dépôt

```bash
git clone https://github.com/mndegue-pixel/ecommerce-analytics.git
cd ecommerce-analytics
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Configurer Databricks

1. Créer un workspace Azure Databricks
2. Générer un token d'accès
3. Configurer les variables d'environnement :
   ```bash
   export DATABRICKS_HOST="https://adb-xxxxx.azuredatabricks.net"
   export DATABRICKS_TOKEN="dapi-xxxxx"
   ```

### 4. Exécuter les notebooks

Dans Databricks, exécute les notebooks dans l'ordre :

1. `01_generate_data.py` - Génération des données
2. `02_silver_cleaning.py` - Nettoyage
3. `03_gold_aggregations.py` - Agrégations
4. `04_mlflow_churn_model.py` - Modèle ML
5. `05_export_powerbi.py` - Export Power BI

---

## 📊 Dashboard Power BI

Le dashboard Power BI présente :

### KPIs principaux
- **CA Total** : 295,5 M€
- **Transactions** : 5 000
- **Panier Moyen** : 240,50 €
- **Taux de Churn** : 37,42%

### Visualisations
- 📈 Évolution du CA par mois
- 🏆 Top 10 produits
- 📂 Performance par catégorie
- 👥 Segmentation clients (High/Medium/Low Spenders)
- ⚠️ Clients à risque de churn (>70%)

---

## 🤖 Modèle de Prédiction de Churn

### Résultats du modèle

| Métrique | Score |
|----------|-------|
| **Accuracy** | 71,3% |
| **ROC-AUC** | 74,9% |
| **Precision** | 66,2% |
| **Recall** | 46,7% |

### Features importantes

| Feature | Importance |
|---------|------------|
| Fréquence d'achat par mois | 21,7% |
| Dépense par jour | 13,4% |
| Panier moyen | 12,7% |
| Ancienneté client | 11,4% |

### Clients à risque

Le modèle identifie les clients avec une probabilité de churn > 70%, permettant de :
- Mettre en place des actions de rétention ciblées
- Optimiser les campagnes marketing
- Réduire le taux d'attrition

---

## 🚀 CI/CD avec GitHub Actions

### Pipeline automatisé

```
┌─────────────────────────────────────────────────────────────────┐
│                    PIPELINE CI/CD                               │
├─────────────────────────────────────────────────────────────────┤
│  ✅ Lint (flake8)          → Vérification du style de code     │
│  ✅ Test (pytest)          → Exécution des tests unitaires     │
│  ✅ Deploy (Databricks)    → Déploiement automatique           │
└─────────────────────────────────────────────────────────────────┘
```

### Déploiement automatique

Les notebooks sont déployés automatiquement vers Databricks :

```
/Shared/ecommerce-dev/
├── 01_generate_data.py
├── 02_silver_cleaning.py
├── 03_gold_aggregations.py
├── 04_mlflow_churn_model.py
└── 05_export_powerbi.py
```

---

## 🧪 Tests

### Exécuter les tests

```bash
pytest tests/
```

### Couverture des tests

- `test_cleaning.py` : Tests de nettoyage des données
- `test_aggregations.py` : Tests des agrégations

---

## 📈 Résultats

| Métrique | Valeur |
|----------|--------|
| Clients générés | 1 000 |
| Produits générés | 100 |
| Transactions générées | 5 000 |
| Modèle Churn Accuracy | ~71% |
| Dashboard Power BI | ✅ |

---

## 🤝 Contribution

Les contributions sont les bienvenues !

1. Fork le projet
2. Crée une branche (`git checkout -b feature/ma-feature`)
3. Commit (`git commit -m "Ajout de ma feature"`)
4. Push (`git push -u origin feature/ma-feature`)
5. Ouvre une Pull Request

---

## 📝 Licence

MIT License - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 👤 Auteur

**Moïse Ndegue Fongué**
- GitHub : [mndegue-pixel](https://github.com/mndegue-pixel)

---

## 🙏 Remerciements

- Azure Databricks pour la plateforme
- MLflow pour le tracking des modèles
- Power BI pour la visualisation
```

---

## 🚀 COMMENT METTRE À JOUR

### 1. Dans GitHub
1. Va sur **github.com/mndegue-pixel/ecommerce-analytics**
2. Ouvre `README.md`
3. Clique sur **"Edit"** (icône crayon ✏️)
4. **Supprime** tout le contenu existant
5. **Colle** le nouveau contenu ci-dessus
6. **Commit changes**

### 2. En local (PowerShell)
```powershell
# 1. Copier le contenu ci-dessus dans README.md
# 2. Pousser
git add README.md
git commit -m "Update README avec documentation complète"
git push
```

