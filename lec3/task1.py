class Point:
    def __init__(self, X_set:int = 0, Y_set:int = 0):
        self.X = X_set
        self.Y = Y_set
    
    def on_line_with(self, p1, p2) -> bool:
        return (p2.X * (p1.Y - self.Y) - p2.Y * (p1.X - self.X) == self.X * p1.Y - p1.X * self.Y)
         


p1 = Point(1,1)
p2 = Point(2,2)
p3 = Point(3,3)

print(p1.on_line_with(p1, p2))
            
