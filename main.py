import time
from src import bucatarie as b
from src import reteta as r

def meniu_principal():
    print("Ce doresti sa faci astazi ?")
    accepted_responses = ['A', 'S', 'V', 'R', 'X']
    stadiu_raspuns = False
    bucatarie = b.Bucatarie("Bucatarie_1")
    while stadiu_raspuns == False:
        text_meniu = """Meniu Principal
    Pentru a adauga in inventar tasteaza 'A'
    Pentru a scadea ceva din inventar tasteaza 'S'
    Pentru a verifica inventaru tasteaza'V'
    Pentru a folosi o reteta tasteaza 'R'
    Pentru a iesi din program tasteaza 'X'"""
        print(text_meniu)
        print("-----------------------------------------------")
        raspuns = str(input('Alege o varianta: ')) \
            # Adaugi in inventar
        if raspuns == 'A' or raspuns == 'a':
            message = bucatarie.adauga_inventar()
            print(message)
            time.sleep(1)
            print("-----------------------------------------------")
        # Scazi din inventar
        elif raspuns == 'S' or raspuns == 's':
            message = bucatarie.scade_inventar()
            print(message)
            time.sleep(1)
            print("-----------------------------------------------")
        # Verifici inventaru
        elif raspuns == 'V' or raspuns == 'v':
            bucatarie.verifica_inventar()
            time.sleep(1)
            print("-----------------------------------------------")
            continue
        # Mergi la meniul retete
        elif raspuns == 'R' or raspuns == 'r':
            meniu_reteta()
            time.sleep(1)
            print("-----------------------------------------------")

        # Iesi din program
        elif raspuns == 'X' or raspuns == 'x':
            print("La Revedere !")
            break
        # Verifica ca tasta trimisa sa fie una dintre optiunile acceptate
        elif raspuns not in accepted_responses:
            print('Alegeti din variantele prestabilite')
            continue


def meniu_reteta():
    reteta = r.Reteta()
    accepted_responses_retete = ['L', 'S', 'I', 'X']
    print("-----------------------------------------------")
    text_meniu_reteta = """Meniu Reteta
        Pentru a vedea lista de retete tasteaza 'L'
        Pentru a selecta o reteta tasteaza 'S'
        Pentru a te intoarce la meniul initial tasteaza 'I'
        Pentru a adauga o reteta tastati 'A'
        Pentru a iesi din program tastati 'X'"""
    print(text_meniu_reteta)
    print("Ce doresti sa faci?")
    while True:
        reteta_input = str(input())
        print("-----------------------------------------------")
        if reteta_input == 'L' or reteta_input == 'l':
            mesaj_retete = reteta.lista_retete()
            print(mesaj_retete)
            time.sleep(1)
            print("-----------------------------------------------")
            print(text_meniu_reteta)
            continue
        elif reteta_input == 'S' or reteta_input == 's':
            reteta.selectare_reteta()
            time.sleep(1)
            print("-----------------------------------------------")
            print(text_meniu_reteta)
        elif reteta_input == 'A' or reteta_input == 'a':
            reteta.adaugare_reteta()
            time.sleep(1)
            print("-----------------------------------------------")
            print(text_meniu_reteta)
        elif reteta_input == 'I' or reteta_input == 'i':
            meniu_principal()
            break
        elif reteta_input == 'X' or reteta_input == 'x':
            print("Ne Intoarcem la meniul principal !")
            break
        elif reteta_input not in accepted_responses_retete:
            print('Alegeti din variantele prestabilite')
            print("-----------------------------------------------")
            print(text_meniu_reteta)


if __name__ == "__main__":
    meniu_principal()
