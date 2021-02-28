from typing import Tuple
#tuple cwiczenia
Group=('tech','Pro', 'comfort')
print(Group)
tup1=('Techpro','compsoft', 123,456);
tup2=(1,2,3,4,5,6,7);
print(tup2)
Tuple=(tup1+tup2)
print(Tuple)
print('tup1[0]:', tup1[0]);
print('tup1[2]:', tup1[2]);
print('tup1[-1]:', tup1[-1]);
print('tup2[1:5]:', tup2[1:5]);
# nadpisanie tupli tworzy sie nowa tupla
tup1=(1,2)
print(tup1)
#usowanie z tupli danych.
tup3=('techpro', 200)
print('tup3 :', tup3)
del tup3
#tuple funkcje
print("jest tyle elementow",len(tup2))
print("najwyzsza wartosc w tupli",max(tup2))
print("najniższa wartosc w tupli",min(tup2))
