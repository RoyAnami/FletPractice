#Original: https://qiita.com/oriefield/items/29e68ba889778e2058bf

def scope_test():
    """Outer func scope"""
    def do_local():
        """Inner func scope"""
        spam = "local spam"

    def do_nonlocal():
        """Inner func scope"""
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        """Inner func scope"""
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam) # not assigned
    do_nonlocal()
    print("After nonlocal assignment:", spam) # assigned
    do_global()
    print("After global assignment:", spam) # not assigned

"""Module scope"""
scope_test()
print("In global scope:", spam) # assigned