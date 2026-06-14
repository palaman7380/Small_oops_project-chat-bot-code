#create and view 2D coordinates


class point:
    
    def __init__(self,x,y):
        self.x_cod = x
        self.y_cod = y


    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)
    
    # #### A user can find out the distance between 2 coordinates ###

    def euclidean_distance(self,other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    
    #A user can find find the distance of a coordinate from origin ###

    def dis_from_origin(self):
        return self.euclidean_distance(point(0,0))
    # other return (self.x_cod **2 + self.y_cod ** 2)**0.5

    def lies_point(self , other):
        if self.x_cod == other.x_cod and self.y_cod==other.y_cod:
            return(True)
        else:
            return(False)
        

    ##### inside another classs ###
class line:
    def __init__(self ,A,B,C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        
        return f'{self.A}x {"+" if self.B >= 0 else "-"} {abs(self.B)}Y {"+" if self.C >= 0 else "-"} {abs(self.C)}'
        
    ##### A user can check if a point lies on a given line ###
    def point_on_line(line,point):
        if line.A * point.x_cod + line.B * point.y_cod + line.C == 0:
            return "Point satisfy on line"

        else:
            return "Point does not satisfy"
        
    #### A user can find the distance between a given 2D point and a given line ####
    def sortest_distance(line , point):
        return abs(line.A * point.x_cod + line.B * point.y_cod +line.C)/(line.A**2 + line.B ** 2)**0.5
                  
p1 = point(2,-2)
p2 = point(2,4)
print(p1.euclidean_distance(p2))
print(p1.dis_from_origin())
print(p1.lies_point(p2))
l1 = line(-2,2,0)
print(l1)
print(l1.point_on_line(p1))
print(l1.sortest_distance(p1))
