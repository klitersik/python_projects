# zawartosci rejestrow
print("Instrukcje powinny znajdować się każda w innej lini, Przykłady instrukcji S(2) T(3,1) Z(7) J(1,2,6)")
print("wartosci powinny byc oddzielone znakiem przecinka ")
r = []
# dodaje 0 na poczatku aby indexy sie zgadzaly
r.append(0)
# tablica instrukcji
instrukcje = []
# dodaje 0 na poczatku aby indexy sie zgadzaly
instrukcje.append('0')
# otwarcie pliku
f = open("test.txt", "r")
#print(f.read())
# dodanie dotatkowych rejestów w sposob nie optymalny
max_index = 0
# petla po wszystkich liniach w pliku
for i in f:
    instrukcje.append(i)
    if int(i[2]) > max_index:
        max_index = int(i[2])
# pobieramy ciag od uzytkownika
tmp = input("podaj ciag wartości: ")
#dzielimy wzgledem ,
x = tmp.split(",")
# domyslnie kazy input jest stringiem wiec kazdy znak zamieniam na liczbe i dodaje na koniec wartosci
r = r + x
# dodajemy troche indexow
for m in range(max_index):
    r.append(0)
# zmieniamy str na int
r = [ int(x) for x in r ]
k = 1
while True :
    if instrukcje[k][0] == 'J':
        if r[int(instrukcje[k][2])] == r[int(instrukcje[k][4])]:
            k = int(instrukcje[k][6])
        else:
            k = k + 1
    elif instrukcje[k][0] == 'S':
        if int(instrukcje[k][2])-1 > len(r):
            for l in range(len(r)-(int(instrukcje[k][2])-1)):
                r.append(0)
        r[int(instrukcje[k][2])] += 1
        k += 1 
    elif instrukcje[k][0] == 'Z':
        r[int(instrukcje[k][2])] == 0
        k += 1
    elif instrukcje[k][0] == 'T':
        r[int(instrukcje[k][4])]= r[int(instrukcje[k][2])]
        k += 1
    if k > len(instrukcje)-1:
        break
print(r[1])
