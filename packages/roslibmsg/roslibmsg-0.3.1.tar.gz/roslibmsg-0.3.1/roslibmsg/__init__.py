from roslibpy import Message

class Vector3(Message):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
        self._data = {'x': self.x, 'y': self.y, 'z': self.z}

    @property
    def data(self):
        self._data = {'x': self.x, 'y': self.y, 'z': self.z}
        return self._data

class Twist(Message):
    def __init__(self, linear=Vector3(), angular=Vector3()):
        self.linear = linear
        self.angular = angular

    @property
    def data(self):
        self._data = {
            'linear': self.linear.data,
            'angular': self.angular.data
        }
        return self._data

class String(Message):
    def __init__(self, data=''):
        self._data = {
            'data': str(data)
        }

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data['data'] = str(value)

class Pose:
    class Position:
        def __init__(self, x=0.0, y=0.0, z=0.0):
            self.x = x
            self.y = y
            self.z = z

        def to_dict(self):
            return {'x': self.x, 'y': self.y, 'z': self.z}

    class Orientation:
        def __init__(self, x=0.0, y=0.0, z=0.0, w=0.0):
            self.x = x
            self.y = y
            self.z = z
            self.w = w

        def to_dict(self):
            return {'x': self.x, 'y': self.y, 'z': self.z, 'w': self.w}

    
    def __init__(self, position=None, orientation=None):
        self.position = position if position is not None else Pose.Position()
        self.orientation = orientation if orientation is not None else Pose.Orientation()

    @property
    def data(self):
        return {'position': self.position.to_dict(), 'orientation': self.orientation.to_dict()}

if __name__ == '__main__':
    data = Pose()
    print(data.data)
