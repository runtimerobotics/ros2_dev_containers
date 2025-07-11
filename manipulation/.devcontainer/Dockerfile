# File: .devcontainer/Dockerfile

FROM ros:jazzy-ros-base

# Set noninteractive frontend
ENV DEBIAN_FRONTEND=noninteractive

# Install ROS 2 tools: RViz, MoveIt, GUI support, etc.
RUN apt update && apt install -y \
    ros-jazzy-desktop-full \
    ros-jazzy-moveit \
    ros-jazzy-rviz2 \
    ros-jazzy-joint-state-publisher-gui \
    ros-jazzy-controller-manager \
    ros-jazzy-ros2-control \
    ros-jazzy-ros2-controllers \
    x11-apps \
    build-essential \
    python3-colcon-common-extensions \
    git \
    curl \
    wget \
    nano \
    && rm -rf /var/lib/apt/lists/*

# Set up entrypoint and environment
SHELL ["/bin/bash", "-c"]

# Source ROS automatically
RUN echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc

# Set DISPLAY env variable for GUI support (X11)
ENV DISPLAY=:0
