

def run():

    name = input("Hello, What is your name?\n")
    num = input("\nHello {}!\nWould you like to see Bitcoin price? Y/N\n".format(name))
    if num.lower() == 'y':

#**************************************************
# TODO: links to APIGetters.py in Support/?
#**************************************************

        print("\n...Doing Stuff")
    else:
        print('\nDoing Nothing')
