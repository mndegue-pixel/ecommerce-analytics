# =============================================
# setup.ps1 - Script de configuration
# Projet : E-Commerce Analytics Pipeline
# =============================================

Write-Host ""
Write-Host "🚀 CREATION DE LA STRUCTURE DU PROJET" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# =============================================
# 1. Creer les dossiers
# =============================================

Write-Host "📁 Creation des dossiers..." -ForegroundColor Yellow

$folders = @(
    ".azure-pipelines",
    "notebooks",
    "tests"
)

foreach ($folder in $folders) {
    if (!(Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder -Force | Out-Null
        Write-Host "   ✅ $folder" -ForegroundColor Green
    } else {
        Write-Host "   ⏳ $folder (deja existant)" -ForegroundColor Gray
    }
}

# =============================================
# 2. Creer les fichiers Python
# =============================================

Write-Host ""
Write-Host "📄 Creation des fichiers..." -ForegroundColor Yellow

$pythonFiles = @(
    "notebooks\01_generate_data.py",
    "notebooks\02_silver_cleaning.py",
    "notebooks\03_gold_aggregations.py",
    "notebooks\04_mlflow_churn_model.py",
    "notebooks\05_export_powerbi.py",
    "tests\test_cleaning.py",
    "tests\test_aggregations.py",
    ".azure-pipelines\ci-cd-pipeline.yml"
)

foreach ($file in $pythonFiles) {
    if (!(Test-Path $file)) {
        $content = "# Fichier: $file`n# Projet: E-Commerce Analytics`n# A completer..."
        $content | Out-File -FilePath $file -Encoding UTF8
        Write-Host "   ✅ $file" -ForegroundColor Green
    } else {
        Write-Host "   ⏳ $file (deja existant)" -ForegroundColor Gray
    }
}

# =============================================
# 3. Creer README.md
# =============================================

Write-Host ""
Write-Host "📄 Creation de README.md..." -ForegroundColor Yellow

if (!(Test-Path "README.md")) {
    $readme = @"
# E-Commerce Analytics Pipeline

## Architecture
- Bronze -> Silver -> Gold (Delta Lake, Azure Databricks)
- Azure Data Factory
- Azure DevOps (CI/CD)
- Power BI

## Setup
1. Cloner le depot
2. Configurer Azure Databricks
3. Executer les notebooks dans l'ordre
4. Connecter Power BI

## Structure
- notebooks/ -> Notebooks Databricks
- tests/ -> Tests unitaires
- .azure-pipelines/ -> CI/CD Pipeline

## Technologies
- Azure Databricks (PySpark, Delta Lake)
- Azure Data Factory
- Azure DevOps
- Power BI
- MLflow
"@
    $readme | Out-File -FilePath "README.md" -Encoding UTF8
    Write-Host "   ✅ README.md" -ForegroundColor Green
}

# =============================================
# 4. Creer requirements.txt
# =============================================

Write-Host ""
Write-Host "📄 Creation de requirements.txt..." -ForegroundColor Yellow

if (!(Test-Path "requirements.txt")) {
    $requirements = @"
pyspark>=3.4.0
delta-spark>=2.4.0
mlflow>=2.5.0
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.3.0
pytest>=7.4.0
flake8>=6.0.0
databricks-cli>=0.17.0
"@
    $requirements | Out-File -FilePath "requirements.txt" -Encoding UTF8
    Write-Host "   ✅ requirements.txt" -ForegroundColor Green
}

# =============================================
# 5. Creer .gitignore
# =============================================

Write-Host ""
Write-Host "📄 Creation de .gitignore..." -ForegroundColor Yellow

if (!(Test-Path ".gitignore")) {
    $gitignore = @"
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.egg-info/
dist/
build/

# Databricks
*.dbc
*.db

# Environment
.env
venv/
.venv/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Data
data/
*.csv
*.parquet
"@
    $gitignore | Out-File -FilePath ".gitignore" -Encoding UTF8
    Write-Host "   ✅ .gitignore" -ForegroundColor Green
}

# =============================================
# 6. Afficher la structure finale
# =============================================

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "📁 STRUCTURE FINALE DU PROJET" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Afficher la structure
Get-ChildItem -Recurse | Select-Object FullName

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "✅ STRUCTURE CREE AVEC SUCCES !" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "📂 Dossier du projet : $PWD" -ForegroundColor White
Write-Host ""
Write-Host "🚀 Prochaines etapes :" -ForegroundColor Yellow
Write-Host "   1. Remplir les notebooks avec le code"
Write-Host "   2. Configurer Azure DevOps"
Write-Host "   3. Pousser le code sur le repository"
Write-Host ""