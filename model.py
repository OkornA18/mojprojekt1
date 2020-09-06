class Kalorije():

    def __init__(self, teza=0, visina=0, starost=0, spol="", aktivnost=0):
        self.teza = teza
        self.visina = visina
        self.starost = starost
        self.spol = spol
        self.aktivnost = aktivnost   
    
    def bmr(self):        
        '''Izračun "basal metabolic rate"'''
        #Harris–Benedictova enačba

        if self.visina is None and self.teza is None and self.starost is None:
            return 0
        else:
            if self.spol == "M":
                bmr = ((10 * int(self.teza)) + (6.25 * int(self.visina)) - (5 * int(self.starost)) + 5)
            else:   
                bmr = ((10 * int(self.teza)) + (6.25 * int(self.visina)) - (5 * int(self.starost)) - 161)
            return bmr
     
    def vzdrzevanje(self):        
        '''Izračun potrebnih kalorij za vzdrževanje telesne teže'''
        if self.aktivnost is None:
            return 0
        else:
            return round(self.bmr() * float(self.aktivnost))
    
    def pridobitev(self):        
        '''Izračun potrebnih kalorij za pridobitev telesne teže''' 
        return round(self.vzdrzevanje() * (1 + 0.2))
    
    def izguba(self):        
        '''Izračun potrebnih kalorij za izgubo telesne teže'''
        return round(self.vzdrzevanje() * (1 - 0.2))