#!/usr/bin/env python3

# Import required libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class LidarPublisher(Node):

    def __init__(self):
        super().__init__('lidar_publisher')

        # Create publisher for the topic "lidar_data"
        self.publisher_ = self.create_publisher(Int32, 'lidar_data', 10)

        # Timer callback every 1 second
        self.timer = self.create_timer(1.0, self.publish_data)

        self.distance = 0

    def publish_data(self):
        msg = Int32()
        msg.data = self.distance

        self.publisher_.publish(msg)
        self.get_logger().info(f'Published distance: {msg.data}')

        # Increment from 1 to 10 and repeat
        self.distance += 1
        if self.distance > 10:
            self.distance = 0


def main(args=None):
    rclpy.init(args=args)

    node = LidarPublisher()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
