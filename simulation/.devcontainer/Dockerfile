# Use official ROS 2 Jazzy base image
FROM ros:jazzy-ros-base

# Install basic tools and Gazebo dependencies
RUN apt-get update && apt-get install -y \
    curl gnupg lsb-release \
    python3-colcon-common-extensions \
    build-essential \
    git wget nano net-tools \
    python3-rosdep \
    gazebo11 \
    ros-jazzy-turtlebot3-gazebo \
    ros-jazzy-gazebo-ros-pkgs \
    ros-jazzy-gazebo-ros2-control \
    ros-jazzy-rviz2 \
    ros-jazzy-xacro \
    ros-jazzy-robot-state-publisher && \
    rm -rf /var/lib/apt/lists/*

# Setup rosdep
RUN rosdep init || true && rosdep update

# Setup ROS environment for user
SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/ros/jazzy/setup.bash" >> /root/.bashrc

# Set working directory
WORKDIR /workspace

# Default command
CMD ["bash"]
