# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
first_name = name1.lower()
second_name = name2.lower()

f_number = 0
f_name = (first_name + second_name).count('t')
f_number+= f_name

f_name = (first_name + second_name).count('r')
f_number+= f_name

f_name = (first_name + second_name).count('u')
f_number+= f_name

f_name = (first_name + second_name).count('e')
f_number+= f_name
 
t_f_number = str(f_number)

s_number = 0
s_name = (first_name + second_name).count('l')
s_number+= s_name

s_name = (first_name + second_name).count('o')
s_number+= s_name

s_name = (first_name + second_name).count('v')
s_number+= s_name

s_name = (first_name + second_name).count('e')
s_number+= s_name

t_s_number = str(s_number)

your_love = int(t_f_number + t_s_number)

if your_love <= 10 and your_love >= 90:
  print(f"Your score is {your_love}, you go together like coke and mentos.")

elif your_love >= 40 and your_love <= 50:
  print(f"Your score is {your_love}, you are alright together.")

else:
  print(f"Your score is {your_love}.")


# Kanye West Kim Kardashian
# Brad Pitt Jennifer Aniston
# Angela Yu Jack Bauer



