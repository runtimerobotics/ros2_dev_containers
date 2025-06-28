# Devcontainers for Simulation, Navigation, Manipulation

**Devcontainers** are portable, reproducible development environments defined using configuration files. They allow developers to easily share and run consistent setups for tools, libraries, and dependencies inside isolated containers.

## Features

- 🛠 **Simulation:** Run and test simulation scenarios in an isolated environment.
- 🗺️ **Navigation:** Develop and test navigation pipelines reproducibly.
- 🤖 **Manipulation:** Build, test, and iterate on robotic manipulation modules.
- 🖥️ Supports GUI tools: **rqt**, **rviz2**, **gz sim** , **moveit**

## Project Structure
```bash
ros2_dev_containers/
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
# Simulation Devcontainer
### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/runtimerobotics/ros2_dev_containers.git
   cd ros2_dev_containers/simulation/ros2_ws
   ```
2. **Reopen in Container**
  Open the Command Palette (Ctrl+Shift+P) and run:
      ```bash
      Dev Containers: Reopen in Container
      ```
3. **Stay in the Workspace**
   If not open your terminal inside the devconatiner and navigate to:
   ```bash
    cd ros2_dev_containers/simulation/ros2_ws
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

