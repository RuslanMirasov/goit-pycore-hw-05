def parse_input(user_input):
   cmd, *args = user_input.split()
   cmd = cmd.strip().lower()
   return cmd, *args

# add_contact handler
def add_contact(args, contacts):
   if len(args) != 2:
      return "Invalid arguments."
   
   name, phone = args
   contacts[name] = phone
   return "Contact added."

# change_contact handler
def change_contact(args, contacts):
   if len(args) != 2:
      return "Invalid arguments."

   name,phone = args
   if name in contacts:
      contacts[name] = phone
      return "Contact updated."
   else:
      return "Contact not found!"

# show_phone handler
def show_phone(args, contacts):
   if len(args) != 1:
      return "Invalid arguments."

   name = args[0]

   if name in contacts:
      return contacts[name]
   else:
      return "Contact not found!"

# show_all handler    
def show_all(contacts):
   if not contacts:
      return "No contacts found."

   result = ""
   for name, phone in contacts.items():
      result += f"{name}: {phone}\n"

   return result.strip()