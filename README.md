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
┌─────────────────────────────────────────────────────────────────────────┐
│ ARCHITECTURE MÉDAILLON │
├─────────────────────────────────────────────────────────────────────────┤
│ │
│ 🥉 Bronze (Raw Data) 🥈 Silver (Cleaned) 🥇 Gold (Aggregated) │
│ │
│ ┌─────────────────┐ ┌──────────────────┐ ┌──────────────────┐ │
│ │ customers │ │ customers_clean │ │ monthly_sales │ │
│ │ products │ ──▶ │ products_clean │ ──▶│ top_products │ │
│ │ transactions │ │ transactions_ │ │ customer_seg │ │
│ └─────────────────┘ │ clean │ │ churn_predict │ │
│ │ transactions_ │ └──────────────────┘ │
│ │ enriched │ │
│ └──────────────────┘ │
└─────────────────────────────────────────────────────────────────────────┘

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
ecommerce-analytics/
├── .github/
│ └── workflows/
│ └── ci-cd.yml # Pipeline CI/CD GitHub Actions
├── notebooks/
│ ├── 01_generate_data.py # Génération des données de test
│ ├── 02_silver_cleaning.py # Nettoyage (couche Silver)
│ ├── 03_gold_aggregations.py # Agrégations (couche Gold)
│ ├── 04_mlflow_churn_model.py # Modèle ML avec MLflow
│ └── 05_export_powerbi.py # Export pour Power BI
├── tests/
│ ├── test_cleaning.py # Tests unitaires - Nettoyage
│ └── test_aggregations.py # Tests unitaires - Agrégations
├── .gitignore
├── README.md
└── requirements.txt


---

## 🚀 Installation et exécution

### 1. Cloner le dépôt

```bash
git clone https://github.com/mndegue-pixel/ecommerce-analytics.git
cd ecommerce-analytics


---

## 🚀 Installation et exécution

### 1. Cloner le dépôt

```bash
git clone https://github.com/mndegue-pixel/ecommerce-analytics.git
cd ecommerce-analytics
