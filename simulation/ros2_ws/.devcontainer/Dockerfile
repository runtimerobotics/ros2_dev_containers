
# # Base Image
# FROM osrf/ros:jazzy-desktop-full

# # Always set noninteractive for safe installs
# ENV DEBIAN_FRONTEND=noninteractive

# # Update package lists
# RUN apt update

# # Install common tools, Gazebo, and MoveIt
# RUN apt install -y \
#     python3-pip \
#     mesa-utils \
#     libgl-dev \
#     libglu-dev \
#     xterm \
#     iputils-ping \
#     net-tools \
#     vim \
#     ros-jazzy-ros-gz \
#     ros-jazzy-moveit \
#     ros-jazzy-moveit-plugins \
#     ros-jazzy-moveit-resources-panda-moveit-config

# # Setup locale
# RUN apt install -y locales && \
#     locale-gen en_US.UTF-8 && \
#     update-locale LANG=en_US.UTF-8

# ENV LANG en_US.UTF-8
# ENV LANGUAGE en_US:en
# ENV LC_ALL en_US.UTF-8

# # Explicit ROS env
# ENV ROS_DISTRO=jazzy

# # Confirm Python version: should be 3.10.x
# RUN python3 --version

# # Default shell
# CMD ["/bin/bash"]


# Base Image
FROM osrf/ros:jazzy-desktop-full

# Always set noninteractive for safe installs
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists
RUN apt update

# Install common tools, Gazebo, MoveIt, Navigation2, clang-format, and libserial
RUN apt install -y \
    python3-pip \
    mesa-utils \
    libgl-dev \
    libglu-dev \
    xterm \
    iputils-ping \
    net-tools \
    vim \
    ros-jazzy-ros-gz \
    ros-jazzy-moveit \
    ros-jazzy-moveit-plugins \
    ros-jazzy-moveit-resources-panda-moveit-config \
    ros-jazzy-nav2-bringup \
    libserial-dev \
    ros-jazzy-ament-cmake-clang-format

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
