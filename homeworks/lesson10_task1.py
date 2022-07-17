def oops():
    raise IndexError


try:
    oops()
except IndexError:
    print('IndexError')
except:
    print('Other exception')
