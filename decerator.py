def outer(func):
    def inner():
        func()
    return inner
def display():
    print("hello")
inner_ob=outer(display)
inner_ob()
