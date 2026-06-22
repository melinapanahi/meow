print("Hej!Jag är en bot som ska hjälpa dig skapa en todo list.")
def visa_lista(todo_lista): #Funktionen är till för att visa de olika elementen i listan.
    for element in todo_lista: # for-loop går igenom listans element. 
        print("Uppgift:", element[0])
        print("Prioritet:", element[1])
        print("Status:", element[2])
        print()
todo_lista = []  #tom lista i vilken användaren kan lägga till element. 
while True: #while-loop för att programmet ska fortsätta fråga användaren. 
    print("\n--- TO DO LIST ---") #menyval
    print("1. Lägg till uppgift och ange prioriteringsgraden för det")
    print("2. Markera slutförd uppgift")
    print("3. Visa listan")
    print("4. Ta bort uppgift")
    print("5. Avsluta")
    val = input("Välj ett alternativ: ") #Här får användaren lägga till alternativ
    if val == "1": # Om användaren väljer nummer 1 så kommer följande hända. 
        uppgift = input("skriv en uppgift:")
        prio = input("Välj prioriteringsgrad för din uppgift, H/M/L  ")
        todo_lista.append([uppgift,prio,"Ej klar"]) #Här samlas uppgiftens namn ,prioritet och status som en gemensam punkt i listan
    elif val == "2":
        uppgift = input("Vilken uppgift är klar? ")
        for element in todo_lista: #Den här raden kommer att gå igenom varje uppgifts beståndsdelar 
            if element[0] == uppgift: #Den här raden identifierar den uppgift vars status ska ändras för programmet
                element[2] = "Klar" #Om ovanstående rad är sann, ändras uppgiftens status här
                print("Uppgiften markerad som klar!")
    elif val == "3":
        visa_lista(todo_lista) #Här anropas den funktion som inleder programmet
    elif val == "4":
        uppgift = input("Skriv vilken uppgift du vill ta bort: ") 
        for element in todo_lista:
            if element[0] == uppgift:
                todo_lista.remove(element) #Här kan uppgift tas bort
                print("Uppgiften är borttagen!")
    elif val == "5":
        print("Programmet avslutas! Tack för den här gången!") 
        break #Programmet avslutas
    else:
        print("Ogiltigt val! Välj ett alternativ mellan 1-5") #Om användaren anger ett nummer förutom 1-5 så skrivs denna rad ut.
