def Brut(characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789/@?!:;.,~-", min=1, max=4, lenght_bar=50): #71
    total = 0
    for p in range(1, max+1-min+1):
        total =+ (len(characters)**p)

    count, progress = 0, 1
    for n in range(min, max+1):
        for i in itertools.product(characters, repeat=n):
            chars, count = ''.join(i), count + 1
            print(f"\r[{'▒'*progress}{' '*(lenght_bar-progress)}] | {round(progress/(lenght_bar+1)*100)}% | Try: {chars} |", flush=True, end='')
            #process
            if count == round(total/lenght_bar)-1:
                count, progress = 0, progress + 1
    print("\nDone")
