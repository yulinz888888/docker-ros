FROM ros:kinetic-perception
LABEL Name=ros-jackal Version=0.0.1

RUN apt-get update
RUN apt-get install -y ros-kinetic-robot-localization ros-kinetic-controller-manager ros-kinetic-joint-state-controller ros-kinetic-diff-drive-controller ros-kinetic-gazebo-ros ros-kinetic-gazebo-ros-control ros-kinetic-gazebo-plugins             ros-kinetic-lms1xx ros-kinetic-pointgrey-camera-description ros-kinetic-roslint ros-kinetic-amcl ros-kinetic-gmapping      ros-kinetic-map-server ros-kinetic-move-base ros-kinetic-urdf ros-kinetic-xacro ros-kinetic-message-runtime ros-kinetic-topic-tools ros-kinetic-teleop-twist-joy

WORKDIR /root/
RUN mkdir -p jackal_ws/src 
WORKDIR /root/jackal_ws/src
RUN git clone https://github.com/jackal/jackal.git
RUN git clone https://github.com/jackal/jackal_simulator.git
RUN git clone https://github.com/jackal/jackal_desktop.git
RUN git clone https://github.com/ros-visualization/interactive_marker_twist_server.git

RUN /bin/bash -c '. /opt/ros/kinetic/setup.bash; cd /root/jackal_ws/src; catkin_init_workspace'

WORKDIR /root/jackal_ws
RUN rosdep install -y --from-paths . --ignore-src --rosdistro=kinetic
RUN /bin/bash -c '. /opt/ros/kinetic/setup.bash; cd /root/jackal_ws; catkin_make'
