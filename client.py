import sys
import Facade.facade as Facade

if __name__ == '__main__':
    if(len(sys.argv) == 1):
        print("Hey, there's Jude, your best friend to analyze computer current situation")
    else:
        facade = Facade.Facade(mode=sys.argv)