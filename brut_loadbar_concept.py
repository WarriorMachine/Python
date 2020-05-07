class Brut:
    def __init__(self, characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789/@?!:;.,~-", min=1, max=4, lenght_bar=50): #71
        self.characters, self.min, self.max, self.lenght_bar = characters, min, max, lenght_bar
        total = 0
        for p in range(1, max+1-min+1):
            total = total + (len(characters)**p)

        sys.stdout.write("Loading : |%s|" % (" " * lenght_bar))
        sys.stdout.flush()
        sys.stdout.write("\b" * (lenght_bar+1))

        count = 0
        for n in range(self.min, self.max+1):
            for i in itertools.product(self.characters, repeat=n):
                chars = ''.join(i)
                count += 1
                #process
                if count == round(total/lenght_bar)-1:
                    sys.stdout.write("▒")
                    sys.stdout.flush()
                    count = 0
        sys.stdout.write("| 100%")
        sys.stdout.write("\nDone")
