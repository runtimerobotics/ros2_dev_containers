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

## ⚙️ Prerequisites

Make sure the following tools are installed on your system:

| Tool | Version | Link |
|------|---------|------|
| [Docker](https://www.docker.com/) | Latest | Docker Desktop or Docker Engine |
| [Visual Studio Code](https://code.visualstudio.com/) | Latest | Code Editor |
| [Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) | Latest | VS Code Extension |

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
