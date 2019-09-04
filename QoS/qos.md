# Quality of Service (QoS)

# Chapter 1:Introduction 
## Topics 
   1. Brief History of QoS
   2. Underlying requirement 
   3. Deploying Methods 
   4. QoS Toolbelt 

## 1.1.  History of QoS
__1992 Best Effort Service :__ 
  > * First come first served 
  > * Application had internal auto recovery mechanism 
  > * with more customers the process fails 
  
__1994 Integrated Services :__
  > * Reservation protocol (RSVP) - reservres bandwidth for communication 
  > * a specific amount of bandwidth is reserved in all routers along a path 
  > * with customer with asymmetric needs, failed the process
  
__1996 Differentiated Service :__
  > * Per hop mechanism for prioritising traffic  
  > * re-prioritization based on various marking 
  
__1998 MPLS/VPN QoS :__ 
  > * allows SP to route at layer 2

__2002 Cisco Auto/template QoS :__
  > * one button many option ! 

__2004 QoS for security :__
  > * Network based application recognition (NBAR) 
  
## 1.2 QoS Requirement 
QoS is not universal rather specific to network traffic type. 
* Data
    >1. Unpredictable - Depends on application

* Voice
    >1. Predictable : G.711 audio codec demands 80kbps/call (no sudden flood)
    >2. Smooth : Constant stream of traffic
    >3. Benign : Once start consuming traffic does'nt ask for more 
    >4. Drop/Delay
    
* Video 
    >1. Predictable : Bursty 
    >2. Greedy : allocates as much as bandwidth it gets 
    >3. Drop/Delay :
    
### Challanges in QoS 
1. Lac of bandwidth - More bandwidth solves problem immediately, <br>
bit it costs, QoS is meant to combat temporary congestion (next 3 points), not suitable for consistent congestion 
2. Packet loss - 
3. Delay - ITU Standard 150ms (RTT : 300ms) for PSTN
4. Jitter - Delay variation 

## 1.3. Deployment method 
1. __CLI__
   >* Legacy way 
   >* Interface wise configuration is time consuming and redundant  
2. __Modular QoS CLI (MQC)__
    >* Preffered approach
    >* creates groups interface and policy then apply policy on interface group (Policy map)
3. __Auto QoS__
    >* you dont start from scratch 
    >* start with auto and change what is needed 
4. __QoS Policy Manager (QPM)__
    >* GUI based 
    >* Easy to troubleshoot 
 
## 1.4. QoS Toolbelt
1. __Classification and marking tools__
    > * classification involves identifying and grouping different traffic types
    > * Marking is to tag packets based on the policy applied for quick recognition 
2.  __Policing and Shapping__
    > * Policing drops or mark packet when limit reached
    > * Shapping Queues packet when limit is reached (used in speed mismatching links e.g. FR)
3.  __Congestion Avoidence__
    > * FIFO : trail drops
    > * Random Early Detection (RED) : As buffer begins filling up, start dropping packets randomly 
    > * Weighted RED (WRED) : Cisco doesn't support RED, rather demands every packets must be marked with weight 
    and perform RED on top of it 
 4. __Queuing__
    > * Efficiently order the packet
 5. __Link Efficienly tools__
    > * Compression 
    > * link fragmentation and Interleaving (LFI) : To match MTU 