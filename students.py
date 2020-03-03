class students:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    class_ = "student"
    def score(self,score1,score2,score3):
        average = (score1 + score2 +score3)/3
        return average
Mike=students("Mike",25)
score1 = int(input("Please input your first score: "))
score2 = int(input("Please input your second score: "))
score3 = int(input("Please input your third score: "))
print("The average score is: ",Mike.score(score1,score2,score3))