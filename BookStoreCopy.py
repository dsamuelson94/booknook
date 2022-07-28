print('''
                .-~~~~~~~~~-._       _.-~~~~~~~~~-.
            __.'              ~.   .~              `.__
          .'//                  \./                  \\`.
        .'//                     |                     \\`.
      .'// .-~"""""""~~~~-._     |     _,-~~~~"""""""~-. \\`.     
    .'//.-"                 `-.  |  .-'                 "-.\\`.
  .'//______.============-..   \ | /   ..-============.______\\`.
.'______________________________\|/______________________________`.
''')
print("Welcome to the Book Nook!")
print("What will be your next great read?") 

q_1 = input("Do you want to read fiction or nonfiction? ").lower()
if q_1 == "nonfiction":
  print("Your next great read will be Mindhunter by John E. Douglas!")
else:
  q_2 = input("Do you prefer historial fiction or fantasy? ").lower()
  if q_2 == "historical fiction":
    print("Your next great read will be The Memoirs of Cleopatra by Margaret George!")
  else:
    q_3 = input("Do you want your book to be long or short? ").lower()
    if q_3 == "short":
      print("Your next great read will be A Wizard of Earthsea by Ursula K. Le Guin!")
    else:
      print("Your next great read will be The Lord of the Rings trilogy by J. R. R. Tolkien!")