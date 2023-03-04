#Write your code below this row 👇
accumulator = 0;
# for number in range(1, 101):
#   if number % 2 == 1:
#     continue;
#   accumulator += number;
# print(accumulator)

for number in range(1, 101):
   if number % 2 == 0:
     accumulator += number;
print(accumulator)