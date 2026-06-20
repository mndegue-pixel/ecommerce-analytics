# E-Commerce Analytics Pipeline

[![CI/CD Pipeline](https://github.com/mndegue-pixel/ecommerce-analytics/actions/workflows/ci-cd.yml/badge.svg?branch=master)](https://github.com/mndegue-pixel/ecommerce-analytics/actions/workflows/ci-cd.yml)

## 📊 Architecture
- Bronze → Silver → Gold (Delta Lake, Azure Databricks)
- Azure Data Factory (orchestration)
- Azure DevOps (CI/CD)
- Power BI (visualisation)

## 🚀 Setup
1. Cloner le dépôt : `git clone https://github.com/mndegue-pixel/ecommerce-analytics.git`
2. Configurer Azure Databricks
3. Exécuter les notebooks dans l'ordre
4. Connecter Power BI

## 📁 Structure du projet
- `notebooks/` → Notebooks Databricks
- `tests/` → Tests unitaires
- `.github/workflows/` → CI/CD Pipeline GitHub Actions

## 🛠️ Technologies
- **Azure Databricks** (PySpark, Delta Lake, MLflow)
- **Azure Data Factory**
- **GitHub Actions** (CI/CD)
- **Power BI**
- **MLflow** (modèle de prédiction de churn)

## 📊 Dashboard Power BI
Le dashboard Power BI est disponible dans le projet.
