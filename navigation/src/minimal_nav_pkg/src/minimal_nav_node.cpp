#include "rclcpp/rclcpp.hpp"

class MinimalNavNode : public rclcpp::Node
{
public:
  MinimalNavNode() : Node("minimal_nav_node")
  {
    RCLCPP_INFO(this->get_logger(), "Minimal Nav2 node started.");
  }
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalNavNode>());
  rclcpp::shutdown();
  return 0;
}
