
class Parent():
    def __init__(self,last_name,eye_color):
        self.last_name=last_name
        self.eye_color=eye_color
        print("Parent Contructor")
    
    def show_info(self):
        print("Last Name: "+self.last_name+";Eye Color: "+self.eye_color)

class Child(Parent):
    def __init__(self,last_name,eye_color,no_of_toys):
        print("Child constructor")
        Parent.__init__(self,last_name,eye_color)
        self.no_of_toys=no_of_toys
    
    def show_info(self):
        print("No. of Toys: "+str(self.no_of_toys))
        



#parent=Parent("Rajan","black")
#parent.show_info()
child=Child("Raj","blue",4)
child.show_info()