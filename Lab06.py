import datetime
class player:
    def __init__(self,firstname,lastname,team=None):
        self.firstname= firstname
        self.lastname= lastname
        self.scores=[ ]
        self.team=team

    def add_score(self,date,score):
        #self.scores.append(date)
        self.scores.append(score)

    def total_score(self):
        total=0
        for items in range (0,len(self.scores)):
            total = total + self.scores[items]
        print 'the total is ',total
        
    def average_score(self):
        count=0
        total=0
        for items in range (0,len(self.scores)):
            total = total + self.scores[items]
            count += 1
        avg = total/count
        print 'Average is: ',avg

    

Torres = player('Fernando','Torres')
Torres.add_score('2012/06/26',0)
Torres.add_score('2012/06/26',0)
Torres.add_score('2012/06/26',1)
Torres.add_score('2012/06/26',0)

Torres.average_score()
Torres.total_score()
