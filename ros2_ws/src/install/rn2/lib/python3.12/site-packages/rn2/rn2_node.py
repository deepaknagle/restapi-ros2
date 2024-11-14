import rclpy
from rclpy.node import Node
from example_interfaces.action import Fibonacci  # Using the same action
from rclpy.action import ActionServer

class RN2(Node):
    def __init__(self):
        super().__init__('rn2_node')
        self._action_server = ActionServer(
            self,
            Fibonacci,
            'travel_action',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        order = goal_handle.request.order
        self.get_logger().info(f"travel ID: {order}")

        feedback_msg = Fibonacci.Feedback()
        feedback_msg.sequence = [0, 1]

        for i in range(1, order):
            feedback_msg.sequence.append(feedback_msg.sequence[i] + feedback_msg.sequence[i-1])
            self.get_logger().info(f'Feedback: {feedback_msg.sequence}')
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)

        goal_handle.succeed()

        result = Fibonacci.Result()
        result.sequence = feedback_msg.sequence
        return result

def main(args=None):
    rclpy.init(args=args)
    rn2_node = RN2()
    rclpy.spin(rn2_node)
    rn2_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
