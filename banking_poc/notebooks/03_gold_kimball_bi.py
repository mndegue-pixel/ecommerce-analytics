# Notebook: 03_gold_kimball_bi.py (Version corrigée - Ambiguïté résolue)
from pyspark.sql.functions import year, month, dayofmonth, col, unix_timestamp

# 1. Chargement des données Silver
df_trans = spark.read.format("delta").load("/dbfs/mnt/silver/transactions_clean")
df_clients = spark.read.format("delta").load("/dbfs/mnt/silver/clients_clean")
df_cartes = spark.read.format("delta").load("/dbfs/mnt/silver/bronze_cartes")
df_marchands = spark.read.format("delta").load("/dbfs/mnt/silver/bronze_marchands")

# 2. Création de la Dimension Temps (avec conversion correcte)
dim_temps = df_trans.select("date_transaction") \
    .distinct() \
    .withColumn("annee", year("date_transaction")) \
    .withColumn("mois", month("date_transaction")) \
    .withColumn("jour", dayofmonth("date_transaction")) \
    .withColumn("id_temps", unix_timestamp(col("date_transaction")).cast("long"))

# 3. Création de la Dimension Carte (avec jointure Client - CORRECTION ICI)
# On renomme les colonnes avant la jointure pour éviter l'ambiguïté
df_cartes_renamed = df_cartes.select(
    col("id").alias("id_carte"),
    col("id_client"),
    col("type_carte"),
    col("plafond"),
    col("date_emission")
)

df_clients_renamed = df_clients.select(
    col("id").alias("id_client"),  # On renomme pour faire la jointure
    col("nom").alias("nom_client"),
    col("ville").alias("ville_client")
)

dim_carte = df_cartes_renamed.join(df_clients_renamed, "id_client", "left") \
    .select(
        col("id_carte"),
        col("type_carte"),
        col("plafond"),
        col("date_emission"),
        col("nom_client"),
        col("ville_client")
    )

# 4. Création de la Dimension Marchand
dim_marchand = df_marchands.select(
    col("id").alias("id_marchand"),
    col("nom_marchand"),
    col("categorie")
)

# 5. Création de la Table de Faits (Transactions)
fact_transaction = df_trans.select(
    col("id").alias("id_transaction"),
    col("date_transaction"),
    col("id_carte"),
    col("id_marchand"),
    col("montant"),
    col("devise")
)

# 6. Sauvegarde en Delta (couche Gold - Prête pour Power BI)
dim_temps.write.format("delta").mode("overwrite").save("/dbfs/mnt/gold/dim_temps")
dim_carte.write.format("delta").mode("overwrite").save("/dbfs/mnt/gold/dim_carte")
dim_marchand.write.format("delta").mode("overwrite").save("/dbfs/mnt/gold/dim_marchand")
fact_transaction.write.format("delta").mode("overwrite").save("/dbfs/mnt/gold/fact_transaction")

print("✅ Couche Gold créée avec succès (Modèle Kimball)")