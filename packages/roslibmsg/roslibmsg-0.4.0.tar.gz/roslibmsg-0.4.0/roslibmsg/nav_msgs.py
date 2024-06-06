from roslibpy import Message
from roslibmsg.geometry_msgs import PoseStamped

class Path(Message):
    def __init__(self, header=None, poses=None):
        self.header = header if header is not None else PoseStamped.Header()
        self.poses = poses if poses is not None else []

    @property
    def data(self):
        return {'header':self.header.data, 'poses': [pose.data for pose in self.poses]}

if __name__ == '__main__':
    data = Path()
    print(data.header)