def Brut(characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789/@?!:;.,~-", min=1, max=4):
    if min >= 0 or max > 0:
        if min <= max:
            for n in range(min, max+1):
                for i in itertools.product(characters, repeat=n):
                    chars = ''.join(i)
                    print(chars) #edit this line as you want
