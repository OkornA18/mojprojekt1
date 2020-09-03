from model import Kalorije

print('Izračunajmo predvideno oceno tvojega dnevnega vnosa kalorij..')

# vpiši starost
starost = int(input("Vpiši svojo starost: "))

# vpiši Z ali M za spol
while True:
    try:
        spol = str(input("Vpiši svoj spol (M za moški in Z za ženski): "))  
        if spol not in ['M','Z']:
            raise AssertionError('Prosim, vpišite črko M ali Z')
        break
    except AssertionError as e:
        print(e)
        
# vpiši težo v kg
while True:
    try:
        teza = float(input("Vpiši svojo težo v kg: "))
        # asserting teza is in Kg
        if not teza < 180:
            raise AssertionError('Teža mora biti v kilogramih, npr. 61, 84..')
        break
    except AssertionError as e:
        print(e)    
        
# Vpiši višina v cm
while True:
    try:
        visina = float(input("Vpiši svojo višino v cm: "))
        # Vpiši visino v cm
        if not visina > 80:
            raise AssertionError('Višina mora biti v centimetrih, npr. 167, 179..')
        break
    except AssertionError as e:
        print(e)            

kalorije = Kalorije(teza, visina, starost, spol)

aktivnost = float(input('''
1.2 - Brez aktivnosti
1.3 - Zelo malo aktivnosti (1-3 dni na teden)
1.5 - Zmerna aktivnost (3-5 dni na teden)
1.7 - Visoka stopnja aktivnosti (6-7 dni na teden)
1.9 - Zelo visoka stopnja aktivnosti (2× na dan, zelo težki treningi) 

Vpiši multiplikator pred stopnjo aktivnosti, ki velja zate (števila med 1.2 in 1.9): '''))

print('''Tvoj dnevni vnos kalorij:
{} za vzdrževanje telesne teže
{} za izgubo telesne teže
{} za pridobitev telesne teže'''.format(kalorije.vzdrzevanje(act_mult = aktivnost), kalorije.izguba(act_mult = aktivnost), kalorije.pridobitev(act_mult = aktivnost)))


# vpiši svoj cilj
while True:
    try:
        cilj = str(input("Kaj je tvoj cilj? Vpiši V za vzdrževanje, I za izgubo ali P za pridobitev: "))  
        if cilj not in ['V','I','P']:
            raise AssertionError('Prosim, vpiši črko V,I ali P')
        break
    except AssertionError as e:
        print(e)
        
if cilj == 'V':
    dnevne_kalorije = kalorije.vzdrzevanje(act_mult = aktivnost)
elif cilj == 'I':
    dnevne_kalorije = kalorije.izguba(act_mult = aktivnost)
elif cilj == 'P':
    dnevne_kalorije = kalorije.pridobitev(act_mult = aktivnost)
    
    
protein = kalorije.proteinski_vnos(teza)


print('''Tvoj dnevni minimalni proteinski vnos: {} gramov'''.format(protein))
