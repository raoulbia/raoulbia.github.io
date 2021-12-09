Title: Azure General Security Features
Date: 2018-03-25
Category: Cloud
Slug: azure_general_security
Summary: Azure General Security Features
Status: draft

<br>

## General Security

also see [Azure General and Network Security](https://raoulbia.github.io/azure_general_and_network_security.html)


* Azure Security Centre
	* monitors and protects
		* Policy compliance of **your** resources
	    * Security alerts (as opposed to alerts for say new VM created)
	    * Secure score
	    * Resource hygiene
	* ties in with Azure Advisor
	* Can be installed on-prem as “security agents”
    
* Key Vault
	* Centrally store your secrets, keys, certificates, DB password
    * **NOT security token** (which is related to AD authentication)
	* Grant access to a program at run time
	* Can generate keys within Key Vault

* Azure Sentinel
    * for deeper investigation into security incidents
	* Centralises all the **log files** from various resources
	* Analyses them to detect threats
	* Allows you to **run queries on those logs**
	* Investigate an incident
	* Orchestration and automation to fix issues

*  Azure Dedicated Host
	* Hardware that is dedicated only to you e.g. I want the computer or network that my VMs are running not to be shared with any other customer


