def func():
    print("This code is from myfunc file")

if(__name__ == "__main__"):
    func()
    print(__name__) # this will print the __main__ if its main file otherwise name of file imported from

else :
    print("  Other files can be runned from main file only")