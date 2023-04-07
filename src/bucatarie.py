import pickle

class Bucatarie():

    def __init__(self, nume):
        self.nume = nume
        self.inventar = {}
        self.deschide_dulap()


    def deschide_dulap(self):
        with open("data/dulap.txt","r") as dulap:
            lines = dulap.readlines()
            for line in lines:
                if ':' in line:
                    key, value = line.strip().split(' : ')
                    self.inventar[key] = int(value)


    # adaugarea ingredientelor noi in inventar
    def scade_inventar(self):
        cantitate_ingredient_nou_total = 0
        with open("data/dulap.txt","r+") as dulap:
            content = dulap.read()
            lines = content.splitlines()
            # stadiu_raspuns = True
            print("Ce vrei sa produs vrei sa scazi ?")
            while True:
                nefiltrat_scadere_ingredient_nou = str(input())
                scadere_ingredient_nou = nefiltrat_scadere_ingredient_nou.lower
                try:
                    float(scadere_ingredient_nou)
                    print("Va rog puneti un ingredient valid")
                    continue
                except ValueError:
                    break

            print("Ce cantitate vrei sa scazi ?")
            while True:
                cantitate_ingredient_nou = int(input())
                try:
                    float(cantitate_ingredient_nou)
                    break
                except ValueError:
                    print("va rog introduceti o cantitate in cifre")
                    continue

            ingredients = dict(line.split(' : ') for line in lines)
            if scadere_ingredient_nou in ingredients:
                ingredients[scadere_ingredient_nou] = int(ingredients[scadere_ingredient_nou]) - cantitate_ingredient_nou
                cantitate_ingredient_nou_total = int(ingredients[scadere_ingredient_nou])
            else:
                message_2 = "Acest ingredient nu este in inventar"
            dulap.seek(0)
            for key, value in ingredients.items():
                dulap.write((key + ' : ' + str(value) + '\n'))
            dulap.truncate()
            message = f'S-a scazut {scadere_ingredient_nou} in cantitatea de {cantitate_ingredient_nou} cantitatea totala este de {cantitate_ingredient_nou_total}'
        return message

    # adaugarea ingredientelor noi in inventar
    def adauga_inventar(self):
        cantitate_ingredient_nou_total = 0
        with open("data/dulap.txt","r+") as dulap:
            content = dulap.read()
            lines = content.splitlines()
            # stadiu_raspuns = True

            # Adaugarea ingredientului de tip str
            while True:
                print("Ce vrei sa adaugi ?")
                nefiltrat_adaugare_ingredient_nou = str(input())
                adaugare_ingredient_nou = nefiltrat_adaugare_ingredient_nou.lower()

                try:
                    float(adaugare_ingredient_nou)
                    print("Va rog sa introduceti un ingredient valid")
                    continue
                except ValueError:
                    break
            # Adaugarea cantitatea ingredientului de tip int
            while True:
                try:
                    print("Ce cantitate vrei sa adaugi ? ")
                    cantitate_ingredient_nou = int(input())
                    break
                except ValueError:
                    print("Te rog sa introduci o cantitate valida ")

            ingredients = dict(line.split(' : ') for line in lines)
            if adaugare_ingredient_nou in ingredients:
                ingredients[adaugare_ingredient_nou] = int(ingredients[adaugare_ingredient_nou]) + cantitate_ingredient_nou
                cantitate_ingredient_nou_total = int(ingredients[adaugare_ingredient_nou])
            else:
                ingredients[adaugare_ingredient_nou] = cantitate_ingredient_nou
            dulap.seek(0)
            for key, value in ingredients.items():
                dulap.write((key + ' : ' + str(value) + '\n'))
            dulap.truncate()
            message = f'S-a adaugat {adaugare_ingredient_nou} in cantitatea de {cantitate_ingredient_nou} cantitatea totala este de {cantitate_ingredient_nou_total}'
        return message


    def verifica_inventar(self):
        with open("data/dulap.txt", "r") as dulap:
            lines = dulap.readlines()
            for line in lines:
                if ':' in line:
                    key, value = line.strip().split(' : ')
                    self.inventar[key] = int(value)
        return print(self.inventar)