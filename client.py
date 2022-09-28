import sys
import Facade.facade as Facade
from pyfiglet import figlet_format 
from rich.console import Console

console = Console()

if __name__ == '__main__':
    if(len(sys.argv) == 1):
        console.print(figlet_format("Jude", font = "standard" ), style="bold yellow")
        console.print("Hey, there's Jude, your best friend to analyze computer current situation", style="bold plum4")
    else:
        facade = Facade.Facade(mode=sys.argv)