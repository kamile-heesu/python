# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# for loop을 이용해서 평균값을 구하세요.

# 정수로 반을룀하세요.

# len() 이나 sum() 을 사용하지 마세요. 

print(student_heights)

# 157 183 167 160 163 148
sum = 0;
index = 0;
for student in student_heights:
  sum = sum + student;
  index = index + 1;
print(f"sum : {sum} \n length : {index}")
average = round(sum / index);
print(average)




