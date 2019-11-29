### 1. Implementirtaj class, ki predstavlja krog. 
Naj ima dve metodi (poleg ostalih potrebnih):
  - area() -> vrne povrsino kroga
  - circumference() -> vrne obseg kroga

Uporaba:
```python
c = Circle(r=10)
c.area()
c.circumference()
```
Namigi:
```python
from math import pi
```


### 2. Implementiraj class, ki predstavlja igričarski karakter in podpira nekaj akcij
Class naj ima sledeče metode (poleg ostalih potrebnih):
- do_attack(player_obj) -> če player_obj ni isti igralec, izvedi napad (napadenemu igralcu se naj spremeni health za vrednost napada)
- is_alive() -> je igralec še živ?

health - zdravje karakterja

attack - maximalen možni napad (ko karakter napade povzroči med 0 in attack škode)

Uporaba:
```python
player_1 = Player(name="Steve", health=100, attack=10)
player_2 = Player(name="Jebediah", health=100, attack=5)

# Izvedi napad
player_1.do_attack(player_2)
print(player_1)
print(player_2)

player_2.do_attack(player_1)
print(player_1)
print(player_2)
```

### 3. Implementiraj class Localize, ki zna glede na parameter pravilno pretvarjati dolžine
Class naj ima sledečo metodo (poleg ostalih potrebnih):
   - loc("location") -> vrne podatek v pravilnih enotah glede na lokacijo
   
Uporaba:
```python
height = Localize(2, "m")  # podpiramo samo metre (m) in feete (ft)

print(height.loc("SLO"))  # izpiše podatek v metrih 
print(height.loc("GB"))  # izpiše podatek v feetih
```

### 4. Implementiraj class Loan (posojilo)
Pri inicializaciji naj sprejme vsoto posojila in dobo odplačevanja v mesecih (obresti ni)

- owed_amount(<month_num>) -> vrne koliko smo še dolžni. 
  - Brez parametra - celoten znesek
  - S parametrom - znesek ki ostane če odplačujemo že toliko mesecev
  
Uporaba:
```python
kredit = Loan(100000, 120)
print(kredit.owed_amount())     # Izpiše celoten znesek kredita
print(kredit.owed_amount(100))  # Izpiše znesek, ki nam ostane če odplačujemo 100 mesecev
```

 