class MusicalInstrument : #class
    def __init__ (self,name,instrument_type): #initializer method
        self.name=name
        self.instrument_type=instrument_type
    def play(self):
        print(f'The {self.name} is fun to play!')
    def get_fact(self):
        return f'The {self.name} is part of the {self.instrument_type} family of instruments.'

instrument_1 = MusicalInstrument('Oboe','woodwind')   
instrument_2 = MusicalInstrument('Trumpet','brass')
print(instrument_1.name)
print(instrument_1.instrument_type)
print(instrument_2.name)
print(instrument_2.instrument_type)
instrument_1.play()
instrument_2.play()
print(instrument_1.get_fact())
print(instrument_2.get_fact())