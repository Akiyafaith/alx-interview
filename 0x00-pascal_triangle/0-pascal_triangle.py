def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            prev_row = triangle[-1]
            new_row = [1]
            for x in range(1, i):
                new_row.append(prev_row[x - 1] + prev_row[x])
            new_row.append(1)
            triangle.append(new_row)
    
    return triangle