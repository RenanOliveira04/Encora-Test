def makeChange(n):
    
    ways = set()

    
    for quarters in range(0, n // 25 + 1):
        
        for dimes in range(0, n // 10 + 1):
           
            for nickels in range(0, n // 5 + 1):
                
                pennies = n - quarters * 25 - dimes * 10 - nickels * 5

                
                if 0 <= pennies <= 11:
                    ways.add((quarters, dimes, nickels, pennies))

    
    return ways