class Brut:
    def __init__(self, characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789/@?!:;.,~-", min=1, max=4, infos=1):
        if infos==1:
            start_time = datetime.now()
            print ('[BRUT] Commence le : '+str(start_time))
            time.sleep(1)
        for n in range(min, max+1):
            for i in itertools.product(characters, repeat=n):
                chars = ''.join(i)
                print(chars)
        if infos==1:
            end_time = datetime.now()
            print ('\n[BRUT] Fini le : '+str(end_time))	
            print ('\n[BRUT] Temps total : '+str((end_time - start_time)-1))
            time.sleep(10)
