#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ArmController(Node):

    def __init__(self):
        super().__init__('arm_controller')

        # Subscribe to wheel commands
        self.subscription = self.create_subscription(
            String,
            'wheel_command',
            self.wheel_callback,
            10
        )

        # Publisher for arm commands
        self.arm_publisher = self.create_publisher(
            String,
            'arm_command',
            10
        )

    def wheel_callback(self, msg):
        wheel_state = msg.data

        arm_msg = String()

        if wheel_state == "MOVE":
            arm_msg.data = "HOLD"
        else:
            arm_msg.data = "MOVE"

        self.arm_publisher.publish(arm_msg)

        self.get_logger().info(
            f'Wheel state: {wheel_state}, Arm command: {arm_msg.data}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = ArmController()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
