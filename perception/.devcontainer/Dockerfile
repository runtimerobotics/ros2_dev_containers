# Base Image
FROM osrf/ros:jazzy-desktop-full

# Set noninteractive for automation
ENV DEBIAN_FRONTEND=noninteractive

# Update system & install base dependencies
RUN apt update && apt install -y \
    python3-pip \
    curl \
    gnupg2 \
    lsb-release \
    vim \
    mesa-utils \
    libgl-dev \
    libglu-dev \
    xterm \
    iputils-ping \
    net-tools \
    libserial-dev && \
    apt clean

# Ensure ROS 2 sources (just in case)
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add - && \
    echo "deb http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list && \
    apt update

# Install OpenCV, PCL, and bridge packages
RUN apt install -y \
    ros-jazzy-cv-bridge \
    ros-jazzy-image-transport \
    ros-jazzy-pcl-ros \
    ros-jazzy-pcl-conversions \
    libopencv-dev \
    libpcl-dev

# Set up locale
RUN apt install -y locales && \
    locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Source ROS 2 on container start
RUN echo "source /opt/ros/jazzy/setup.bash" >> /root/.bashrc

CMD ["/bin/bash"]
