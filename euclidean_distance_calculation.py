def euclideanDistance(point1, point2):  #Bu fonksiyon 2 nokta arasındaki en kısa mesafeyi döndürür.
    a, b = point1
    c, d = point2
    return ((c - a) ** 2 + (d - b) ** 2) ** 0.5

points = ((5, 8), (8, 4), (2, 12), (15, 9))

distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))
      
min_dist = distances[0]

for i in range(len(distances) - 1):
    if distances[i + 1] < min_dist:
        min_dist = distances[i + 1]

print("En kısa mesafe: ", min_dist)