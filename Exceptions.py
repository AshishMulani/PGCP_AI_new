import sys
import traceback as tb

try:
    dividend=int(input('Enter Dividend: '))
    divisor=int(input('Enter Divisor: '))
    result=dividend/divisor
    print(result)
except ZeroDivisionError as err:
    print(f'{err}: Divisor cannot be zero')
    e_type,e_cause,tb=sys.exc_info()
    # print class and message for an error object
    print(f'{e_type},{e_cause}')
    # Enter Dividend: 0
    # Enter Divisor: 0
    # division by zero: Divisor cannot be zero
    # <class 'ZeroDivisionError'>,division by zero
except ValueError as err:
    print(err)
    tb.print_exc() #prints the traceback

    # Enter Dividend: 7.5
    #err==invalid literal for int() with base 10: '7.5'
    # Traceback (most recent call last):
    #   File "D:\PGCP_AI_new\Day6\Exceptions.py", line 5, in <module>
    #     dividend=int(input('Enter Dividend: '))
    #              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # ValueError: invalid literal for int() with base 10: '7.5'
else:
    print('continue')
finally:
    print('Executed')