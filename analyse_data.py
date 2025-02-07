import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV files
data = pd.read_csv('All_Data.csv', delimiter=';')

# Display the first few rows of the dataframes
# print(data.head())

#Affiche de nombre total de patients 
total_patients = data['Patient_ID'].nunique()
print(f"Nombre total de patients : {total_patients}")

""" Partition  des patients par genre """
# Calcul du pourcentage des hommes et des femmes
gender_counts = data['Gender'].value_counts(normalize=True) * 100
print("Pourcentage des hommes et des femmes :")
print(gender_counts)

# Dessiner l'histogramme
plt.figure(figsize=(6, 4))
gender_counts.plot(kind='bar', color=['blue', 'pink'])
plt.title("Répartition des hommes et des femmes")
plt.xlabel("Genre")
plt.ylabel("Pourcentage")
plt.xticks(rotation=0)
plt.show()

""" Partition des patients par âge """
# Calcul de l'âge moyen
age_mean = data['Age'].mean()
print(f"L'âge moyen des patients : {age_mean:.2f} ans")

# Dessiner l'histogramme du nombre de personnes par âge
age_counts = data['Age'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
age_counts.plot(kind='bar', color='skyblue')
plt.legend()
plt.title("Nombre de personnes par âge")
plt.xlabel("Âge")
plt.ylabel("Nombre de personnes")
plt.xticks(rotation=0)
plt.show()
print("Nombre de personnes par âge :", age_counts)

""" Partition par BLood month"""

plt.figure(figsize=(6, 4))
data['Blood_Month_sample'].value_counts().sort_index().plot(kind='bar', color='lightgreen')
plt.title("Nombre de patients par Blood Month")
plt.xlabel("Blood Month")
plt.ylabel("Nombre de patients")
plt.xticks(rotation=45)
plt.show()



