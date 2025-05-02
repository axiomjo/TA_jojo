hariini w pake terminal, ngetik tanpa liat layar mycobot.


lappy -> kabel ethernet -> rasppi mycobot  

buka terminal (CTRL + ALT + T)  

di raspi ketik  
`sudo ip addr add 169.254.0.1/16 dev eth0`

trus cek  
`ping 169.254.0.1`

trus nyalain ssh  
`sudo systemctl enable ssh`

trus start ssh
`sudo systemctl start ssh`  

pindah ke terminal lappy  
`ssh er@169.254.0.1`  

masukin password
`Elephant`

NOW U CAN CONTROL MYCOBOT LEWAT LAPPY! HAHAHAHA!

---
# 💻 CARA SUPAYA BISA GUI
u can open more terminals, just ssh again.  
  
pindah ke terminal lappy  
`ssh -Y er@169.254.0.1`  

  if ga -X ato -Y, bakal errror
er@er:~/colcon_ws$ ros2 run turtlesim turtlesim_node
qt.qpa.xcb: could not connect to display 
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, xcb.

---
# disaranin ganti static IP coz yg itu 169.x.x.x masuk kategori **link-local addressing**. oh....



