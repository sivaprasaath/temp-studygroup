while True:
    try:
        age=int(input('enter your age: '))
        10/age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter a age higher than 0')
    else:
        print('thank you')
        break