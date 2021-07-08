monthRunning = True 


def handleInput(): 
    valid = True 

    monthsNumbers = {
        1 : 'January',
        2 : 'February',
        3 : 'March',
        4 : 'April',
        5 : 'May',
        6 : 'June',
        7 : 'July',
        8 : 'August', 
        9 : 'September',
        10 : 'October',
        11 : 'November',
        12 : 'December'
    }

    selection = int(input("Enter a number 1-12 to get its corresponding month: "))
    
    if selection in monthsNumbers:
        print ( monthsNumbers[selection])
    else: 
        print("Invalid choice, try again.")
        valid = False 


def monthSelector():
    while monthRunning: 
        handleInput() 

monthSelector() 
   
   
  

 