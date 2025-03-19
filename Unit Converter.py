tasks = print("TASK CHOICES: 0: Quit, 1: Temperature(F to C), 2: Weight(lb to kg), 3: Distance(mi to km), 4: height/length(ft to m), and 5: Volume(Gal to L)")




while True:
    task = int(input("Enter Task (0-5): "))
    if task == 1:
        print("We will now convert temperature in degrees F to degrees C.")
        temp = float(input("Enter Temperature in F Here: "))
        tempC = (temp - 32) * (5/9)
        print(f"Result: {temp} degrees Fahrenheit is {tempC} degrees Celsius")
        print() 
    elif task == 2:
        print("We will now convert weight in pounds to kilograms.")
        weight = float(input("Enter Weight in lbs Here: "))
        weightkg =  weight * .454
        print(f"Result: {weight} pounds is {weightkg} kilograms")   
        print()  
    elif task == 3:
        print("We will now convert distance in miles to kilometers.")
        distance = float(input("Enter Distance in Miles Here: "))
        distancekm =  distance * 1.609
        print(f"Result: {distance} miles is {distancekm} kilometers")   
        print()      
    elif task == 4:
        print("We will now convert height/length in feet to meters.")
        length = float(input("Enter Height/Length in ft Here: "))
        lengthm =  length * .305
        print(f"Result: {length} feet is {lengthm} meters")   
        print()    
    elif task == 5:
        print("We will now convert volume in gallons to liters.")
        volume = float(input("Enter Volume in gal Here: "))
        volumel =  volume * 3.78541
        print(f"Result: {volume} gallons is {volumel} liters")   
        print()  
    elif task > 5:
        print("Invalid Input")
    elif task < 0:
        print("Invalid Input") 
    else:
        break
print("Thank you for using the Unit Converter. Have a great day!")           

