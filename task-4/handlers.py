from functools import wraps

# Декоратор для обробки помилок введення користувача
def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ValueError:
            return "Give me name and phone please."

        except KeyError:
            return "Contact not found."

        except IndexError:
            return "Enter user name."

    return inner

# Функція розбору введеної команди
def parse_input(user_input):
   cmd, *args = user_input.split()
   cmd = cmd.strip().lower()
   return cmd, *args

# Обробник команди додавання контакту
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Обробник команди зміни контакту
@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

# Обробник команди перегляду телефону контакту
@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]

# Обробник команди виведення всіх контактів  
@input_error
def show_all(contacts):
    # Якщо словник контактів порожній
    if not contacts:
        return "No contacts found."

    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"

    return result.strip()