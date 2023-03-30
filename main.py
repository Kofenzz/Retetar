import time
from src import bucatarie as b
# from src import produs_final as p
# from src import reteta as r



def hello():
    s = """Ce doresti sa faci astazi ?
    Pentru a adauga in inventar tasteaza 'A'
    Pentru a scadea ceva din inventar tasteaza 'S'
    Pentru a verifica inventaru tasteaza'V'
    Pentru a folosi o reteta tasteaza 'R'
    Pentru a iesi din program tasteaza 'X'"""
    print(s)
    accepted_responses = ['A' ,'S' ,'V' ,'R','X']
    stadiu_raspuns = False
    bucatarie = b.Bucatarie("Bucatarie_1")
    while stadiu_raspuns == False:
        print("-----------------------------------------------")
        raspuns = str(input('Alege o varianta: '))\
        # Adaugi in inventar
        if raspuns =='A' or raspuns == 'a':
            message = bucatarie.adauga_inventar()
            print(message)
            time.sleep(1)
            print("-----------------------------------------------")
            print(s)
        # Scazi din inventar
        elif raspuns == 'S' or raspuns == 's':
            message = bucatarie.scade_inventar()
            print(message)
            time.sleep(1)
            print("-----------------------------------------------")
            print(s)
        # Verifici inventaru
        elif raspuns == 'V' or raspuns == 'v':
            print(f'Acesta este inventaru actual: {bucatarie.inventar}')
            time.sleep(1)
            print("-----------------------------------------------")
            print(s)
            continue
        # Mergi la meniul retete
        elif raspuns == 'R' or raspuns == 'r':
            pass
        # Iesi din program
        elif raspuns == 'X' or raspuns == 'x':
            break
        # Verifica ca tasta trimisa sa fie una dintre optiunile acceptate
        elif raspuns not in accepted_responses:
            print('Alegeti din variantele prestabilite')
            continue

hello()