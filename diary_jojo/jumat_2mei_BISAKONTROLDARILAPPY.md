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
# 📑 cara set static ip mycobot selamanya  

kan pake tipe **point-to-point ethernet connection**,

  dan mepinginnya  
  ip address RASPBERRY PI mycobot = 169.254.0.1  

so, di mycobot,buka terminal (CTRL + ALT + T)  

edit file YAML( YAML Aint Markup Language) netplan pake `nano` di terminal  
`sudo nano /etc/netplan/01-network-manager-all.yaml`  

ganti semua isinya (ato komen pake #) jadi  
`network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      dhcp4: no
      addresses: [169.254.0.1/16]
`  

Save (Ctrl+O, Enter)

trus keluar dari `nano` (Ctrl+X)  

trus apply config  
`sudo netplan apply`  

trus reboot mycobot
`sudo reboot`  

trus ntar sambungin kabel ethernet langsung ke laptop kita deh.
trus yg ssh supaya bisa GUI.

DAH. OTOMATIS NYAMBUNG GPERLU NGETIK2 DI MYCOBOT LAGIIIII. :>





