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
                return None

        print(f"Aveti suficiente ingrediente pentru {reteta_selectata['nume']}")

        # Optiune de afisare intructiuni sau revenire la meniu

        while True:
            optiune = input(f"Doriti sa reveniti la meniu sau sa vedeti reteta {reteta_selectata['nume']}\n Pentru meniu tastati 'm'\n Pentru a vedea {reteta_selectata['nume']} tastati v\n")
            if optiune == 'm' or optiune == 'M':
                return
            elif optiune == 'v' or optiune == 'V':
                print(f"Reteta selectata este: {reteta_selectata['nume']}")
                print(f"Ingrediente: \n")
                for i, (nume, cantitate) in enumerate(reteta_selectata['ingrediente'].items()):
                    print(f"{i + 1}. {nume} : {cantitate}\n")
                print(f"Mod de preparare: \n")
                for i, step in enumerate(reteta_selectata['pasi']):
                    print(f"{i + 1}. {step}\n")
            else:
                print("Te rog sa introduci o optine valida")
                continue

    def adaugare_reteta(self):
        print(s)

    def stergere_reteta(self):
        pass

    # def informatii_reteta(self, reteta_selectata):
    #     if reteta_selectata is None:
    #         print("Nu s-a selectat o reteta")
    #     else:
    #         print(f"Reteta selectata este: {reteta_selectata['nume']}")
    #         print(f"Ingrediente: ")
    #         for i, step in enumerate(reteta_selectata['ingrediente']):
    #             print(f"{i+1}. {step}\n")
    #         print(f"Mod de preparare: ")
    #         for i, step in enumerate(reteta_selectata['mod_de_preparare']):
    #             print(f"{i+1}. {step}\n")