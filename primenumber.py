 
first = int(input ("first value "))  
last = int(input ("last value"))  
  
 
for number in range (first, last + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  
            
