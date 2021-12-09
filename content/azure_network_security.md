Title: Azure Network Security
Date: 2018-03-25
Category: Cloud
Slug: azure_network_security
Summary: Azure Network Security
Status: draft

<br>

## Network Security

also see [Azure General and Network Security](https://raoulbia.github.io/azure_general_and_network_security.html)

* Azure Virtual Network
    * is the fundamental buidling block of your private network in Azure.
    * enables resources (e.g. VMs) to securely communicate w/each other, the internet and on-prem networks.
    * similar to traditional network
    * to ensure that to VMs cannot communicate w/ech other they must be deployed in separate VN's.
    * VN's are FREE but are tied to VM's therefore removing a VN does not reduce cost.
	* a VN can be divided into subnets

* Azure Firewall
    * is a managed network security service
    * protects Azure Virtual Network resources	
    * can be implemented to secure multiple VNs
    * built-in high availability and unrestricted scalability
    * Is an application gateway device
	* has "threat intelligence" option to automatically block traffic: analyse traffic to see if it matches certain known bad patterns e.g. SQL injections, cross-site scripting
    * NOT used for encryption
    * NO reports

* Network Security Groups (NSG)
	* to allow applications to be accessed over HTTP
    * controls traffic to and from resources in an Azure Virtual NEtwork.
	* NSG is a static set of rules that protects each subnet
		* list of IP addresses, port numbers, source and destination that are allowed through
	* Aka **“access control list”**
	* It’s **Deny by default** setup where you have to specifically allow traffic through
    * NOT used for encryption

* VPN Gateway
	* connecting two or more networks AS IF they were on the same network
	* uses a network gateway
	
* Virtual Network Peering
	* used to link virtual networks
  
* ExpressRoute
    * lets you extend on-prem network to the cloud
    * **dedicated private connection that doesn't travel over the internet**
	* high speed private connection similar to VPN
	* does NOT run on public cloud
    * does NOT provide encrypted network communication


* Network Interface (NIC)
    * tied to VM
    * removing it will NOT reduce cost
    
* Local Network Gateway
	* used to represent a VPN device in your local network
    * used for site-to-site VPN connection between Azure Virtual Network and on-prem local network
   
* Private Cloud Network
    * operated within a company's firewall

* DDoS protection
    * secures websites from attacks and generates reports that contain details of attempted attacks.
	* Basic
        * always on 
        * free basic level DDoS that applies to everybody
	* Standard
		* not free
		* for you specifically
		* real-time atttack metrics

* Encryption
    * must install *Remote Access Server* for VPN.

* Defence in depth
	* Best/recommended protection form all different sides, not just the front door!
	* Instead of having a single firewall or security point that enforces security, defence in depth allows to **enforce security at different levels within your group of resources**:
		* Data: virtual network endpoint
		* Application: API management
		* Compute: limit remote desktop access, windows update
		* Network: network security group, subnets, deny by default
		* Perimeter: DDoS, firewalls
		* Identity and Access: Azure Active Directory
		* Physical: doors, keys 
