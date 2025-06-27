cmake_minimum_required(VERSION 3.8)
project(my_test_package)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

# Define and build the executable
add_executable(my_node src/my_node.cpp)
ament_target_dependencies(my_node rclcpp)

# Install the executable
install(TARGETS my_node
  DESTINATION lib/${PROJECT_NAME})

# Optional: Linting if you enable tests
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_cpplint_FOUND TRUE)
  set(ament_cmake_copyright_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
