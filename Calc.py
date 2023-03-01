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
      print(f"The sum of {num1} and {num2} is {result}")
      return user_options()
    elif option == "2":
      num1 = user_input()
      num2 = user_input()
      result = num1 - num2
      print(f"The sum of {num1} and {num2} is {result}")
      return user_options()
    elif option == "3":
      num1 = user_input()
      num2 = user_input()
      result = num1 * num2
      print(f"The sum of {num1} and {num2} is {result}")
      return user_options()
    elif option == "3":
      num1 = user_input()
      num2 = user_input()
      if num2 == 0:
        print("Enter more than zero")
        return
      else:
        result = num1 / num2
        print(f"The divisor of {num1} ÷ {num2} is {result}")
        return user_options()
    elif option == "q":
      print("GoodBey!!!!!!!!")
      break
    else:
      print("Unknown option. try again.")
user_input()
