#Celcius <-> Fahrenheit <-> Kelvin
#start
user_input = input("°C = 1 | °F = 2 |°K = 3 : ") #User input


if user_input == "1":
    Celcius = int(input("Enter Fahrenheit: "))      #celcius to fahrenheit
    print(int(Celcius-32) * 5 / 9)

elif user_input == "2":
    Fahrenheit = input("Enter Celcius: ")           #fahrenheit to celcius
    print((int(Fahrenheit) * 9 / 5) + 32)

elif user_input == "3":
    
    user_input_K = input("°C & °F to °K = 1  | °K to °C & °F = 2 : ")   #2nd user input

    if user_input_K == "1":
        type = input("°C to °K = 1 | °F to °K = 2 : ")      #3rd user input
        if type == "1":
            kelvin = int(input("Enter Celcius: "))    #celcius to kelvin
            print(int((kelvin/5)*5)+273.15)

        elif type == "2":
            kelvin = int(input("Enter Fahrenheit: "))   #fahrenheit to kelvin
            print(int(kelvin-32) * 5 / 9 + 273.15)

        else:
            print("Invalid input")  #404 error
    elif user_input_K == "2":
        type_K = input("°K to °C = 1 | °K to °F = 2 : ")    #4th user input

        if type_K == "1":
            kelvin = int(float((input("Enter Kelvin: "))))  #kelvin to celcius
            print(int(kelvin-273.15))

        elif type_K == "2":
            kelvin = int(float(input("Enter Kelvin: ")))    #kelvin to fahrenheit
            print(int((kelvin-273.15)/5*9)+32) 
        else:
            print("Invalid input")  #404 error
else:
    print("Invalid input")  #404 error

#end