# Notebook: 00_generate_banking_data.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, col, lit, when, date_add, current_date, expr
import random

spark = SparkSession.builder.appName("BankDataGenerator").getOrCreate()

# Paramètres de simulation
nb_transactions = 2000000  # 2 millions de transactions
nb_clients = 50000
nb_cartes = 70000
nb_marchands = 1000

# 1. Génération des clients
clients = spark.range(1, nb_clients + 1) \
    .withColumn("nom", expr("concat('Client_', id)")) \
    .withColumn("date_naissance", date_add(current_date(), - (rand() * 20000 + 5000).cast("int"))) \
    .withColumn("ville", when(rand() < 0.3, "Paris").when(rand() < 0.6, "Lyon").otherwise("Marseille"))

# 2. Génération des cartes
cartes = spark.range(1, nb_cartes + 1) \
    .withColumn("id_client", (rand() * nb_clients + 1).cast("int")) \
    .withColumn("type_carte", when(rand() < 0.4, "VISA").when(rand() < 0.7, "MasterCard").otherwise("AMEX")) \
    .withColumn("date_emission", date_add(current_date(), - (rand() * 2000 + 100).cast("int"))) \
    .withColumn("plafond", (rand() * 5000 + 500).cast("int"))

# 3. Génération des marchands
marchands = spark.range(1, nb_marchands + 1) \
    .withColumn("nom_marchand", expr("concat('Marchand_', id)")) \
    .withColumn("categorie", when(rand() < 0.2, "Alimentation")
                .when(rand() < 0.4, "Habillement")
                .when(rand() < 0.6, "Électronique")
                .otherwise("Services"))

# 4. Génération des transactions (2 millions)
transactions = spark.range(1, nb_transactions + 1) \
    .withColumn("id_carte", (rand() * nb_cartes + 1).cast("int")) \
    .withColumn("id_marchand", (rand() * nb_marchands + 1).cast("int")) \
    .withColumn("montant", (rand() * 500 + 1).cast("double")) \
    .withColumn("date_transaction", date_add(current_date(), - (rand() * 1825).cast("int"))) \
    .withColumn("devise", when(rand() < 0.7, "EUR").otherwise("USD")) \
    .withColumn("statut", when(rand() < 0.95, "APPROUVEE").otherwise("REFUSEE"))

# Sauvegarde en CSV (simule l'extraction du mainframe)
transactions.coalesce(1).write.mode("overwrite").option("header", "true").csv("/dbfs/mnt/bronze/transactions_source")
clients.coalesce(1).write.mode("overwrite").option("header", "true").csv("/dbfs/mnt/bronze/clients_source")
cartes.coalesce(1).write.mode("overwrite").option("header", "true").csv("/dbfs/mnt/bronze/cartes_source")
marchands.coalesce(1).write.mode("overwrite").option("header", "true").csv("/dbfs/mnt/bronze/marchands_source")

print("✅ Données de test générées avec succès !")