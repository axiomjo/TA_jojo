import rclpy
from rclpy.node import Node
from pymycobot.mycobot import MyCobot
from std_srvs.srv import Trigger
import time

class MyCobotControlNode(Node):
    def __init__(self):
        super().__init__('mycobot_control_node')
        self.mc = MyCobot('/dev/ttyAMA0', 1000000)
        self.mc.power_on()
        self.get_logger().info("MyCobot powered on!")

        self.srv = self.create_service(Trigger, 'move_to_home', self.move_to_home_callback)

    def move_to_home_callback(self, request, response):
        try:
            home = [52.9, -61.5, 411.3, 89.12, 36.59, 92.99]
            self.mc.send_coords(home, 50, 0)
            time.sleep(3)
            response.success = True
            response.message = "Moved to home."
        except Exception as e:
            response.success = False
            response.message = f"Error: {str(e)}"
        return response

def main(args=None):
    rclpy.init(args=args)
    node = MyCobotControlNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
