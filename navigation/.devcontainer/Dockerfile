# Base Image
FROM osrf/ros:jazzy-desktop-full

# Always set noninteractive for safe installs
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and add ROS 2 sources
RUN apt update && apt install -y curl gnupg2 lsb-release && \
    curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc -o /etc/apt/trusted.gpg.d/ros.gpg && \
    echo "deb http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list && \
    apt update

# Install only Navigation2-related packages and useful tools
RUN apt install -y \
    python3-pip \
    xterm \
    iputils-ping \
    net-tools \
    vim \
    ros-jazzy-nav2-bringup && \
    apt clean && rm -rf /var/lib/apt/lists/*

# Setup locale
RUN apt update && apt install -y locales && \
    locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL=en_US.UTF-8

# Explicit ROS environment
ENV ROS_DISTRO=jazzy

# Confirm Python version
RUN python3 --version

# Default shell
CMD ["/bin/bash"]
