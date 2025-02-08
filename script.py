import os
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def visualize_directory(path, indent=0):
    try:
        if not os.path.exists(path):
            print(Fore.RED + f"Помилка: Шлях '{path}' не існує!")
            return
        if not os.path.isdir(path):
            print(Fore.RED + f"Помилка: Шлях '{path}' не є директорією!")
            return
        
        items = os.listdir(path)

        for item in items:
            item_path = os.path.join(path,item)

            if os.path.isdir(item_path):
                print(Fore.CYAN + ' ' * indent + f"[DIR] {item}")
                visualize_directory(item_path, indent + 4)
            else:
                print(Fore.GREEN + ' ' * indent + f"[FILE] {item}")

    except PermissionError:
        print(Fore.RED + f"Помилка: Немає прав доступу до '{path}'")
    except Exception as e:
        print(Fore.RED + f"Сталася помилка: {e}")

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Будь ласка, вкажіть шлях до директорії як аргумент!")
        sys.exit(1)
    
    path = sys.argv[1]

    visualize_directory(path)

if __name__ == "__main__":
    main()