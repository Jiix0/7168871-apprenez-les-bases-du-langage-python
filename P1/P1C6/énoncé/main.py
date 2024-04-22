# Écrivez votre code ici !
'''Créez une liste nommée fruits contenant les éléments "pomme", "banane" et "orange".
Ajoutez "kiwi" à la liste fruits.
Supprimez "orange" de la liste fruits.
Modifiez le deuxième élément de la liste fruits en "ananas".
Affichez la longueur de la liste fruits.
Triez la liste fruits par ordre alphabétique
Affichez la liste. (N'oubliez pas d'afficher la liste pour que les tests passent)'''


fruits = ["pomme","banana","orange"]
fruits.append("kiwi")
fruits.remove("orange")
fruits[1] = "ananas"
print(len(fruits))
