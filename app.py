from unicodedata import name
from cars import car
from Questions import question
from Objects import object
python_2 = 5
print("primul program " + str(python_2))


def Function_1 (name):
    print ("premier function "+name)

#Function_1(input("give name: "))

def Function_2 (num1,num2):
   return num1 * num2


result = Function_2(3,5)
print(result)



def change(text):
    changer = ""
    for letter in text:
        if letter in "ast":
            changer = changer + ".."
        else:
            changer= changer + letter
    return changer
#print(change(input("text: ")))

#file = open("file1", "a")

#file.write("\ntoby")

#file.close()

car1 = car("Ferrari", "F150","SportCar", 200000)
print(car1.name)

car1.speed("200")

questions = ["What color are apples?\n (a)red\n (b)gray \n(c)Indonesia\n",
             "What color are flour?\n (a)red\n (b)gray \n(c)Indonesia\n",
             "Which country starts with I and Finish if ndonesia?\n (a)red\n (b)gray \n(c)Indonesia\n"]

q = [question(questions[0], "a"),
     question(questions[1], "b"),
     question(questions[2], "c")]

q1 = [question(questions[2], "c"),
     question(questions[1], "b"),
     question(questions[0], "a")]


def run_test(qestions):
    score = 0
    for question in qestions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got "+ str(score)+"/"+str(len(qestions) )+ " Correct")

#run_test(q1)


matrix = [5,3,11,653,1,53,55]
for sorted in range(len(matrix)):
    for x in range(len(matrix)-1):
        if matrix[x] > matrix[x+1]:
            aux = matrix[x]
            matrix[x] = matrix[x+1]
            matrix[x+1] = aux
print(matrix)

matrix1 = [5,11,2,6,432,6,23,5,1]
matrix1.sort()
print(matrix1)

#crearea unui nou branch


print("test for added branch")
print("test2")
#set are not dublicate numbers in array
s1 = set([1,2,33,33,4])
print(s1)
#tuple container to store diferent values
coordonates = [("hello", "world"), (32,11), (35,1)]
#tuples are immutable can not been changed or modify
print(coordonates[0][1]) 
#dictionary
student = {'name':'john','age':24,'courses':['Math','compSci'] }
print(student['name'],student['courses'])

#slicing is litteraly extracting certan elements form our array list list[start:end:step(skip)]
print (matrix[1:4])
print (matrix[2:])
print (matrix[1:6:2])



obj1 = object("Asus","ROG 554","Gaming")
print(obj1.name)

obj1.trax("noob")
