def generatorKrasovychJezerCR():
    yield "Chalupské jezírko"
    #kdyz tady dame stopiteration tak vypise error
    yield "Velké mechové jezírko"
    yield "Jezírko pod Táborem"
    yield "Malé mechové jezírko"
    yield "Rosička"
    #raise StopIteration() #bez raise nebude error

print("Krasjova jezera v CR")
jezera = generatorKrasovychJezerCR()
s = 0
while s != 5:
    #print(next(jezera))
    s = s+1

def generatorITVelikanu():
    yield "Steve Jobs"
    yield "Bill Gates"
    yield "Lawrence Joseph Ellison"

print("Velikani v IT")
for osoba in generatorITVelikanu():
   # print(osoba)

    def generatorSudychCisel(od, do):
        i = od
        while(i < do):
            if(i%2 == 0):
                yield i
                i=i+1
            else:
                i=i+1

#for x in generatorSudychCisel(1,50):
    #print(x)

class GeneratorKrasovychJezer():
    
    i = 0

    jezera = [
    ["Dyje", ["Křivé jezero","Květné jezero","Kutnar","Mahenovo jezero"]],
    ["Labe", ["Babinecká tůň","Hrbáčkovy tůně"]],
    ["Bílina", ["Komořanské jezero"]],
    ["(bez řeky)", ["Antošovické jezero", "Holásecká jezera","Krňák","Kurfürstovo rameno","Malá říčka","Podhradská tůň"]]
]
 
    def __iter__(self):
        self.i = 0;
        return self
    
    def __next__(self):
        for x in range(len(self.jezera)):    
            for y in range(len(self.jezera[x])):
             for z in range(len(self.jezera[x][y])):
                if len(str(self.jezera[x][y][z])) == 1:
                    something = "?"
                else:
                    print(str(self.jezera[x][y][z])+" (" + str(self.jezera[x][0]) + ")")
    
        
        pomocnaPromenna = self.jezera[self.i]
        self.i = self.i + 1
        return pomocnaPromenna

        for jezero in GeneratorKrasovychJezer():
            print(jezero)

