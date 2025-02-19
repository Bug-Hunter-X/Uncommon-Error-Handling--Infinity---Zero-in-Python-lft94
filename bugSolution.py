def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        if b == 0 and a == float('inf'):
            return float('inf')
        elif b == 0 and a == float('-inf'):
            return float('-inf')
        else:
            raise

#Corrected exception handling for infinity cases
print(function_with_uncommon_error(float('inf'), 0)) # Output: inf
print(function_with_uncommon_error(float('-inf'),0)) # Output: -inf

# Example to show the standard ZeroDivisionError handling
# try:
#     print(function_with_uncommon_error(5, 0))
# except ZeroDivisionError as e:
#     print(f"ZeroDivisionError caught: {e}") # Output: ZeroDivisionError caught: division by zero