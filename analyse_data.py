#%% 
import pandas as pd
import matplotlib.pyplot as plt
#%%
# Load data from CSV files
data = pd.read_csv('All_Data.csv', delimiter=';')

#Display the first few rows of the dataframes
print(data.head())

#Affiche de nombre total de patients 
total_patients = data['Patient_ID'].nunique()
print(f"Nombre total de patients : {total_patients}")

#%%
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

#%%
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

#%%
""" Partition par Blood month sample """
plt.figure(figsize=(6, 4))
data['Blood_Month_sample'].value_counts().sort_index().plot(kind='bar', color='lightgreen')
plt.title("Nombre de patients par Blood Month")
plt.xlabel("Blood Month")
plt.ylabel("Nombre de patients")
plt.xticks(rotation=45)
plt.show()

#%%
"""Partition par Type d'habitat"""
type_habitat= data['Rural_or_urban_area'].value_counts().sort_index()

for index, value in type_habitat.items():
    if index==9: 
        print(f"Nombre de partient avec habitat manquant est :  {value} patients")
plt.figure(figsize=(6, 4))
type_habitat.plot(kind='bar')
plt.title("Nombre de patients par type d'habitat")
plt.xlabel("Type d'habitat")
plt.ylabel("Nombre de patients")
plt.legend()
plt.xticks(ticks=[0, 1, 2], labels=["Rural", "Urbain", "Manquant"], rotation=0) 
plt.show()
# %%
fact_gen= data['General_cofactors'].value_counts().sort_index()

for index, value in fact_gen.items():
    if index==9: 
        print(f"Nombre de facteurs non renseigner est :  {value} patients")

plt.figure(figsize=(6, 4))
fact_gen.plot(kind='bar')
plt.title("facteurs généraux")
plt.xlabel("Type facteurs")
plt.ylabel("Nombre de patients")
plt.legend()
plt.xticks(ticks=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], labels=["Aucun",
                    "Effort", "AINS", "Alcool", "Moississures", 
                    "Acariens", "Chat", "Chien", "Cheval", 
                    "Manquants", "ronguer", "Mucoviscidose", 
                    "IPP"], rotation=0) 
plt.show()        
# %%
