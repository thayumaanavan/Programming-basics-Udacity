
class Parent():
    def __init__(self,last_name,eye_color):
        self.last_name=last_name
        self.eye_color=eye_color
        print("Parent Contructor")

class Child(Parent):
    def __init__(self,last_name,eye_color,no_of_toys):
        print("Child constructor")
        Parent.__init__(self,last_name,eye_color)
        self.no_of_toys=no_of_toys
        



#parent=Parent("Rajan","black")

child=Child("Raj","blue",4)