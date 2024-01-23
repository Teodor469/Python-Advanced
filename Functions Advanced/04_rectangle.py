def rectangle(length, width):
    if not (isinstance(length, int) and isinstance(width, int)):
        return "Enter valid values!"
    
    area = length * width
    perimeter = (length + width) * 2

    return f"Rectangle area: {area}\nRectangle perimeter: {perimeter}"


print(rectangle(2, 10))

def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"
    
    def area():
        return length * width
    
    def perimeter():
        return (length + width) * 2
    
    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"