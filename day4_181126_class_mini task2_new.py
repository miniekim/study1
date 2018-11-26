##미니과제 2 클래스복습

class school :
    def _init_(self,name,year_built,address):
        self.name=name
        self.year_built=year_built
        self.address=address

school1=school("university","ac.1000","Seoul")
print(school1.name,school1.year_built,school1.address)
