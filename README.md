# micromouse_simulator
This is a simulator for micromouse competition held by IEEE-HTI Student branch 
## Introduction 
This simulation is based on gazebo and ros.The maze itself is designed on solidworks and exported as stl file added to .world file to be launched as the default maze . you can add your custom maze by modifing the maze.sldprt and export it as stl to the meshes directory. 
The robot is written as a xacro file to silulate an abstract version of the real robot and can be easily modified by changing the dimension in the file.

The file Tree is devided into two main folders each folder represent a package : 
/src
     /my_simulation
     /mazebot
my_simulation folder contains the launch file forthe gazebo and the world data, mazebot folder contains the robot urdf/xacro file and all the robot ros nodes used for movement, navigation and observation. These nodes are used to communicate with the decision making layer of the physical robot algorithm to simulate the robot's interaction with the gazebo environment. in summary these nodes will provide the algorithm to be simulated with localization data and distance sensors readings. and recieves from the robot the coordinates to which the robot should move or the next movement in the grid.
change
