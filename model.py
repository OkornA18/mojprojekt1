class Kalorije():
    
    def __init__(self, teza, visina, starost, spol):
        self.teza = teza
        self.visina = visina
        self.starost = starost
        self.spol = spol
    
    def bmr(self, spol):        
        '''Izračun "basal metabolic rate"'''
        
        #Harris–Benedictova enačba
        if spol == "M":
            bmr = ((10*self.teza) + (6.25*self.visina) - (5*self.starost) + 5)
        else:   
            bmr = ((10*self.teza) + (6.25*self.visina) - (5*self.starost) - 161)
        return bmr
     
    def vzdrzevanje(self, act_mult = 1.4):        
        '''Izračun potrebnih kalorij za vzdrževanje telesne teže'''
        
        return round(self.bmr(self.spol)*act_mult)
    
    def pridobitev(self, percentage = 0.2, act_mult = 1.4):        
        '''Izračun potrebnih kalorij za pridobitev telesne teže''' 
        
        return round(self.vzdrzevanje(act_mult = act_mult)*(1+percentage))
    
    def izguba(self, percentage = 0.2, act_mult = 1.4):        
        '''Izračun potrebnih kalorij za izgubo telesne teže'''
        
        return round(self.vzdrzevanje(act_mult = act_mult)*(1-percentage))
    
    def proteinski_vnos(self, teza, mult = 2.2):       
        
        return round(self.teza*mult)