# Notebook: 01_bronze_ingestion.py
# Chargement des données sources
df_transactions = spark.read.option("header", "true").csv("/dbfs/mnt/bronze/transactions_source")
df_clients = spark.read.option("header", "true").csv("/dbfs/mnt/bronze/clients_source")
df_cartes = spark.read.option("header", "true").csv("/dbfs/mnt/bronze/cartes_source")
df_marchands = spark.read.option("header", "true").csv("/dbfs/mnt/bronze/marchands_source")

# Sauvegarde en Delta (couche Bronze)
df_transactions.write.format("delta").mode("overwrite").save("/dbfs/mnt/silver/bronze_transactions")
df_clients.write.format("delta").mode("overwrite").save("/dbfs/mnt/silver/bronze_clients")
df_cartes.write.format("delta").mode("overwrite").save("/dbfs/mnt/silver/bronze_cartes")
df_marchands.write.format("delta").mode("overwrite").save("/dbfs/mnt/silver/bronze_marchands")

print("✅ Couche Bronze créée avec succès dans Delta Lake")