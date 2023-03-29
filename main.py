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
        raspuns = str(input('Alege o varianta: '))
        if raspuns =='A' or raspuns == 'a':
            message = bucatarie.adauga_inventar()
            print(message)
            time.sleep(1)
            print("-----------------------------------------------")
            print(s)
        elif raspuns == 'S' or raspuns == 's':
            pass
        elif raspuns == 'V' or raspuns == 'v':
            print(f'Acesta este inventaru actual: {bucatarie.inventar}')
            time.sleep(1)
            print("-----------------------------------------------")
            print(s)
            continue
        elif raspuns == 'R' or raspuns == 'r':
            pass
        elif raspuns == 'X' or raspuns == 'x':
            break
        elif raspuns not in accepted_responses:
            print('Alegeti din variantele prestabilite')
            continue

hello()