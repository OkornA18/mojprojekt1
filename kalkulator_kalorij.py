import bottle
from model import Kalorije

@bottle.get("/") 
def osnovna_stran():
    return bottle.template("views/osnovna_stran.tpl")

@bottle.post('/igra/')
def pokazi_igro():
    
    return bottle.template('views/igra.tpl')

bottle.run(reloader=True, debug=True)