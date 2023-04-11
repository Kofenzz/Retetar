import json


class Reteta():

    def __init__(self,file_path = "data\lista_retete.json"):
        self.file_path = file_path
        self.recipes = self.incarca_reteta()

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
            if ingredient not in dulap_dict or dulap_dict[ingredient] < int(cantitate):
                print("Nu aveti destule ingrediente")
                return None

        print(f"Aveti suficiente ingrediente pentru {reteta_selectata['nume']}")

        # Optiune de afisare intructiuni sau revenire la meniu

        while True:
            optiune = input(f"Doriti sa reveniti la meniu sau sa vedeti reteta {reteta_selectata['nume']}\n Pentru a vedea {reteta_selectata['nume']} tastati 'V'\n Pentru meniu tastati 'M'\n")
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

    def incarca_reteta(self):
        """ Incarcam lista curenta pentru a o pune intr-un dicitonar
        Returneaza:

        - dictionar: Contine retetele curente
        """
        with open(self.file_path, "r") as f:
            recipes = json.load(f)
        return recipes

    def salveaza_reteta(self):
        """
        Salveaza reteta curenta
        """
        with open(self.file_path,'w') as f:
            json.dump(self.recipes, f, indent=4)

    def adaugare_reteta(self):
        """
        Adauga reteta noua in dictionar

        Args:
        - nume (str): Numele retetei
        - durata (str): Durata de retetei
        - ingrediente (dict): Un dicitonar ce contine toate ingredientele retetei
        - pasi (list): O lista de pasi pentru a face reteta
        """

        # Luam informatiile pentru reteta noua

        nume = input("Introduceti numele retetei (trebuie sa contina litere):  ")
        durata = input("Introduce durata retetei (trebuie sa contina numere): ")
        ingrediente = {}
        while True:
            ingrediente_nume = input("Introduceti numele ingredientului (sau 'q' pentru a iesi): ")
            if ingrediente_nume == 'q':
                break
            ingrediente_cantitate = input("Introduceti cantitatea ingredientului: ")
            ingrediente[ingrediente_nume] = ingrediente_cantitate
        pasi = []
        while True:
            pas = input("Introduceti un pas pentru reteta (sau 'q' pentru a iesi): ")
            if pas == 'q':
                break
            pasi.append(pas)

        # Verificam care este urmatorul ID disponibil
        available_ids = [int(recipe_id) for recipe_id in self.recipes.keys()]
        next_id = str(max(available_ids) + 1) if available_ids else "1"

        # Creearea dictionarului care reprezinta noua reteta

        reteta_noua = {
            "id": next_id,
            "nume": nume,
            "durata":durata,
            "ingrediente":ingrediente,
            "pasi":pasi
        }

        # Adaugam reteta noua la dictionar cu ID ul nou ca si cheie

        self.recipes[next_id] = reteta_noua
        self.salveaza_reteta()

        print(f'Reteta cu ID-ul {next_id} si cu numele: {nume} a fost adaugata cu succes')
        return nume