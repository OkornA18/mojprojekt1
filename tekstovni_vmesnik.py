from model import Kalorije

print('Izračunajmo predvideno oceno tvojega dnevnega vnosa kalorij.')


def uporabnik():
    starost = int(input('Vpišite svojo starost: '))
    spol = input('Vpišite svoj spol(moški, ženski): ')
    teza = int(input('Vpišite svojo težo v kilogramih: '))
    visina = int(input('Vpišite svojo višino v centimetrih: '))

    if spol == "moški":
        bmr = ((10*teza) + (6.25*visina) - (5*starost) + 5)b
    else:   
        bmr = ((10*teza) + (6.25*visina) - (5*starost) - 161)
    return bmr

def aktivnost(bmr): 
    aktivnostna_stopnja = input('Brez aktivnosti, Zelo malo aktivnosti (1-3 dni na teden),Zmerna aktivnost (3-5 dni na teden), Visoka stopnja aktivnosti (6-7 dni na teden), Zelo visoka stopnja aktivnosti (2× na dan, zelo težki treningi)? :  ')

    if aktivnostna_stopnja == 'Brez aktivnosti':
        aktivnostna_stopnja = 1.2 * bmr
    elif aktivnostna_stopnja == 'Zelo malo aktivnosti (1-3 dni na teden)':
        aktivnostna_stopnja = 1.3 * bmr
    elif aktivnostna_stopnja == 'Zmerna aktivnost (3-5 dni na teden)':
        aktivnostna_stopnja = 1.5 * bmr
    elif aktivnostna_stopnja == 'Visoka stopnja aktivnosti (6-7 dni na teden)':
        aktivnostna_stopnja = 1.7 * bmr
    elif aktivnostna_stopnja == 'Zelo visoka stopnja aktivnosti (2× na dan, zelo težki treningi)':
        aktivnostna_stopnja = 1.9 * bmr

    return(int(aktivnostna_stopnja))

def izgubitev_pridobitev(aktivnostna_stopnja):
    cilj = input('Želite vzdrževati, pridobiti ali izgubiti telesno težo: ')
    kalorije = Kalorije(teza, visina, starost, spol)
    if cilj == 'izgubiti':
        koncne_kalorije = kalorije.izguba(aktivnostna_stopnja)
    elif cilj == 'vzdrževati':
        koncne_kalorije = kalorije.vzdrzevanje(aktivnostna_stopnja)
    elif cilj == 'pridobiti':
        koncne_kalorije = kalorije.pridobitev(aktivnostna_stopnja)

    print('Če je vaš cilj ', cilj, 'telesno težo, morate na dan zaužiti', int(koncne_kalorije), 'kalorij!')


izgubitev_pridobitev(aktivnost(uporabnik()))