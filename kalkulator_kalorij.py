import bottle
import model

kalorije = model.Kalorije()

@bottle.get("/") 
def osnovna_stran():
    return bottle.template("views/osnovna_stran.tpl")

@bottle.post('/igra/')
def pokazi_igro():
    return bottle.template('views/igra.tpl')

@bottle.post('/igra/')
def preberi():
        
    starost = bottle.request.forms.get('starost')
    visina = bottle.request.forms.get('visina')
    masa = bottle.request.forms.get('masa')
    spol = bottle.request.forms.get('spol')
    aktivnost = bottle.request.forms.get('aktivnost')

    kalorije.teza = masa
    kalorije.visina = visina
    kalorije.starost = starost
    kalorije.spol = spol
    kalorije.aktivnost = aktivnost

    return bottle.template('views/igra.tpl', kalorije=kalorije)
    
bottle.run(reloader=True, debug=True)