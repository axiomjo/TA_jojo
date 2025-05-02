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
