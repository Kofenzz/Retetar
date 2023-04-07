import json
# import bucatarie
class Reteta():

    def __init__(self,):
        self.lista = {}

    def lista_retete(self):

        with open("data\lista_retete.json", "r") as l_r:
            retete_lista = json.load(l_r)
            nume_retete = [retete_lista[id]['nume'] for id in retete_lista]
            mesaj_retete = nume_retete
            return mesaj_retete
    def selectare_reteta(self):
        # Incarcam ingredientele din dulap intr-un dictionar

        with open("data/dulap.txt", "r") as dulap:
            content = dulap.read()
            lines = content.splitlines()
            dulap_dict = {}
            for line in lines:
                ingredient, cantitate = line.split(' : ')
                dulap_dict[ingredient] = int(cantitate)
        retete = self.lista_retete()
        for i, reteta in enumerate(retete):
            print(f'{i+1}. {reteta}')
        # Alegerea retetei
        while True:
            try:
                numar_reteta = int(input("Selecteaza o reteta (introduce numarul din fata acesteia): \n"))
                if numar_reteta < 1 or numar_reteta > len(retete):
                    print("Te rog sa introduci un numar valid")
                    continue
                else:
                    break
            except ValueError:
                print("te rog sa introduci un numar valid")

        # Incarcam reteta aleasa

        with open("data\lista_retete.json","r") as l_r:
            retete_lista = json.load(l_r)
            reteta_selectata = retete_lista[str(numar_reteta)]


        # Verificam daca in dulap sunt ingrediente suficiente

        for ingredient, cantitate in reteta_selectata['ingrediente'].items():
            if ingredient not in dulap_dict or dulap_dict[ingredient] < cantitate:
                print("Nu aveti destule ingrediente")
                return

        print(f"Aveti suficiente ingrediente pentru reteta {reteta_selectata['nume']}")