[LAST EDITED: 2 Mei 2025 12:59]
# 📌 What to Code First (MVP Plan)

##  Step 1: Set Up Basic Robot Communication

- Install ROS2 Galactic and test MyCobot’s movement.

Write a simple ROS2 publisher to send movement commands.

- Verify LAN communication with the MyCobot 280 Pi.
  

##  Step 2: Control the Vacuum Pump

Write a script to turn the vacuum pump on/off via ROS2.

Test picking up and releasing objects manually using commands.

## ✅ Step 3: Display Webcam Feed

- Use OpenCV to capture and display the video feed.
  
- Ensure real-time video streaming on your Qt5 GUI.
  

##  Step 4: Basic Object Detection

Detect a simple object using color or shape detection.

Overlay the detected object's position on the webcam feed.

##  Step 5: Move Robot to Object

Convert detected object position into robot coordinates.

- Move the MyCobot to the object using simple hardcoded movements.
  

##  Step 6: Automate Pick & Place

Combine movement + vacuum pump control to complete one full cycle:

Detect object.

Move arm to object.

Activate vacuum pump.

Lift & move object to a fixed drop zone.

Release object.

---


# bookmarks of yummy resources to eat 

## Ubuntu 
* Ubuntu 20.04 (focal fossa) instalation
https://releases.ubuntu.com/focal/ 

* Intro to Command Line Interface
https://ubuntu.com/tutorials/command-line-for-beginners#1-overview

* how to configure ur Ubuntu system (?) (it's trial and error hahahaha, gonna make this in my TA book)
- problem 1: black screen after rebooting

## ROS2 (Robot Operating System)
-- Intro to ROS2 in Ubuntu  
https://ubuntu.com/tutorials/getting-started-with-ros-2#2-prerequisites

-- ROS2 (Galactic Geochelone) instalation  
https://docs.ros.org/en/galactic/Installation/Ubuntu-Install-Debians.html

-- ROS2 tutorials  
https://docs.ros.org/en/galactic/Tutorials.html

-- Rviz2
https://docs.elephantrobotics.com/docs/gitbook-en/12-ApplicationBaseROS/12.2-ROS2/12.2.4-rviz%E4%BB%8B%E7%BB%8D%E5%8F%8A%E4%BD%BF%E7%94%A8/

-- Gazebo 11 Classic for ROS2 Galactic, Ubuntu Focal
`sudo apt install gazebo11 ros-galactic-gazebo-ros-pkgs ros-galactic-gazebo-ros2-control`

`ros2 launch gazebo_ros gazebo.launch.py`

## Mycobot 280 Pi
-- Mycobot 280 Pi python programming(?)
https://docs.elephantrobotics.com/docs/mycobot_280_pi_en/3-FunctionsAndApplications/6.developmentGuide/python/1_download.html

-- MyCobot 280 Pi with Ethernet cable
https://docs.elephantrobotics.com/docs/gitbook-en/2-serialproduct/2.1-280/2.1.2.2%20Robotic%20Arm%20Electrical%20Interface.html

-- loading the premade URDF file  
punya xacro dulu
download package joint_state_publisher_gui

blurts
-
**Rabu, 30 April 2025**
ok, i gagal daftar prasem kemaren. so, g bisa lulus sem ini. ohwell, it was my mistake anyway, i accept this reality. btw, i feel blank, i dunno what to do now that i have more time to do my TA. but finishing it before July is definitely interesting.  
i think imma make agood presentation for my seminar, one that introduces ROS2 & robotics resources to newbies alike.  

semoga kewujud ya, i think that'll be useful n good. maybe i'll get to teach it to other interested peeps. i hope so :D.

hm, i wanna teach. seems interesting and good to know.

btw, i havent finished my dbs coding camp thinggy, i hope tommorow will do :D

k, bby jo, i love ya. u r loved.

**Rabu, 23 April 2025**  
hariini bisa liat file URDF, launchfiles, executables :D yeeyy
bisa buka kamera lappy juga yeyeeyey


**Senin, 14 April 2025**
learning is learning. isokeh. lesgo finish this, bby!

**Kamis, 10 April 2025**
it's been 2 months now, and im back to learning ROS2. skrg udh sampe tutorial yg "implementing custom interfaces". klo bisa selesain beginner hariini kyknya bagus. klo bisa sampe advanced, lebih bagus lagi. serius seneng bgt akhirnya bisa lanjut balik ke sini T-T. pingin lulus semester ini.  

**Jumat, 14 Feb 2025**
this feels exciting. 
i hope i can finish it well and properly.
i hope i don't sacrifice things that shouldn't be sacrificed.
i hope i do this well enough to pass.

i did not expect that I'll take forever to eat the tutorials 😭. thing is, i feel bleurgh already. like i really don't wanna continue this rn. but i wanna lulus. imma face it again.

ok so, to use the repo by elephant robotics, 
we'll need to understand how to build a workspace in ROS2, which is still quite far from what i ate. oh we got a loooooong way to go.

**Kamis, 13 Feb 2025**
-- very happy coz i can finally build stuff now TvT
today, MY LINUX UBUNTU IS WARAS AND I CAN FINALLY USE THE GUI TvT ! sosososososo happy. 
do i know why it can work? NO HAHAHAHAHA

i still use the nouveau driver,
i purged nvidia-340.

ROS2 already installed. 
next up: connect mycobot to my laptop, and control it with an interface. 
