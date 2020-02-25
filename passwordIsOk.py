

def encoding(password):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    decimal = "0123456789"
    special_chr = "~!@#$%^&*()_+"
    key = "pokemon_go"
    cipher = ''
    pwd = ''
    secret_key = '1'
    for k in key:
        secret_k = ord(k)
        secret_key = int(secret_key) + secret_k
    for c in password:
        if c in alpha:
            cipher += alpha[(alpha.index(c)+secret_key)%(len(alpha))]

        elif c in decimal:
            cipher += decimal[(decimal.index(c)+secret_key)%(len(decimal))]

        elif c in special_chr:
            cipher += special_chr[(special_chr.index(c)+secret_key)%(len(special_chr))]
    return cipher

def decoding(c):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    decimal = "0123456789"
    special_chr = "~!@#$%^&*()_+"
    key = "pokemon_go"
    cipher = ''
    pwd = ''
    secret_key = '1'
    for k in key:
        secret_k = ord(k)
        secret_key = int(secret_key) + secret_k
    if c in alpha:
        pwd += alpha[(alpha.index(c)-secret_key)%(len(alpha))]

    elif c in decimal:
        pwd += decimal[(decimal.index(c)-secret_key)%(len(decimal))]


    elif c in special_chr:
        pwd += special_chr[(special_chr.index(c)-secret_key)%(len(special_chr))]

    return pwd

def pwCheck(user_information):
    data = ''
    comma_count = 1
    for info in user_information:
        if info == ',' and comma_count == 1 :
            comma_count += 1
            user_name = data
            data = ''
            continue

        elif info == ',' and comma_count == 2 :
            comma_count += 1
            encoded_password = data
            data = ''
            continue
        data = data + info
    return (user_name,encoded_password,data)



count = 0

while count != 3:
    if count == 0:
        userinfo_1 = input("Please enter your Username,Encoded Password,Account Balance by Comma Seperated: ")
        result_1 = pwCheck(userinfo_1)

    elif count == 1:
        userinfo_2 = input("Please enter your Username,Encoded Password,Account Balance : ")
        result_2 = pwCheck(userinfo_2)
    elif count == 2:
        userinfo_3 = input("Please enter your Username,Encoded Password,Account Balance : ")
        result_3 = pwCheck(userinfo_3)
        
    count += 1

user_count = 0

while user_count != 3:
    username_real = input("Please enter your Username :")
    password_real = str(input("Please enter your password :"))
    string_length = int(len(password_real))

    if string_length < 10 :
        print("\n***The password you have entered should must be at least 10 characters long")

    else:
        characters = 0
        upper_count = 0
        decimal_count = 0
        special_count = 0
        space_count = 0
    
        temp_password = encoding(password_real)
        while characters != string_length :
            password = decoding(temp_password[characters:characters + 1])
            if password.isupper() :
                upper_count += 1

            elif password.isdecimal() :
                decimal_count += 1

            elif  set('#$%&*').intersection(password):
                special_count += 1

            elif password.isspace() :
                space_count += 1
                break

            characters += 1

        if ( upper_count == 0 or decimal_count == 0 or special_count == 0):
            if ( upper_count == 0):
                print("***Your password must contain at least one Uppercase letter." )

            if ( decimal_count == 0):
                print("***Your password must contain at least one decimal." )

            if (special_count == 0):
                print("***Your password must contain at least one Special Character from # $ % *." )

            if (space_count == 1):
                print("***Your password must not contain any spaces")

        else:
            if username_real == result_1[0] and password_real == result_1[1]:
                print("The balance in " + result_1[0] + " account is " + result_1[2])
                user_count += 1
            elif username_real == result_2[0] and password_real == result_2[1]:
                print("The balance in " + result_2[0] + " account is " + result_2[2])
                user_count += 1
            elif username_real == result_3[0] and password_real == result_3[1]:
                print("Hello " + result_3[0] +", Welcome to Online Banking ")
                print("The balance in " + result_3[0] + " account is " + result_3[2])
                user_count += 1
            else:
                print("Sorry Sir your Username and/or password does not match with our directory")
         

print("Goodbye you need to login once again due timed out")
