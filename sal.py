class Player:
    teamplayer='Liverpool'
    def __init__(self,name):
        self.name=name #create instance of variabel
        
t1=Player('salman')
t2=Player('samad')
print(t1.name)
print(t2.name)
print("the liverpool player is an:",t1.teamplayer)
print("the liverpool player is an:",t2.teamplayer)


class Student:
    def __init__(self,phy,eng,math):
        self.phy=phy
        self.eng=eng
        self.math=math
        
        
        
t1=Student(80)
t2=Student(90)
t3=Student(70)

def objectTotal(self,total,phy,eng,math):
    self.total=total
    total=phy+eng+math
    
print(t1.objectTotal())
print(t2.objectTotal())
print(t3.objectTotal())



