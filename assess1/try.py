def fun(a,b):
    try:
        c = int(a)
        print(c+'a')
    except TypeError:
        print('t')
    finally:
        print('if')

try:
    fun('c',3)
except ValueError:
    print('v')
finally:
    print('of')
