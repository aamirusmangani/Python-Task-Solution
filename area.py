def calculate_area(length, width):
    if length == width:
        return "This is a Square"
    area = length * width
    return area

length = float(input())
width = float(input())
result = calculate_area(length, width)
print(result)