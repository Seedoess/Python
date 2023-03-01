def user_input():
  while True:
    num = input("enter a number")
    try:
      num = int(num)
      break
    except:
      print("Enter a number!!!")
    return num
