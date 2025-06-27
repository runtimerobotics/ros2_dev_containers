cmake_minimum_required(VERSION 3.5)
project(minimal_nav_pkg)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

add_executable(minimal_nav_node src/minimal_nav_node.cpp)
ament_target_dependencies(minimal_nav_node rclcpp)

install(TARGETS
  minimal_nav_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
