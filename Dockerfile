FROM ubuntu:24.04

# Set environment variables to avoid user interaction during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install Qt, build tools, and X11 libraries
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    ninja-build \
    qmake6 \
    g++ \
    gdb \
    clang-format \
    pkg-config \
    qt6-base-dev \
    qt6-tools-dev \
    qt6-tools-dev-tools \
    qtcreator \
    libqt6svg6-dev \
    libgl1-mesa-dev \
    libglu1-mesa-dev \
    x11-apps \
    mesa-utils \
    libboost-all-dev \
    git \
    nano \
    vim \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Set up working directory
WORKDIR /app

# Set environment for Qt and X11
ENV DISPLAY=host.docker.internal:0.0
ENV QT_X11_NO_MITSHM=1

# Command to keep container running or start Qt Creator
CMD ["/bin/bash"]

