def animal():
    print("animal")

def large_func():
    x = 6

def func_that_uses_x():
    print("func_that_uses_x")


def func_that_modifies_x():
    nonlocal x  # python3 only
    x += 1

func_that_uses_x()
func_that_modifies_x()