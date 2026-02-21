def total_salary(path):
   try:
      with open(path, 'r', encoding='utf-8') as file:
         lines = file.readlines()

         if not lines:
            print("[ERROR]: File is empty!")
            return (0, 0)
         
         total = 0
         persons_with_salary_count = 0 

         for line in lines:
            person = line.strip().split(",")
            try:
               salary = int(person[1])
               total += salary
               persons_with_salary_count += 1
            except (IndexError, ValueError): 
               continue
 
         average = total // persons_with_salary_count 

         return (total, average)
          
   except FileNotFoundError:
      print("[ERROR]: File not found!")
      return (0, 0)

# test
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")