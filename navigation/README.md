# ros2_dev_containers
This repository consist of Dev containers files of ROS 2 for Simulation, Navigation and Manipulation
# NAVIGATION 
 
ROS 2 Navigation Dev Container (Jazzy + Ubuntu 24.04)
This project provides a pre-configured Dev Container for developing with the ROS 2 Navigation Stack (Nav2) using ROS 2 Jazzy on Ubuntu 24.04 .

It uses Docker + Visual Studio Code Remote - Containers extension to provide a consistent, isolated development environment for ROS 2 navigation applications.

🧩 Features
ROS 2 Jazzy pre-installed
Navigation Stack (nav2, tb3_simulation)
Rviz2, RQt, and other GUI tools
Ready-to-run simulation example
Works in VS Code with Dev Containers

here
🛠 Requirements
Before proceeding, ensure you have the following installed:

Docker
Visual Studio Code
Remote - Containers extension
Optional: Git for version control
🔧 Setup Instructions
Step 1: Clone This Repository
 https://github.com/runtimerobotics/ros2_dev_containers
 cd ros2-navigation-container

STEP 4: Open in VS Code
Open the folder in Visual Studio Code :

bash
code .
Click on the bottom-left corner of VS Code and select:

"Reopen in Container" 

This will:

Build the container using Dockerfile
Install ROS 2 Jazzy and all required tools
Open a terminal inside the container
Step 3: Verify ROS 2 Installation
Inside the container, verify that ROS 2 Jazzy is available:

source /opt/ros/jazzy/setup.bash
ros2 --version
# Should output something like "ros2 version 0.x.x"

Step 4: Launch Navigation Simulation
source /opt/ros/jazzy/setup.bash
ros2 launch nav2_bringup tb3_simulation_launch.py

This will:

Start Gazebo with TurtleBot3
Load the map
Start the Nav2 stack components (planner, controller, AMCL, etc.)
You can now use Rviz2 to send navigation goals.

Step 5: Run Rviz2 
Open a new terminal in VS Code (still inside the container), then:

bash:
sudo apt update
sudo apt install -y ros-jazzy-rviz2
source /opt/ros/jazzy/setup.bash
rviz2
