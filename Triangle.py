def classifyTriangle(a, b, c):
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    if a + b <= c or a + c <= b or b + c <= a:
        return 'NotATriangle'
    x, y, z = sorted([a, b, c])
    if a == b == c:
        return 'Equilateral'
    if x*x + y*y == z*z:
        return 'Right'
    if a == b or b == c or a == c:
        return 'Isosceles'
    return 'Scalene'
