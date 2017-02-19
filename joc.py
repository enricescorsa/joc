# joc
joc introducció python per a nens

#proba

print('Hola!')
print('com et dius? (escriu el teu nom)')
myName=raw_input('')
print('Hola, '+myName)
print('El número de lletres que té el teu nom és:')
print(len(myName))
print('quants anys tens?')
myAge=input()
print('Molt bé. Sabies que quan hagin passat 10 anys tindràs '+str(int(myAge)+10)+' anys?')
raw_input('')
print('OK. Com veus, sé moltes coses de tu '+myName+'!')
print('Una altra pregunta: quants jocs de la play tens?')
numJocs=raw_input()
try:
    if int(numJocs)>=4:
        print ('Caram! quants jocs. Què mimat! Segur que et vicies molta estona!')
    else:
        print('què poquets! Molt bé, així no et distreus tant i estudies més')
except ValueError:
    print('això no és cap número xavalet!')
import random
print('Una altra pregunta; '+myName+', a veure si endevines un número de 1 al 20 que estic pensant...')
secretNumber=random.randint(1,20)

for guessesTaken in range(1, 7):
    print('Digues quin creus que és?')
    guess=int(input())
    if guess>secretNumber:
        print('massa gran')
    elif guess<secretNumber:
        print ('massa petit')
    else:
        break
if guess==secretNumber:
    print('Molt bé '+myName+'! Ho has endevinat en '+str(guessesTaken)+' intents.')
else:
    print('No. Ho sento, el número era '+str(secretNumber)) 


print('Adéu '+myName+'!')



