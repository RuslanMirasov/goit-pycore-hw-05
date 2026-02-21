import sys
from pathlib import Path
from colorama import init, Fore
from filestree import print_tree 

init(autoreset=True) 

def main():
   if len(sys.argv) < 2:
      return print("Please provide a directory")
   
   path = Path(sys.argv[1])

   if not path.exists():
      return print("Directory not exist!")
   
   if not path.is_dir():
      return print("Provided path is not a directory!")
   
   print(Fore.BLUE + "📂 " + path.name)
   print_tree(path)

if __name__ == "__main__":
    main() 

# test 
# Активація оточення (git bush): source .venv/Scripts/activate
# Запуск скрипта з папкою: python main.py ./picture