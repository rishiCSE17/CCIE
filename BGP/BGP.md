# Chapter 1 : BGP Foundation
* BGP - the biggest routing protocol in the world

## What is BGP
* Routing protocol of the internet 
    > Exterior Routing Protocol (Earler it was EGP, phased out eventually)
* Management of Trust 
    >  for IGP there exists a implicit trust mechanism <br>
      BGP doesnt trust any body, even with neighbours it takes all measure to safe its AS <br>
      this is because BGP makes neighbours with external networks 
* Routing through autonomous systems (AS) instead routers
    > "Cloud is nothing without Datacenters" - Juniper <br>
    Everything ends with a Router 
* Slowest Routing protocol in the world 
    > by design it's not a fast protocol <br>
    BGP can't be superfast & Reactive (for this we've EIGRP) <br>
    In BGP, if route goes down, it waits for 30 secs. this is to prevent propagation of flapping <br>
* BGP is more for ISP not enterprise customer network 

## BFP  talks between AS 
* AS : One or more network, managed by a single entity (e.g. intel is known as 442), 
however for some cases its managed by several orgs 
* Essencially, an AS comprises of a number of routers, having assigned with a public IP
address (220.5.1.0/24)
* 