from colorama import Fore

def print_tree(path, prefix=""):
    items = list(path.iterdir())
    count = len(items)

    for index, item in enumerate(items):
        is_last = index == count - 1

        connector = "┗ " if is_last else "┣ "
        blue_prefix = Fore.BLUE + prefix + connector

        if item.is_dir():
            print(
                blue_prefix +
                Fore.BLUE + "📂 " + item.name
            )

            new_connector = "    " if is_last else "┃ "
            new_prefix = prefix + new_connector
            print_tree(item, new_prefix)

        else:
            print(
                blue_prefix +
                Fore.GREEN + "📜 " + item.name
            )
