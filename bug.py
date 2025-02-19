def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        # This is the common handling, but let's add an uncommon scenario
        if b == 0 and a == float('inf'):
            return float('inf')  #infinity divided by zero is infinity
        elif b == 0 and a == float('-inf'):
            return float('-inf') # -infinity divided by zero is -infinity
        else:
            raise

# This may raise an exception
print(function_with_uncommon_error(float('inf'), 0))

# This will raise an exception
print(function_with_uncommon_error(5, 0))