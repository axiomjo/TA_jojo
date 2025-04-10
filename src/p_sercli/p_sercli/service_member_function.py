from example_interfaces.srv import AddTwoInts

import rclcpy
from rclcpy.node import Node

class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal service')
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info('Incoming request\n:a: %d b: %d' % (request.a, request.b))

        return response


def main():
    rclcpy.init()

    minimal_service = MinimalService()

    rclcpy.spin(minimal_service)

    rclcpy.shutdown()


if __name__ == '__main__':
    main()
