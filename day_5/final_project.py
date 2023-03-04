#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# second try

easy_pwd = [];
for random_letter in range(0, nr_letters):
  target = random.choice(letters);
  easy_pwd += target;

for random_symbol in range(0, nr_symbols):
  target = random.choice(symbols);
  easy_pwd += target;

for random_number in range(0, nr_numbers):
  target = random.choice(numbers);
  easy_pwd += target;

print('second try',easy_pwd)

random.shuffle(easy_pwd);
print(easy_pwd)

final_hard_pwd = '';
for item in easy_pwd:
  final_hard_pwd += item;

print(f"final second hard pwd : {final_hard_pwd}")


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

random_letters = [];
random_symbols = [];
random_numbers = [];

pwd_list = [];

for random_cycle_letter in range(0, nr_letters):
  random_letter = letters[random.randint(0, len(letters)-1)];
  pwd_list.append(random_letter);

for random_cycle_symbol in range(0, nr_symbols):
  random_symbol = symbols[random.randint(0, len(symbols) - 1)];
  pwd_list.append(random_symbol);

for random_cycle_number in range (0, nr_numbers):
  random_number = numbers[random.randint(0, len(numbers)-1)];
  pwd_list.append(random_number)

print(pwd_list)
final_pwd_easy = '';
for item in pwd_list:
  final_pwd_easy += item;

print(final_pwd_easy);

# pwd_list에서 random length를 뽑아서 나열

replicate_pwd_list = pwd_list;

print(replicate_pwd_list)

mixed_list = [];

for mixed_up in range(0, len(pwd_list)):
  # 먼저 pwd_list의 length만큼 반복문을 돌릴건데.
  target = replicate_pwd_list[random.randint(0, len(replicate_pwd_list)-1)];
  mixed_list.append(target);
  replicate_pwd_list.remove(target);
print(mixed_list);

final_pwd_hard = '';

for item in mixed_list:
  final_pwd_hard += item;
print(f"Your final password is: {final_pwd_hard}")
  


  
  
  

  


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P