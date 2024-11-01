# for some reason, putting CQs.cq09.point gave me a ModuleNotFoundError
from point import Point

# new equal instances of Point
point1 = Point(5.0, 2.0)
point2 = Point(5.0, 2.0)


# call both methods and check results:

# mutated
point1.scale_by(2)
print(f"Mutated: ({point1.x}, {point1.y})")

# not mutated
new_point2 = point2.scale(2)  # create variable to check if point2 got mutated
print(f"Original point2: ({point2.x}, {point2.y})")
print(f"Scaled point2: ({new_point2.x}, {new_point2.y})")
