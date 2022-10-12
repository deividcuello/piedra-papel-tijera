import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

# Pedirle al usuario que seleccione una opcion
user_choice = int(input("Qué eliges? 0 para piedra, 1 para papel y 2 para tijera: "))
print(game_images[user_choice])

#Seleccionamos una opcion aleatoria por la computadora
computer_choice = random.randint(0,2)
#imprimir la opción de la computadora
print("La computadora eligió: ")
print(game_images[computer_choice])

#Determinar quien gana y mostrar al usuario

print(user_choice, computer_choice)

if user_choice == computer_choice:
    print('Empate')
elif user_choice == 0 and computer_choice == 1:
    print('Gana computadora')
elif user_choice == 0 and computer_choice == 2:
    print('Gana usuario')
elif user_choice == 1 and computer_choice == 0:
    print('Gana usuario')
elif user_choice == 1 and computer_choice == 2:
    print('Gana computadora')
elif user_choice == 2 and computer_choice == 0:
    print('Gana computadora')
elif user_choice == 2 and computer_choice == 1:
    print('Gana usuario')