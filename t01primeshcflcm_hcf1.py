# Find the Highest Common Factor (HCF) of 18 and 30.

 if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
            
    return hcf
  
  num1 = 18
  num2 = 30
