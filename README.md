Overview: This is a simple robot model that automatically rotates 360 degrees.name is joker1
video
[robat_joker1.webm](https://github.com/user-attachments/assets/2eb9f494-ca55-4462-941f-df35f3f7148b)

Compile:
  1、create a project directory, for example
       mkdir -p ros2_ws/src
  2、Put the directory 'urdf_tutorial_learn' into 'ros2_ws/src'
  3、Run in the ros_2ws directory
       colcon build --symlink-install --packages-select urdf_tutorial_learn
       source install/setup.zsh
run:
  1、Launch the package
      ros2 launch urdf_tutorial_learn demo.launch.py
  2、Open a new terminal, the run Rviz using
       ros2 launch urdf_launch display.launch.py  urdf_package:=urdf_tutorial_learn  urdf_package_path:=joker1.urdf jsp_gui:=false
