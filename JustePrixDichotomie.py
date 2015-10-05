import random

Min=int(input('Minimum:'))
Max=int(input('Maximum:'))
Nbr=random.randint(Min,Max)
compteur=0
Valeur=Min-1

while Nbr != Valeur:
    Valeur=(int)(Min+Max)//2
    print('coup', compteur+1, ':', Valeur)
    if Valeur > Nbr:
        Max = Valeur-1
    
    if Valeur < Nbr:
        Min = Valeur +1
        
    
    compteur = compteur + 1
    
print("Nombre de coups:", compteur, '   Bien joué!')
