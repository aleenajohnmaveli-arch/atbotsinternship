#!/usr/bin/env python3

# Import required libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String


class WheelController(Node):

    def __init__(self):
        super().__init__('wheel_controller')

        # Subscribe to LiDAR topic
        self.subscription = self.create_subscription(
            Int32,
            'lidar_data',
            self.lidar_callback,
            10
        )

        # Publisher for wheel commands
        self.publisher_ = self.create_publisher(
            String,
            'wheel_command',
            10
        )

    def lidar_callback(self, msg):
        distance = msg.data

        command = String()

        if distance < 3:
            command.data = "STOP"
        else:
            command.data = "MOVE"

        self.publisher_.publish(command)

        self.get_logger().info(
            f'Distance = {distance}, Command = {command.data}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = WheelController()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
