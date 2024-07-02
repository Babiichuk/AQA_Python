# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record in the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13 have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# 1 - Add your new record in the beginning of the given list
people_records.insert(0, ('Olena', 'Velyka', 33, 'Cleaner', 'Kyiv'))

# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
temp_record = people_records[1]
people_records[1] = people_records[5]
people_records[5] = temp_record

for record in people_records:
    print(record)

# 3 - check that all people in modified list with records indexes 6, 10, 13 have age >=30. Print condition check result
record_6 = (people_records[6][2])
record_10 = (people_records[10][2])
record_13 = (people_records[13][2])

print(record_6 >= 30 and record_10 >= 30 and record_13 >= 30)