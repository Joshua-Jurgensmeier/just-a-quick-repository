from getpass import getpass
from time import sleep
ATTEMPTS_BETWEEN_LOCKOUT = 3

pin = 12345

entry = 0

incorrect_entries = 0
entry_correct = False

while not entry_correct:
    
    # You know users these days, you can always trust their input!
    entry = int(getpass(prompt="Enter your 5 digit pin!:"))

    if entry == pin:
        entry_correct = True
    
    else:

        incorrect_entries += 1
        
        if incorrect_entries < 3:  
            print("Incorrect entry.  Please try again.")
            print("{0} incorrect entry(ies).  Program will lockout after 3.\n".format(incorrect_entries))
        
        else:
            print("Stop hacking! (For 10 seconds.)")
            sleep(10)
            incorrect_entries = 0

print("Congratulations!")
