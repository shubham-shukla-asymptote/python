import math
def circle_states(radius):
    area=math.pi*radius**2
    circumference=2*math.pi*radius
    return round(area,3),round(circumference,3)
a,b=circle_states(7)
print("Area:",a,"Circumference:",b)
