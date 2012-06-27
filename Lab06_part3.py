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

    

#Torres = player('Fernando','Torres',spain.name)
#Ronaldo = player('Cristiano','Ronaldo',portugal.name)
#Torres.add_score('2012/06/26',0)
#Torres.add_score('2012/06/26',0)
#Torres.add_score('2012/06/26',1)
#Torres.add_score('2012/06/26',0)

#Torres.average_score()
#Torres.total_score()


class Team:
    def __init__(self,name,league,manager_name,points=None):
        self.name   = name
        self.league = league
        self.manager_name =manager_name
        self.points = points
        self.players = []


    def add_player(self, newname):
        self.players.append(newname)

    def __str__(self):
        return 'Name: ',self.name,'League: ',self.league,'Manager: ',self.manager_name,'Points: ',self.points


class Match:
    def __init__(self,home_team,away_team,date = None):
        self.home_team = home_team
        self.away_team = away_team
        self.date = date
        self.home_scores = {}
        self.away_scores = {}

    def add_score(self,player,score):
        player_team=player.team
        
        if player_team == self.home_team:
            if player.lastname not in self.home_scores:
                self.home_scores[player.lastname]=score
            else :
                self.home_scores[player.lastname] += score
    
        elif player_team== self.away_team:
            if player.lastname not in self.away_scores:
                self.away_scores[player.lastname] = score
            else:
                self.away_scores[player.lastname] += score
        else:
            print 'Player name spelt wrong or not in team'


    def home_score(self):
        total = 0
        for value in self.home_scores.itervalues():
            total = total + value
        print self.home_team,':',total
        return total

    def away_score(self):
        total = 0
        for value in self.away_scores.itervalues():
            total = total + value
        print self.away_team,':',total
        return total

    def winner(self):
        
        if self.away_score()>self.home_score():
            print 'the winner is',self.away_team
        elif self.away_score()<self.home_score():
            print 'the winner is',self.home_team

        else:
            print 'the match is a draw'

        
portugal = Team('Portugal','UEFA','Paulo Bento')
spain  = Team('Spain','UEFA','Vicente del Bosque')

Torres = player('Fernando','Torres',spain.name)
Ronaldo = player('Cristiano','Ronaldo',portugal.name)

portugal.add_player('Ronaldo')
spain.add_player('Torres')

   
qualifier = Match('Portugal','Spain')
qualifier.add_score(Torres,1)
qualifier.add_score(Ronaldo,1)
qualifier.add_score(Torres,1)


