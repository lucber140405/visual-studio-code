
import random

question = input('¿que quieres preguntarle a la bola mágica?: ')

numero = random.randint(1, 9)
# print(random_number)

if numero == 1:
  answer = 'si, definitivamente'
elif numero== 2:
  answer = 'Esta decidido que si'
elif numero== 3:
  answer = 'sin duda'
elif numero == 4:
  answer = 'dificil respuesta, pregunta de nuevo'
elif numero == 5:
  answer = 'pregunta más tarde'
elif numero == 6:
  answer = 'mejor te lo digo en otro momento'
elif numero == 7:
  answer = 'mi subsconsciente dice no'
elif numero == 8:
  answer = 'no se ve muy claro'
elif numero == 9:
  answer = 'muy dudos'
else:
  answer = 'Error'
  
print('¿que quieres preguntarle a la bola mágica?:      ' + question)
print('La bola mágica dice:  ' + answer)
