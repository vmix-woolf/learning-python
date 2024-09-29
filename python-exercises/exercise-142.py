def polygon_name():
    polygon = ''
    sides = int(input("Input the number of sides for the shape (from 3 to 6):"))
    
    while sides < 3 or sides > 6:
        print(f"That number of sides is not supported by this program.")
        sides = int(input("Input the number of sides for the shape (from 3 to 6):"))

    match sides:
        case 3:
            polygon = f"This is a triangle"
        case 4:
            polygon = f"This is a quadrilateral"
        case 5:
            polygon = f"This is a pentagon"
        case 6:
            polygon = f"This is a hexagon"

    print(polygon)

polygon_name()
