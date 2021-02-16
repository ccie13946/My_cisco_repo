from yy import Student
student1 = Student("stephen","41","176")
print(student1.name)
"""

question_prompts = ["what is your favorite game?\n a minecraft\n b,amongus\n",
             "what is your name\n a stephen\n b alex\n",
             "what is your favorite car\n a white\n b blue\n"
]
from question import Question

questions = [Question(question_prompts[0],"a"),
             Question(question_prompts[1],"b"),
             Question(question_prompts[2],"b")
           ]

def run_test(questions):
      score = 0
      for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
              score += 1
      print("you have got " + str(score)+"/"+ str(len(questions)) +  " answered right")

run_test(questions)
#very very good

"""

from student import Student

student1 = Student("stephen",41,3.9)
student2 = Student("Alex",10,3.1)
student2.good()
