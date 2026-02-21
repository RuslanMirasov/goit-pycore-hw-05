def get_cats_info(path):
   cats = []

   try:
      with open(path, 'r', encoding='utf-8') as file:
         lines = file.readlines()
         
         if not lines:
            print("[ERROR]: File is empty!")
            return cats
         
         for line in lines:
            cat = line.strip().split(",")

            if len(cat) != 3: 
               continue

            cat_id, name, age = cat

            cats.append({
               "id" : cat_id, 
               "name" : name, 
               "age" : age
            })

         return cats
          
   except FileNotFoundError:
      print("[ERROR]: File not found!")
      return cats

# test
cats_info = get_cats_info("cats_file.txt")
print(cats_info)