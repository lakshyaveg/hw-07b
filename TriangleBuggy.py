
def classifyTriangle(a,b,c):

    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= b or c <= 0:
        return 'InvalidInput'
    
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput';
      
    if (a >= (b - c)) or (b >= (a - c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == a:
        return 'Equilateral'
    elif ((a * 2) + (b * 2)) == (c * 2):
        return 'Right'
    elif (a != b) and  (b != c) and (a != b):
        return 'Scalene'
    else:
        return 'Isoceles'
