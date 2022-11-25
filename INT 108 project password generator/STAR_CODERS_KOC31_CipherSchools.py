import random
chars = "`1234567890-=~!@#$%^&*()_+qwertyuiop[]\\QWERTYUIOP{}|asdfghjkl;'ASDFGHJKL:zxcvbnm,./ZXCVBNM<>?"
while True:
    password_len = int(12)
    password_count = int(input("How many passwords would you like : "))
    for x in range(0, password_count):
        password = "  "
        for y in range(0, password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Here is your password : ", password)
    repeat = input("Do you want to genarate more passwards?  ")
    if repeat == "no" or "No":
        break
print("Thank you")
