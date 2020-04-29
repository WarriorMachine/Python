class Brut:
    def __init__(self, characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789/@?!:;.,~-", min=1, max=4, infos=True):
        self.characters, self.min, self.max, self.infos = characters, min, max, infos
        if self.min > 0 or self.max > 0:
            if self.min < self.max or self.min <= self.max:
                if self.infos:
                    start_time = datetime.now()
                for n in range(self.min, self.max+1):
                    for i in itertools.product(self.characters, repeat=n):
                        chars = ''.join(i)
                        print(chars) #edit this line as you want
                if self.infos:
                    end_time = datetime.now()
                    print ('\n[BRUT] A commencer le : '+str(start_time))
                    print ('\n[BRUT] Fini le : '+str(end_time))	
                    print ('\n[BRUT] Temps total : '+str(end_time-start_time))
            else:
                print("\n[BRUT] Erreur 0002 : La valeur min doit être inférieur ou égal à la valeur max")
        else:
            print("\n[BRUT] Erreur 0001 : Les valeurs min et max doivent être suppérieur à 0")
