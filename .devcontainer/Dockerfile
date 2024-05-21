FROM ubuntu:latest AS ubuntu_container

######################################################################################

# Set up Environmental Variables
ENV DEBIAN_FRONTEND noninteractive
ENV USER="vscode"
ENV HOME="/home/$USER"

# Update packages, install required tools, and clean up
RUN apt update -y \
 && apt install -y \
     sudo \
     openjdk-17-jdk-headless \
     # Linux prerequisites
     curl \
     git \
     xz-utils \
     zip \
     unzip \
     libglu1-mesa \
     # Chrome prerequisites
    #  wget \
    #  gpg \
 && apt autoremove -y \
 && apt clean -y \
 && rm -rf /var/lib/apt/lists/* 

# Create a non-root user and configure sudo for non-password access
RUN useradd -rm -d /home/$USER -s /bin/bash -g root -G sudo -u 1001 $USER \
 && echo $USER ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USER \
 && chmod 0440 /etc/sudoers.d/$USER

USER $USER
WORKDIR $HOME

######################################################################################

# # Chrome
# RUN sudo wget https://dl-ssl.google.com/linux/linux_signing_key.pub -O /tmp/google.pub \
#  && sudo gpg --no-default-keyring \
#         --keyring /etc/apt/keyrings/google-chrome.gpg \
#         --import /tmp/google.pub \
#  && echo 'deb [arch=amd64 signed-by=/etc/apt/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list \
#  && sudo apt update && sudo apt install -y google-chrome-stable \
#  && sudo apt autoremove -y \
#  && sudo apt clean -y \
#  && sudo rm -rf /var/lib/apt/lists/* 

######################################################################################