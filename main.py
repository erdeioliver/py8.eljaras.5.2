'''
5.2 Feladat
A program, egy eljárás segítségével kirajzol a képernyőre egy 6x3-as mezőt. Alakítsd át ezt a programot úgy, az eljárás hívásakor megadott értékpárnak megfelelően a program az adott pozícióba 'O' helyett '+' jelet írjon ki. A lenti példában az eljárás hivása: mezot_rajzol(0,4)

    O O O O + O
    O O O O O O
    O O O O O O

Feladat
Alakítsd át az előző programot úgy, hogy a felhasználó adhassa meg a koordinátákat, ahová a program 'O' helyett '+' jelet ír. A koordináták bekérése és a mező kirajzolása addig ismétlődjön, amíg a felhasználó negatív számot nem ad meg koordinátaként!
'''
def mezot_rajzol(x, y):
    x += 1
    szamlalo = 0
    szamlalo2 = 0
    for sor in range(3):
        szamlalo += 1
        szamlalo2 = 0
        for oszlop in range(6):
            if szamlalo == x and szamlalo2 == y:
                print('+ ', end='')
            elif szamlalo != x or szamlalo2 != y:
                print('O ', end='')
            szamlalo2 += 1
        print()

while True:
    szam1 = int(input("Adjon meg egy koordinátát! "))
    szam2 = int(input("Adjon meg egy másik koordinátát! "))
    if szam1 < 0 or szam2 < 0:
        break
    bekeres = mezot_rajzol(szam1, szam2)
