def circle_area():
    radius = int(input('\nEnter the raduis:'))
    import math
    pie = math.pi
    area_of_a_circle = pie*radius**2
    print(f"The area of the circle with raduis {radius} is {area_of_a_circle:.2f}")
circle_area()          