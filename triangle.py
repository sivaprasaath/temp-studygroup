class triangle(object):
    num_of_sides=3
    def __init__(self,angle1,angle2,angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3
    def check_angles(self):
        if self.angle1 +self.angle2 +self.angle3==180:
            return True
        else:
            return False

my_triangle=triangle(30,30,120)
print(my_triangle.num_of_sides)
print(my_triangle.check_angles())