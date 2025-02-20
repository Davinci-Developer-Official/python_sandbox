# def greeting():
#     print("hello world");

# greeting();

# def calculate_area_of_rectangle(length,width):
#     calc= length * width;
#     print(calc);
#     return;
# calculate_area_of_rectangle(5,6);

def conditions(shape=""):
        #area of triangle
    def area_of_trangle(base,height):
            area = 1/2*base*height;
            print(area);
            return;
        #area of square
    def area_of_square(length):
            area = length * length;
            print(area)
            return;
        # area of rectangle
    def area_of_a_rectangle(length,width):
        area = length * width;
        print(area)
        return;
    def area_of_a_cylinder(radius,height):
        area = 3.14 * (radius*radius) * height;
        print(area+'m2');
        return;
    
    def area_of_cube(length):
        area = length * length * length;
        print(area);
        return;   
        
    # logical statements
    if(shape=="triangle"):
        area_of_trangle(6,7)
    elif(shape=="square"):
        area_of_square(4)
    elif(shape=="rectangle"):
        area_of_a_rectangle(9,5)
    elif(shape=="cylinder"):
        area_of_a_cylinder(10,20);  
    elif(shape=="cube"):
        area_of_cube(30)
    
conditions("cube");
    