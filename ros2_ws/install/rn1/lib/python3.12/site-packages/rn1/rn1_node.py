import rclpy
from rclpy.node import Node
import requests
import time
from example_interfaces.action import Fibonacci  # Using a standard action for simplicity
from rclpy.action import ActionClient

class RN1(Node):
    def __init__(self):
        super().__init__('rn1_node')
        self._action_client = ActionClient(self, Fibonacci, 'travel_action')
        self.timer = self.create_timer(1.0, self.check_for_travel)
        self.travel_id = 1  # Starting travel ID

    def check_for_travel(self):
        url = f'http://127.0.0.1:8000/travel/{self.travel_id}'
        response = requests.get(url)
        if response.status_code == 200 and 'error' not in response.json():
            travel = response.json()
            self.get_logger().info(f"trip received: {travel}")
            self.send_goal(travel)
            self.travel_id += 1
        else:
            self.get_logger().info("No new trip")

    def send_goal(self, travel):
        self.get_logger().info("Waiting for action server...")
        self._action_client.wait_for_server()
        goal_msg = Fibonacci.Goal()
        goal_msg.order = travel['travel_id']  # Just an example
        self._send_goal_future = self._action_client.send_goal_async(goal_msg)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return
        self.get_logger().info('Goal accepted :)')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f'Result: {result.sequence}')

def main(args=None):
    rclpy.init(args=args)
    rn1_node = RN1()
    rclpy.spin(rn1_node)
    rn1_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
