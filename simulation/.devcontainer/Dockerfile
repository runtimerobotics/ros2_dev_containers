# Base Image
FROM osrf/ros:jazzy-desktop-full

# Always set noninteractive for safe installs
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and add ROS 2 sources to ensure all packages are found
RUN apt update && apt install -y curl gnupg2 lsb-release && \
    curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add - && \
    echo "deb http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list && \
    apt update

# Install common tools, Gazebo, MoveIt, Navigation2, clang-format, libserial, PCL, OpenCV
RUN apt install -y \
    python3-pip \
    mesa-utils \
    libgl-dev \
    libglu-dev \
    xterm \
    iputils-ping \
    net-tools \
    vim \
    ros-jazzy-ros-gz 

# Setup locale
RUN apt install -y locales && \
    locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Explicit ROS env
ENV ROS_DISTRO=jazzy

# Confirm Python version
RUN python3 --version

# Default shell
CMD ["/bin/bash"]




