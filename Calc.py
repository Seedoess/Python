def user_input():
  while True:
    num = input("enter a number: ")
    try:
      num = float(num)
      break
    except:
      print("Enter a number!!!")
  return num

def user_options():
  while True:
    print("""
1. ===> add        
2. ===> sub     
3. ===> multiplication        
4. ===> division 
q. ===> quit 
          """)
    option = input("Enter a option 1 - 4 or 'q' to quit: ")
    if option == "1":
      num1 = user_input()
      num2 = user_input()
      result = num1 + num2
      print(f"Sum of {num1} and {num2} is ===================> {result}")
      continue
    elif option == "2":
      num1 = user_input()
      num2 = user_input()
      result = num1 - num2
      print(f"Diffrens of {num1} and {num2} is ===================> {result}")
      continue
    elif option == "3":
      num1 = user_input()
      num2 = user_input()
      result = num1 * num2
      print(f"{num1}'s are {num2} is ===================> {result}")
      continue
    elif option == "4":
      num1 = user_input()
      while True:
        num2 = user_input()
        if num2 == 0:
          print("Enter more than zero")
        else:
          break
      result = num1 / num2
      print(f"division of {num1} ÷ {num2} is ===================> {result}")
      continue
    elif option == "q":
      print("GoodBey!!!!!!!!")
      break
    else:
      print("Unknown option. try again.")
user_options()
