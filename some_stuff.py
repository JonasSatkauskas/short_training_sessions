

class Augintinis:
    def __init__(self, vardas, tipas, amzius):
        self.vardas = vardas
        self.tipas = tipas
        self.amzius = amzius


    def help(self):
        info = f"""Yra tokios galimos komandos:\n
                   informacija  -   parodo pagrindinę informaciją apie jūsų augintinį
                   sedet    -   jūsų augintinis atsisėda"""
        
        print(info)


    def informacija(self, vardas):
        bendra = f'''Duomenys apie jūsų augintinį:\n
                     [+] Vardas: {self.vardas}\n
                     [+] Tipas: {self.tipas}\n
                     [+] Amžius: {self.amzius}'''
        
        print(bendra)

    def sedet(self, vardas):
        print(f'{self.vardas} atsisėdo.')



augintinis1 = Augintinis('Bilis', 'Šuo', '4 metai')
print()
augintinis1.help()
augintinis1.informacija('Bilis')
augintinis1.sedet('Bilis')