# Use official Ubuntu 24.04 as base image
FROM ubuntu:24.04

# Set environment variables to avoid interactive prompts during package install
ENV DEBIAN_FRONTEND=noninteractive
ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

# Install required tools and dependencies
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    lsb-release \
    apt-transport-https \
    software-properties-common && \
    mkdir -p /etc/apt/keyrings && \
    curl -fsSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc  | gpg --dearmor -o /etc/apt/keyrings/ros2-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/ros2-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2.list && \
    apt-get update && apt-get install -y \
    ros-jazzy-desktop \
    python3-colcon-common-extensions \
    && apt-get clean && rm -rf /var/lib/apt/lists\
     apt update\
     apt install -y \
    ros-jazzy-rviz2 \
    ros-jazzy-rqt \
    ros-jazzy-rqt-common-plugins \
    ros-jazzy-gazebo-ros \
    ros-jazzy-gazebo-ros2-control \
    gazebo \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    x11-apps \
    xvfb

# Setup ROS 2 environment
ENV ROS_DISTRO=jazzy
ENV ROS_VERSION=2
ENV ROS_PYTHON_VERSION=3

# Source ROS setup script automatically
RUN echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc

# Default working directory
WORKDIR /workspace