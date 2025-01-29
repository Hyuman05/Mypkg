import rclpy
from rclpy.node import Node
from std_msgs.msg import String


rclpy.init()
node = Node("listener")


def cb(sub):
    global node
    node.get_logger().info("Listen: %s" % sub.data)


def main():
    sub = node.create_subscription(String, "weather_data", cb, 10)
    rclpy.spin(node)
