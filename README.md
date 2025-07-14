# Devcontainers for Simulation, Navigation, Manipulation,Perception

**Devcontainers** are portable, reproducible development environments defined using configuration files. They allow developers to easily share and run consistent setups for tools, libraries, and dependencies inside isolated containers.

## Features

- 🧰 **ROS Dev Tools:** Supports GUI tools like rqt, rviz2, gz sim, MoveIt, and other ROS developer tools.
- 🛠 **Simulation:** Run and test simulation scenarios in an isolated environment.
- 🗺️ **Navigation:** Develop and test navigation pipelines reproducibly.
- 🤖 **Manipulation:** Build, test, and iterate on robotic manipulation modules.
- 🖥️ Supports GUI tools: **rqt**, **rviz2**, **gz sim** , **moveit**
- 👀 Perception: Integrate and test perception pipelines for sensors and vision systems.

## Project Structure
```bash
ros2_dev_containers/
├── ros_dev_tools/
├── perception/
├── manipulation/
├── navigation/
├── simulation/
└── README.md
```
## How to Use Devcontainers

### Prerequisites

To use these Devcontainers, you’ll need:

- ✅ **Docker:** Install [Docker](https://www.docker.com/) to run containers on your system.
- ✅ **Visual Studio Code (VS Code):** Install [VS Code](https://code.visualstudio.com/).
- ✅ **Dev Containers Extension:** Install the **Dev Containers** extension for VS Code.
  
---
# ros_dev_tools  Devcontainer
### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/runtimerobotics/ros2_dev_containers.git
   cd ros2_dev_containers/ros_dev_tools/ros2_ws
   ```
2. **Reopen in Container**
  Open the Command Palette (Ctrl+Shift+P) and run:
      ```bash
      Dev Containers: Open Folder in Container 
      ```
      then select ros_dev_tools folder
3. **Stay in the Workspace**
   If not open your terminal inside the devconatiner and navigate to:
   ```bash
    cd ros2_dev_containers/ros_dev_tools/ros2_ws
   ```
4. **Source the ROS Environment**
   Run
   ```bash
   source /opt/ros/jazzy/setup.bash
   ```
5. **Test Basic Commands**
   Verify that your devcontainer works by trying:
   ```bash
   ros2
   rqt
   rviz2
   gz sim
   ```
6. **Note for GUI Tools (rqt, rviz2, gz sim)**
   If GUI tools are not displaying properly, allow local network connections for X11 with:
   ```bash
   xhost +local:
   ```
   ✅ Do this on your host machine terminal (not inside the container).
   After you finish using the Devcontainer, disallow local connections for security:
   ```bash
   xhost -local:
   ```
## 🧩 Test the Sample Simulation
1. **A sample simulation package is already placed in the src folder.**
  To test it:
  Clean up previous builds using
   ```bash
   rm -rf build/ install/ log/
   ``` 
2. **Build and Run**
 Navigate to your workspace root:
   ```bash
      cd ros2_dev_containers/ros_dev_tools/ros2_ws
      colcon build
      source install/setup.bash
      ros2 launch andino_gz andino_gz.launch.py
   ```
3. **Troubleshooting**
If you get errors about missing or broken packages, install the required packages inside the container, then rebuild and try again.

## 🧩 Create and Test Your Own Packages

You can create your own ROS 2 packages inside the src/ folder:
  ```bash
      cd ros2_dev_containers/ros_dev_tools/ros2_ws/src
      ros2 pkg create --build-type ament_python my_new_package
      cd ..
      colcon build
      source install/setup.bash
   ```
Then test your simulation launch files or nodes as needed.
## 🧪 How to test OpenCV

To verify OpenCV is installed and working, run a test script like:

```bash
# ✅ Check if OpenCV Python is installed
python3 -c "import cv2; print(cv2.__version__)"
# ✅ Check if OpenCV ROS bindings (cv_bridge) are installed
ros2 pkg list | grep cv_bridge
```
## ✅ Checking if PCL is installed
1️⃣ Check the ROS PCL package

To verify that the ROS PCL package is installed (for example, pcl_ros):
 ```bash
   ros2 pkg list | grep pcl
   ```
You should see output like:

pcl_conversions
pcl_msgs
pcl_ros

## Simulation DevContainer
### Steps

1. **Clone the Repository**
```bash
      git clone https://github.com/runtimerobotics/ros2_dev_containers.git
      cd ros2_dev_containers/simulation/ros2_ws
```

3. **Reopen in Container**
  Open the Command Palette (Ctrl+Shift+P) and run:
      ```bash
      Dev Containers: Open Folder in Container
      ```
      then select the simulation folder
4. **Stay in the Workspace**
   If not open your terminal inside the devconatiner and navigate to:
   ```bash
    cd ros2_dev_containers/simulation/ros2_ws
   ```
5. **Source the ROS Environment**
   Run
   ```bash
   source /opt/ros/jazzy/setup.bash
   ```
  ## test the Sample Simulation tools
   ```bash
   ros2
   rqt
   rviz2
   gz sim
   ```
--------------------------------------------------------------------- NAVIGATION ---------------------------------------------------------------------

## Navigation DevContainer
### Steps

1. **Clone the Repository**
    ```bash
      git clone https://github.com/runtimerobotics/ros2_dev_containers.git
      cd ros2_dev_containers/navigation/ros2_ws
      ```
3. **Reopen in Container**
  Open the Command Palette (Ctrl+Shift+P) and run:
      ```bash
      Dev Containers: Reopen in Container
      ```
4. **Stay in the Workspace**
   If not open your terminal inside the devconatiner and navigate to:
   ```bash
    cd ros2_dev_containers/navigation/ros2_ws
   ```
5. **Source the ROS Environment**
   Run
   ```bash
   source /opt/ros/jazzy/setup.bash
   ```
## test the Sample Navigation Stack
   **A TurtleBot3 navigation launch file is included for quick testing**
  To test it:
  Clean up previous builds using
   ```bash
   rm -rf build/ install/ log/
   ``` 
**Build the Workspace**
```bash
cd ros2_dev_containers/navigation/ros2_ws
colcon build
source install/setup.bash
```

## Launch Navigation
```bash
ros2 launch nav2_bringup tb3_simulation_launch.py
```
**Note for GUI Tools (rqt, rviz2, gz sim)**
   If GUI tools are not displaying properly, allow local network connections for X11 with:
   ```bash
   xhost +local:
   ```
   ✅ Do this on your host machine terminal (not inside the container).
   After you finish using the Devcontainer, disallow local connections for security:
   ```bash
   xhost -local:
   ```

It will open Like :
<img width="1341" height="621" alt="Screenshot 2025-06-28 163834" src="https://github.com/user-attachments/assets/164ac4c9-da5b-416c-8d74-9c5cf2b07c0a" />


## Create and Test Your Own Navigation Packages
**You can create your own packages inside the src/ folder.**

```bash
cd ros2_dev_containers/navigation/ros2_ws/src
ros2 pkg create --build-type ament_python my_nav_pkg
cd ..
colcon build
source install/setup.bash
```

**Then, test your nodes or launch files with:**
```bash
ros2 launch my_nav_pkg my_nav_launch.py
```


## Troubleshooting
If you encounter errors such as missing packages:
Use **apt** inside the container to install them
Then rebuild using:
```bash
colcon build --symlink-install --event-handlers console_direct+
source install/setup.bash
```



# 📘 Manipulation Dev Container – ROS 2 MoveIt 2 (Panda Robot)

## 🔧 Project Overview

This repository provides a complete **ROS 2 Jazzy** development container (Dev Container) environment preconfigured for robotic **manipulation tasks** using **MoveIt 2** and the **Panda robot**.

Developed using Docker and VS Code, this environment allows seamless building, testing, and visualization of motion planning without the need for native setup.


## 📂 Repository Clone Instructions

```bash
git clone https://github.com/runtimerobotics/ros2_dev_containers.git
cd ros2_dev_containers/manipulation
```

---


## 🚀 How to Run the Dev Container

1. Open the folder in **Visual Studio Code**.
2. When prompted, click on: ✅ **“Reopen in Container”**

VS Code will now:
- Build the container from `.devcontainer/Dockerfile`
- Mount the project into `/workspaces/manipulation_ws`
- Set up the ROS 2 Jazzy environment with MoveIt 2

---

## 📦 Build the Workspace

Once inside the container terminal:

```bash
cd /workspaces/manipulation_ws
colcon build
```

After the build finishes:

```bash
source install/setup.bash
```

---

## 🤖 Launch Panda Robot with MoveIt 2

```bash
LIBGL_ALWAYS_SOFTWARE=1 ros2 launch moveit_resources_panda_moveit_config demo.launch.py
```

> This command uses **software rendering** to make RViz work inside Docker.

---

## 🧪 RViz Usage

- The Panda robot will be displayed in RViz.
- Use the “Planning” tab to:
  - Plan to a pose
  - Execute motion
- Try planners like OMPL, CHOMP, Pilz, STOMP

---

## ✅ Included Components

| Component | Purpose |
|----------|---------|
| `moveit_resources_panda_description` | URDF/Xacro of the Panda robot |
| `moveit_resources_panda_moveit_config` | MoveIt configuration |
| `panda_arm_controller` | JointTrajectoryController |
| `panda_hand_controller` | GripperActionController |
| `joint_state_broadcaster` | Publishes joint states |

---

## 🛠 Troubleshooting

| Issue | Fix |
|-------|-----|
| RViz not showing robot | Use `LIBGL_ALWAYS_SOFTWARE=1` before `ros2 launch` |
| Controller overrun warnings | Safe to ignore for most simulations |
| Missing 3D sensor plugin | Not required unless doing octomap-based collision |

---


# Perception  Devcontainer



## 🧠 ROS 2 Perception Setup (Dev Containers)
This README provides instructions for setting up and working with the Perception Stack inside a ROS 2 Dev Container environment. It includes installation steps for OpenCV, PCL (Point Cloud Library), and relevant ROS bridges.


## 📦 Installed Packages
opencv2 (OpenCV for image processing)
pcl (Point Cloud Library for 3D perception)
pcl_ros (ROS interface for PCL)
image_transport
cv_bridge (OpenCV to ROS image conversion)
pcl_conversions
vision_opencv (Includes cv_bridge and image_geometry)



## 🐳 Steps to Use in Dev Container
1.**Clone and Open in Dev Container**
```bash
git clone https://github.com/runtimerobotics/ros2_dev_containers.git
cd ros2_dev_containers/perception
```
## Use Dev Container: Reopen in Container
2. **Open in Container**
  Open the Command Palette (Ctrl+Shift+P) and run:
      ```bash
      Dev Containers: Open Folder in Container 
      ```
      then select perception folder
3.**Build the Workspace**
```bash
   source /opt/ros/jazzy/setup.bash
```

## 🧪 Test Commands

## ✅ Checking if PCL is installed
1️⃣ Check the ROS PCL package

To verify that the ROS PCL package is installed (for example, pcl_ros):
 ```bash
   ros2 pkg list | grep pcl
   ```
You should see output like:

pcl_conversions
pcl_msgs
pcl_ros
## 🧪 How to test OpenCV

To verify OpenCV is installed and working, run a test script like:

```bash
# ✅ Check if OpenCV Python is installed
python3 -c "import cv2; print(cv2.__version__)"
# ✅ Check if OpenCV ROS bindings (cv_bridge) are installed
ros2 pkg list | grep cv_bridge
```




  





