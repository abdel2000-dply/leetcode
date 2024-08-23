'''
592. Fraction Addition and Subtraction

Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.
'''
class Solution:
    def fractionAddition(self, expression: str) -> str:
        arr = []
        temp = ''
        i, n = 0, len(expression)
        
        while i < n:
            if expression[i] in '+-':  
                if temp:
                    arr.append(temp)
                temp = expression[i]
            else:
                temp += expression[i]
            i += 1
        
        arr.append(temp)

        numerator, denominator = 0, 1

        for frac in arr:
            if not frac:
                continue  # Skip any empty strings
            
            num, denom = map(int, frac.split('/'))
            
            numerator = numerator * denom + num * denominator
            denominator *= denom
            
            common_gcd = gcd(abs(numerator), denominator)
            numerator //= common_gcd
            denominator //= common_gcd
        
        return f"{numerator}/{denominator}"
