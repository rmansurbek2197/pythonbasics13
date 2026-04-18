class MatnAjratish:
    def __init__(self, matn):
        self.matn = matn
        self.unlilar = "aeiou"
        self.undoshlar = "bcdfghjklmnpqrstvwxyz"
        self.unli_harflar = []
        self.undosh_harflar = []

    def ajratish(self):
        for harf in self.matn.lower():
            if harf in self.unlilar:
                self.unli_harflar.append(harf)
            elif harf in self.undoshlar:
                self.undosh_harflar.append(harf)

    def chiqarish(self):
        print("Unli harflar: ", self.unli_harflar)
        print("Undosh harflar: ", self.undosh_harflar)


matn = input("Matn kiriting: ")
dastur = MatnAjratish(matn)
dastur.ajratish()
dastur.chiqarish()