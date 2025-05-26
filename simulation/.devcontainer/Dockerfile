# Start from the official ROS 2 Jazzy base image (Ubuntu 24.04).
FROM ros:jazzy

# Set environment variables to avoid locale warnings and ensure non-interactive apt.
ARG DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# This Dockerfile defines the base image and basic dependencies.
# The `remoteUser` and `features` in devcontainer.json will handle user creation,
# switching to that user, and installing more common tools like `sudo`, `git`, etc.

# Install any core apt packages required BEFORE the user is created.
# This should be minimal, usually just things like 'git' if needed for image build itself.
RUN apt-get update && apt-get install -y \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# The Dev Container will then set the 'remoteUser' (e.g., 'ros')
# and execute the remaining commands as that user.
# Therefore, we *don't* put 'USER ros' or explicit useradd here.
# Let `devcontainer.json` take full control of the user.