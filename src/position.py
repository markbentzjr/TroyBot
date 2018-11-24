import math


class Vector3:
    def __init__(self, x=0.00, y=0.00, z=0.00):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def set_value(self, target):
        self.x = float(target.x)
        self.y = float(target.y)
        self.z = float(target.z)
        return self

    def __add__(self, val):
        return Vector3(self.x + val.x, self.y + val.y, self.z + val.z)

    def __sub__(self, val):
        return Vector3(self.x - val.x, self.y - val.y, self.z - val.z)

    def __mul__(self, val):
        return Vector3(self.x * val.x, self.y * val.y, self.z * val.z)

    def real_distance(self, target):
        return ((self.x - target.x)**2 + (self.y - target.y)**2 + (self.z - target.z)**2)**0.5

    def correction_2D(self, ideal):
        curr = math.atan2(self.y, -self.x)
        ideal = math.atan2(ideal.y, -ideal.x)

        correction = ideal - curr
        if abs(correction) > math.pi:
            if correction < 0:
                correction += 2 * math.pi
            else:
                correction -= 2 * math.pi

        return correction
