##미니과제 2 클래스복습

class school :
    def __init__(self,name,year,address):
        self.name=name
        self.year=year
        self.address=address

    def print (self):
        print("The school is {} built in {} located in {}".format(self.name,self.year,self.address))

school1 = school("[Amazing primary school]","year 1999","Seoul")
school1.print()

user=input("Type in 'school name','year it's built','location'").split(' ')
school2 = school(user[0],user[1],user[2])
school2.print()
