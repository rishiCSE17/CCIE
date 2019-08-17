# Spanning Tree

## Redundancy and Loops
* Prevents switching loops 
* Original 802.1D for loop prevention 
* Bridge Protocol Data Unit (BPDU) : for probing and loop detection 
* __Boomering__ : 
* __Network Diameter__ : Max hop in a L2 networks. 
    > + Cisco recommends to limit diameter at 7  
    > + BPDU is transmitted (by default) each 2 sec, large diameter may collide two BPDU packets 
* STP doesn't send BPDU on port fast link
    
## Simple Rules of STP 
* BPDU : | Priority | MAC | 
* BPDU type
    > 1. Configuration BPDU : periodic by 2 sec 
    > 2. Topology Change Notification (TCN) : When link change is detected 
    
## Root bridge election 
* Election is based on bridge ID (Lowest ID wins)
    > 1. priority (0-65535, default : 32768), multiple of 4096 (VLAN ID)
    > 2. MAC Address - Back plane MAC (Lower = Older is prioritised)
* an old switch may throttle the CPU with massive STP load, thus priority is changed manually 

## Root Election 
* All ports of RB is Designated Port (DP)
* All NRB switch makes Root Port (RP) that connects RB
* 
![](pics/STP_ports.png)
## STP Path cost 
* STP assigns a cost based on link speed 
    > 4 Mbps    : 250 <br>
     __10 Mbps   : 100__ <br>
     16 Mbps   : 62  <br>
     45 Mbps   : 39  <br>
     __100 Mbps  : 19__  
     155 Mbps  : 14  <br>
    622 Mbps  : 6   <br>
     __1 Gbps    : 4__   <br>
     __10 Gbps   : 2__   <br>
     
## STP States
1. disable  :   down by admin 
2. blocking :   to prevent loops , received BPDU, cant send/receive data
3. listening :   

![](pics/stp%20states.png)    

## STP Timers 
1. __Hello__ : BPDU sent by root bridge 802.1d (2Sec)
2. __Forwarding Delay__ : Spend in listening and learning states (15 Sec X 2 = 30 Sec)
3. __max Age time__ : 20 sec (if not received by 20 sec, means the link has problem)

## Effect of topology change 
![](pics/topo_change.png) 
 _Recalculation of Links takes 30 secs : Not Acceptable !_ 

## Indirect Topology Change 
due to data filter, switch stops receiving BPDU (20 + 2 + 15 + 15 = 52 sec) default 