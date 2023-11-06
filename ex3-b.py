# Définition de la fonction pour convertir le CTR en pourcentage
def convertir_ctr_en_pourcentage(ctr):
    return ctr * 100

# Tests de la fonction avec différentes entrées
ctr_test_1 = 0.05
ctr_test_2 = 0.1
ctr_test_3 = 0.02

# Affichage des résultats
print(f"CTR en pourcentage ({ctr_test_1}): {convertir_ctr_en_pourcentage(ctr_test_1)}%")
print(f"CTR en pourcentage ({ctr_test_2}): {convertir_ctr_en_pourcentage(ctr_test_2)}%")
print(f"CTR en pourcentage ({ctr_test_3}): {convertir_ctr_en_pourcentage(ctr_test_3)}%")
