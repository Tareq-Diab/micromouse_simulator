# micromouse_simulator
This is a simulator for micromouse competition held by IEEE-HTI Student branch 
## Introduction 
This simulation is based on gazebo and ros.The maze itself is designed on solidworks and exported as stl file added to .world file to be launched as the default maze . you can add your custom maze by modifing the maze.sldprt and export it as stl to the meshes directory. 
The robot is written as a xacro file to silulate an abstract version of the real robot and can be easily modified by changing the dimension in the file.

![show](https://user-images.githubusercontent.com/28588004/88641652-c6bfa200-d0bf-11ea-97bc-cd69da7c10a0.gif)


The file Tree is devided into two main folders each folder represent a package : 
/src
     /my_simulation
     /mazerunnerbot
my_simulation folder contains the launch file forthe gazebo and the world data, mazebot folder contains the robot urdf/xacro file and all the robot ros nodes used for movement, navigation and observation. These nodes are used to communicate with the decision making layer of the physical robot algorithm to simulate the robot's interaction with the gazebo environment. in summary these nodes will provide the algorithm to be simulated with localization data and distance sensors readings. and recieves from the robot the coordinates to which the robot should move or the next movement in the grid. the next figure demonstrate the data flow between the nodes and algorithm.

 ![figure 1](https://github.com/Tariq96/micromouse_simulator/blob/master/images/node-algorithm%20dataflow.jpg)
 
 The localizer node is deseined with a P-controllerr to controll the linear and angullar speed of the robot with a Kp set as a variable in the localizer.py file , you can change it with your own values after tuning them on your own robot if you changed the robot configurations.
 
#### P-controller Diagram
 ![figure 1](https://github.com/Tariq96/micromouse_simulator/blob/master/images/P-controller.jpg)

the next graph demonstrate p-controller response for moving from  cell [0,0] to cell [5,0] ,notice that the response in the grapgh is for the linear error only the anguler error is not show in the grapgh as  it's irrelevent becouse the movement is mostly linear and anguler controller is used to compensate slipping of the wheel and unwanted anguler movements.
![figure 1](https://github.com/Tariq96/micromouse_simulator/blob/master/images/p_controller_response.png)
