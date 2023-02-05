x = input("Welcome to Caesar Cipher. What would you like to do? (Encode/Decode) ")
if x.lower() == "encode":
    try:
        inpe = input("What do you want to encode? ")
        keye = int(input("What key would you like to use? "))
        encoded_str = ""
        for i in inpe:
            while keye > 26:
                keye -= 26
            while keye < 0:
                print("Key should be in positive integers")
                keye = int(input("What key would you like to use? "))
            if ord(i) == 32: # Space character
                encoded_str += i
            elif i.isalpha():
                encoded_ascii = ord(i) + keye
                if i.islower() and encoded_ascii > 122:
                    encoded_ascii -= 26
                elif i.isupper() and encoded_ascii > 90:
                    encoded_ascii -= 26
                encoded_str += chr(encoded_ascii)
            else:
                encoded_str += i
        print(encoded_str)
    except ValueError:
        print("Key must be a number.")
elif x.lower() == "decode":
    try:
        inpd = input("What would you like to decode? ")
        keyd = int(input("What key would you like to use? "))
        decoded_str = ""
        for j in inpd:
            while keyd > 26:
                keyd -= 26
            while keyd < 0:
                print("Key should be in positive integers")
                keyd = int(input("What key would you like to use? "))
            if ord(j) == 32: # Space character
                decoded_str += j
            elif j.isalpha():
                decoded_ascii = ord(j) - keyd
                if j.islower() and decoded_ascii < 97:
                    decoded_ascii += 26
                elif j.isupper() and decoded_ascii < 65:
                    decoded_ascii += 26
                decoded_str += chr(decoded_ascii)
            else:
                decoded_str += j
        print(decoded_str)
    except ValueError:
        print("Key must be a number.")
else:
    print("You can only respond with 'Encode' or 'Decode'.")
