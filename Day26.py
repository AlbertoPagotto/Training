numbers=[1,2,3]
new_list=[n+1 for n in numbers]

name="Alberto"
new_list1=[letter for letter in name]
print(new_list1)
new_list1

num_set=range(1,5)
num_set2=[2*num for num in num_set]
print(num_set2)

'''with open ("file1.txt") as file_1:
    list1=file_1.readlines()
    list1=[int(num.strip()) for num in list1]

with open ("file2.txt") as file_2:
    list2=file_2.readlines()
    list2=[int(num.strip()) for num in list2]

result=[num1 for num1 in list1 if (num1 in list2) ]
# Write your code above 👆

print(result)'''

'''sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
list_words=sentence.split()

result={word:len(word) for word in list_words}


print(result)'''

'''weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f={key:round((9/5*weather_c[key]),1)+32 for key in weather_c}


print(weather_f)'''
