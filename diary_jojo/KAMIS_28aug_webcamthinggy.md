ok, jadi ternyata, webcamku klo di beda laptop, bisa beda port(?) 

kyk di lappy lama, kan /dev/video0 klo gasala.  
tapi klo di lappy yg satunya, bisa /dev/video2.  

# jadi supaya tau mana yg mana, pake command
`v4l2-ctl --list-devices`  

---
trus nanti bakal dapet output  
```
WEB CAM: WEB CAM (usb-0000:00:14.0-1):
	/dev/video2
	/dev/video3

Integrated_Webcam_HD: Integrate (usb-0000:00:14.0-12):
	/dev/video0
	/dev/video1
```  
ntar bisa dipake buat masuk parameter buat node usb_cam_node. rn aku pake  
```ros2 run usb_cam usb_cam_node_exe --ros-args --remap __node:=usb_cam_1 --remap /image_raw:=/cam1_nih_boss/image_raw --remap /camera_info:=/cam1_nih_boss/camera_info -p video_device:="/dev/video2"```  
btw iku one-line command.  
panjang gegara remappingnya di sana :v  

nah trus, krn ros2 udh punya package gg kyk gini, package yg image publisher nya diapus aja kyknya?

<img width="1920" height="1080" alt="28aug_opsicamera" src="https://github.com/user-attachments/assets/c55cc99f-e8be-4a70-8491-cd64c5563859" />
