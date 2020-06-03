# Created by Truzz Blogg (Ricardo)
# Youtube link: https://youtu.be/Uh5x-InkAS0

user_input = int(input("Enter your number: "))

even_num = 0
odd_num = 0

while(user_input > 0):
  if user_input % 2 == 0:
    even_num += 1
  else:
    odd_num += 1
  user_input = user_input // 10

print(f"Number of Even Numbers: {even_num} | Number of Odd Numbers: {odd_num}")
# print("Number of Even Numbers: {} | Number of Odd Numbers: {}".format(even_num, odd_num))
# print("Number of Even Numbers: %d | Number of Odd Numbers: %d" % (even_num, odd_num))