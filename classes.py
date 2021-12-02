# class point() :
#     def __init__ (self,input1,input2) :
#         self.x = input1
#         self.y = input2

# p = point(2,3)
# print(p.x)
# print(p.y)
class flight() :
    def __init__(self,capacity) :
        self.capacity = capacity 
        self.passangers = []

    def add_passanger(self,name) :
        if not self.open_seats() :
            return False
        self.passangers.append(name)
        return True

    def open_seats(self) :
        return self.capacity - len(self.passangers)
        
p = flight(3)

person = ["jitesh","sourav","nitesh","vishwajeet"]

for pk in person :
    sucess = p.add_passanger(pk)
    if sucess :
        print(f"your seat is booked {pk}")
    else :
        print(f"not enough seats for {pk} go by train ")
        

        
        
         #automatically called  self() refereces the object 