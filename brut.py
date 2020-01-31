class Brut:
    def __init__(self, characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/@?!:;.,~-", min=1, max=4, infos=1, wait_info=1):
        if min > 0 or max > 0:
            if min < max or min <= max:
                if infos==1:
                    start_time = datetime.now()
                for n in range(min, max+1):
                    for i in itertools.product(characters, repeat=n):
                        chars = ''.join(i)
                        print(chars)
                if infos==1:
                    end_time = datetime.now()
                    print ('\n[BRUT] A commencer le : '+str(start_time))
                    print ('\n[BRUT] Fini le : '+str(end_time))	
                    print ('\n[BRUT] Temps total : '+str(end_time-start_time))
                    if wait_info == 1:
                        time.sleep(10)
            else:
                print("\n[BRUT] Erreur 0002 : La valeur min doit être inférieur ou égal à la valeur max")
        else:
            print("\n[BRUT] Erreur 0001 : Les valeurs min et max doivent être suppérieur à 0")
