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

    def scade_inventar(self):
        """
        sa se adauge in inventar ingredientele respective
        :return:
        """
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
                cantitate_ingredient_nou_total = int(ingredients[adaugare_ingredient_nou]) - cantitate_ingredient_nou
            else:
                message_2 = "Acest ingredient nu este in inventar"
            dulap.seek(0)
            for key, value in ingredients.items():
                dulap.write((key + ' : ' + str(value) + '\n'))
            dulap.truncate()
            message = f'S-a adaugat {adaugare_ingredient_nou} in cantitatea de {cantitate_ingredient_nou} cantitatea totala este de {cantitate_ingredient_nou_total}'
        return message

    def adauga_inventar(self): #adaugarea ingredientelor noi in inventar

        with open("data/dulap.txt","r+") as dulap:
            content = dulap.read()
            lines = content.splitlines()
            # stadiu_raspuns = True
            print("Ce vrei sa adaugi ?")
            adaugare_ingredient_nou = str(input())
            print("Ce cantitate vrei sa adaugi ?")
            cantitate_ingredient_nou = int(input())
            ingredients = dict(line.split(' : ') for line in lines)
            if adaugare_ingredient_nou in ingredients:
                ingredients[adaugare_ingredient_nou] = int(ingredients[adaugare_ingredient_nou]) + cantitate_ingredient_nou
                cantitate_ingredient_nou_total = int(ingredients[adaugare_ingredient_nou]) + cantitate_ingredient_nou
            else:
                ingredients[adaugare_ingredient_nou] = cantitate_ingredient_nou
            dulap.seek(0)
            for key, value in ingredients.items():
                dulap.write((key + ' : ' + str(value) + '\n'))
            dulap.truncate()
            message = f'S-a adaugat {adaugare_ingredient_nou} in cantitatea de {cantitate_ingredient_nou} cantitatea totala este de {cantitate_ingredient_nou_total}'
        return message

    def verificare_inventar(self):
        """
        sa aflii ce este in inventar
        :return:
        """
        pass

    # def hello(self):
    #     print("Buna ce doresti sa faci astazi ?\n"
    #           "Pentru a adauga in inventar tasteaza 'A'\n"
    #           "Pentru a scadea ceva din inventar tasteaza 'S'\n"
    #           "Pentru a verifica inventaru tasteaza'V'")
    #     accepted_responses = ['A','S','V','R']
    #     stadiu_raspuns = False
    #     while stadiu_raspuns == False:
    #         self.raspuns = str(input('Alege o varianta: '))
    #         if self.raspuns =='A':
    #             self.adauga_inventar()
    #
    #         elif self.raspuns == 'S':
    #             stadiu_raspuns = True
    #             pass
    #         elif self.raspuns == 'V':
    #             print(f'Acesta este inventaru actual: {self.inventar}')
    #             stadiu_raspuns = True
    #             pass
    #         elif self.raspuns not in accepted_responses:
    #             print('Alegeti din variantele prestabilite')
    #             continue

