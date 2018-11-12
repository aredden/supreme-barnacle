import sys

#**************************************************
#   Example 0: How to add python files to __main__.py
#**************************************************
from .funcmodule import run

#**************************************************
#   Example 1: main method called in BlockChainTxcli.
#**************************************************
def main():

#****************My Code v0.1.0********************
    run()

#**************************************************
#   Example 2 Below: Taking args from the command line.
#   Example 2.1: How to insert information into {}
#   brackets in strings
#       'passed argument :: {}'.format(arg)
#**************************************************
args = sys.argv[1:]
### My Code ###
#if args.__len__() > 0 :

#**************************************************
#   Example 3: Calling a function with args.
#**************************************************
### My Code ###
#my_function(args[0])

#**************************************************
#   Example 4: How to use object oriented programming
#   with BlockChainTx-cli.
#**************************************************
#my_object = MyClass(args[0])
#my_object.say_name()

#**************************************************
#   Example 5: How the script hooks into python
#   & calls main().
#**************************************************
if __name__ == '__main__':
    main()
