class students:
    calc = 0
    def __init__(self,name=student,age=student,class_=student):
        self.name = name
        self.age = age
        self.class_ = class_
    def score(self,scores=[],average=0):
        for i in range(4):
            scores = input ("Please enter your scores?")
            for i in scores:
                calc = calc + scores[i]
                average = calc/(len(scores)
current = students("Mike",25,"QA")