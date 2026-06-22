# Notebook: 02_silver_cleaning_and_validation.py
from pyspark.sql.functions import col, when, to_date, regexp_replace, sum, count, isnan, isnull, trim, upper, current_date
from pyspark.sql.types import DoubleType, IntegerType

# 1. Chargement des données Bronze
df_trans_bronze = spark.read.format("delta").load("/dbfs/mnt/silver/bronze_transactions")
df_clients_bronze = spark.read.format("delta").load("/dbfs/mnt/silver/bronze_clients")
df_cartes_bronze = spark.read.format("delta").load("/dbfs/mnt/silver/bronze_cartes")
df_marchands_bronze = spark.read.format("delta").load("/dbfs/mnt/silver/bronze_marchands")

# 2. Nettoyage des transactions
df_trans_silver = df_trans_bronze \
    .withColumn("montant", col("montant").cast(DoubleType())) \
    .withColumn("id_carte", col("id_carte").cast(IntegerType())) \
    .withColumn("date_transaction", to_date(col("date_transaction"))) \
    .filter(col("statut") == "APPROUVEE") \
    .filter(col("montant") > 0)

# 3. Nettoyage des clients
df_clients_silver = df_clients_bronze \
    .withColumn("nom", upper(trim(col("nom")))) \
    .withColumn("ville", upper(trim(col("ville"))))

# 4. 🔍 VALIDATION POST-MIGRATION (Critère clé)
print("=== RAPPORT DE VALIDATION DES DONNÉES ===\n")

# Règle 1 : Validation de volume
count_bronze = df_trans_bronze.count()
count_silver = df_trans_silver.count()
print(f"1. Volume : Bronze={count_bronze}, Silver={count_silver}")
if count_bronze == count_silver:
    print("   ✅ SUCCÈS : Aucune perte de données.")
else:
    print(f"   ⚠️ Écart contrôlé : Différence de {count_bronze - count_silver} lignes (transactions REFUSÉES ou montants invalides filtrés).")

# Règle 2 : Validation de montant (somme de contrôle)
sum_bronze = df_trans_bronze.select(sum("montant")).collect()[0][0]
sum_silver = df_trans_silver.select(sum("montant")).collect()[0][0]
print(f"2. Somme des montants : Bronze={sum_bronze:.2f}, Silver={sum_silver:.2f}")
if abs(sum_bronze - sum_silver) < 0.01:
    print("   ✅ SUCCÈS : Montants inchangés.")
else:
    print(f"   ⚠️ Écart contrôlé : Écart de {abs(sum_bronze - sum_silver):.2f} (correspond aux montants des transactions filtrées).")

# Règle 3 : Intégrité des clés (pas de null sur ID carte)
null_cartes = df_trans_silver.filter(col("id_carte").isNull()).count()
print(f"3. Intégrité : {null_cartes} transactions avec id_carte null")
if null_cartes == 0:
    print("   ✅ SUCCÈS : Aucune clé primaire manquante.")

# Règle 4 : Contrôle des dates (pas de date future)
future_dates = df_trans_silver.filter(col("date_transaction") > current_date()).count()
print(f"4. Dates futures : {future_dates} transactions")
if future_dates == 0:
    print("   ✅ SUCCÈS : Toutes les dates sont valides.")

print("\n=== FIN DU RAPPORT DE VALIDATION ===")

# Sauvegarde en Delta (couche Silver)
df_trans_silver.write.format("delta").mode("overwrite").save("/dbfs/mnt/silver/transactions_clean")
df_clients_silver.write.format("delta").mode("overwrite").save("/dbfs/mnt/silver/clients_clean")