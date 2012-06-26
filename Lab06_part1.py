"""
Lab_Python_06
Part 1
"""

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/21/2012	| 1
"""

## create the player_stats data structure
import datetime 
player_stats= {'Rooney':[( datetime.date(2012,6,23) ,2),( datetime.date(2012,6,25) ,2)],'Ronaldo':[(datetime.date(2012,6,19),0),(datetime.date(2012,6,20),3)],'Torres':[(datetime.date(2012,6,21),0),(datetime.date(2012,6,21),1)]}

## implement highest_score
for i in range (0,1):
    var1 = player_stats['Rooney'][0][1]
    var2 = player_stats['Rooney'][1][1]
        
    if var1> var2:
        newVar=var1
        
print newVar
"""
var= player_stats['Rooney'][0][1]
print var
"""
##print player_stats['Rooney'][1][1]

## implement highest_score_for_player



## implement highest_scorer
