import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізація colorama
init(autoreset=True)

def visualize_structure(path, indent=""):
    try:
        p = Path(path)
        
        if not p.exists():
            print(Fore.RED + f"Помилка: Шлях '{path}' не існує.")
            return
        if not p.is_dir():
            print(Fore.RED + f"Помилка: '{path}' не є директорією.")
            return

        # Отримуємо список файлів та папок
        items = sorted(p.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))

        for item in items:
            #  додаємо ігнорування системних папок
            if item.name in ['venv', '__pycache__', '.git', '.ipynb_checkpoints']:
                continue
                
            if item.is_dir():
                # Виводимо папку синім кольором
                print(f"{indent}{Fore.BLUE}📁 {item.name}")
                # Рекурсивно заходимо всередину
                visualize_structure(item, indent + "    ")
            else:
                # Виводимо файл зеленим кольором
                print(f"{indent}{Fore.GREEN}📜 {item.name}")

    except Exception as e:
        print(Fore.RED + f"Виникла помилка: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(Fore.YELLOW + "Використання: python main.py [шлях_до_директорії]")
    else:
        root_path = sys.argv[1]
        print(Fore.CYAN + f"\nСтруктура директорії: {root_path}\n" + "-"*30)
        visualize_structure(root_path)