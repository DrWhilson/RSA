import random
import math
    
def isPrimeMillerRabin(mrc):
    max_divisions_by_two = 0
    ec = mrc-1
    while ec % 2 == 0: 
        ec >>= 1
        max_divisions_by_two += 1

    def trialComposite(round_tester): 
        if pow(round_tester, ec, mrc) == 1: 
            return False
        for i in range(max_divisions_by_two): 
            if pow(round_tester, 2**i * ec, mrc) == mrc-1: 
                return False
        return True

    trials_amount = 20 
    for i in range(trials_amount): 
        round_tester = random.randrange(2, mrc) 
        if trialComposite(round_tester): 
            return False
    return True

def GeneratePrime(start, end):
    while True:
        Number = random.randint(start, end)
        if isPrimeMillerRabin(Number):
            return Number    
    return -1

def gcdExtended(a, b):  
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcdExtended(b, int(a) % b)
        return d, y, x - y * (int(a) // b)

def multInvMod(num, mod):
    gcd,x,y = gcdExtended(num, mod)
    if x > 0:
        return x
    else:
        return mod+x

def GenerateDotInStringWithParam(start, end, N):
    while True:
        n = random.randint(start,end)
        if n < N:
            return n
    return -1

def CutText (Text, start, end):
    newText = Text
    while True:
        if start == end:
            return newText
        newText[start] = Text[start]
        start = start + 1

def RaisingArrayPowerModulo (Mass, power, N):
    i = 0
    while True:
        if i == len(Mass):
            return Mass
        Mass[i] = pow(Mass[i], power, N)
        i = i + 1

Text = input("Пользователь А вводит сообщение: ")

#Преобразование сообщения в числа
Text = Text.lower()
Num_Text = []
for character in Text:
    number = ord(character)
    Num_Text.append(number)

#Количество знаков в произведении простых чисел
Power = 30

#Генерируем количество знаков в 2х просых числах
PowerP = random.randint(1,Power)
PowerQ = Power - PowerP;

#Генерируем простые числа
P = GeneratePrime(10**PowerP // 10, (10**PowerP) - 1)
Q = GeneratePrime(10**PowerQ // 10, (10**PowerQ) - 1)

N = P * Q
d = (P-1)*(Q-1)


while True:
    s = input("Пользователь Б вводит открытый ключ: ")
    s = int(s)
    if math.gcd(s,d) == 1:
        break
    else:
       print("Некоректно введённый ключ. Ключ не должен иметь общих делителей с d, попробуйте ещё раз.")

e = multInvMod(s, d)

#Каждый сивол шифруем
c = RaisingArrayPowerModulo(Num_Text,s,N)

print("Передаётся зашифрованное сообщение: ")
print(c)

#Дешифруем каждый символ
m = RaisingArrayPowerModulo(c,e,N)

#Переводим числа в символы
Out_Text = []
for number in m:
    character = chr(number)
    Out_Text.append(character)

print("Пользователь Б получает сообщение: ")
print(Out_Text)