import pickle

class Bucatarie():

    def __init__(self, nume):
        self.nume = nume
        self.inventar = {}
        with open("data/dulap.txt","r") as dulap:
            lines = dulap.readlines()
            for line in lines:
                if ':' in line:
                    key, value = line.strip().split(' : ')
                    self.inventar[key] = int(value)

    # adaugarea ingredientelor noi in inventar
    def scade_inventar(self):

        with open("data/dulap.txt","r+") as dulap:
            content = dulap.read()
            lines = content.splitlines()
            # stadiu_raspuns = True
            print("Ce vrei sa produs vrei sa scazi ?")
            adaugare_ingredient_nou = str(input())
            print("Ce cantitate vrei sa scazi ?")
            cantitate_ingredient_nou = int(input())
            ingredients = dict(line.split(' : ') for line in lines)
            if adaugare_ingredient_nou in ingredients:
                ingredients[adaugare_ingredient_nou] = int(ingredients[adaugare_ingredient_nou]) - cantitate_ingredient_nou
                cantitate_ingredient_nou_total = int(ingredients[adaugare_ingredient_nou])
            else:
                message_2 = "Acest ingredient nu este in inventar"
            dulap.seek(0)
            for key, value in ingredients.items():
                dulap.write((key + ' : ' + str(value) + '\n'))
            dulap.truncate()
            message = f'S-a scazut {adaugare_ingredient_nou} in cantitatea de {cantitate_ingredient_nou} cantitatea totala este de {cantitate_ingredient_nou_total}'
        return message

    # adaugarea ingredientelor noi in inventar
    def adauga_inventar(self):

        with open("data/dulap.txt","r+") as dulap:
            content = dulap.read()
            lines = content.splitlines()
            # stadiu_raspuns = True

            # Adaugarea ingredientului de tip str
            while True:
                print("Ce vrei sa adaugi ?")
                adaugare_ingredient_nou = input()
                if not adaugare_ingredient_nou.isalpha() and not adaugare_ingredient_nou.isspace():
                    print("Te rog sa introduci un ingredient valid ")
                else:
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


