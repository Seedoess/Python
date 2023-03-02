import random
import string

def genarate_otp():
    num = (string.digits)
    num_list = list(num)
    random.shuffle(num_list)
    otp = ''.join(num_list[:4])
    print(otp)
    return otp

def verify_otp():
    otp = genarate_otp()
    while True:
        v_otp = input("Enter otp: ")
        if v_otp == otp:
            print('verifyed!!!!!!')
            break
        else:
            print("wrong otp enter again!!!!!")
verify_otp()
