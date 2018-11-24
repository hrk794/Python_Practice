def ask_ok(prompt, retries=4, reminder="Please try again!"):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes', 'yep'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries -= 1
        if retries <= 0:
            raise ValueError('invalid user response')
        print(reminder)


print(ask_ok('Do you really want to quit?'))
print(ask_ok('Ok to overwrite the existing content?', 2))
print(ask_ok('Ok to overwrite the existing data?', 3, 'Please enter only yes or no'))
