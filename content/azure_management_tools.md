Title: Azure Management Tools
Date: 2018-03-26
Category: Cloud
Slug: azure_management_tools
Summary: Azure Management Tools
Status: draft

<br>

## Azure Management Tools

* portal.azure.com

* Command Line Tools
	* Cloud  Shell
		* Brower-based
		* on Linux, user can opt to run bash, on Windows user can opt to run Powershell
	* Azure PowerShell
		* available on all platforms
		* on Mac it's called *macOS Powershell Core*
	* Azure CLI
        * not supported on iPhone
		* cannot run Powershell
        * can run in Docker container
	* see video 34 @ 2:00 for DEMO


* Azure Advisor 
    * can be configured to only generate recommendations for specified subscriptions and resource groups
    * covers:
     	* Cost 
	    * High availability
	    * Security
	    * Performance
	    * Operational excellence e.g. recommendation on VMs that are not backed up (and allows to do it in a few clicks)
    * NOT network-related recommendations!
    * see video 35 @ 1:20 for DEMO
	
* Azure Monitor
	* to monitor **individual** resources
    * must select a region
	* Useful if you have hundreds of resources
	* Centralised dashboard for (most of) your resources / services
	* Respond: can produce **alerts** e.g. when new VM is created
	* Integrate: can collect and query data from various sources e.g. Apps, logs 
    * Visualise
    * Insights
    * Analyse    

* Azure Service Health
	* Azure Monitor for **Azure infrastructure as a whole** i.e. for regions or services etc
	* Issues that affect all regions or all services / resources (that you also happen to be using)
	* Can add it to your dashboard
	* Has past issues
	* Ability to do **alerts** (SMS, Email, …)


* Azure Resource Manager (ARM) templates
    * automate the simultaneous creation of multiple resources if they are of the same type
	* aka Infrastructure as Code
	* IS A JSON file
	* All actions that you take to manage your Azure resources goes through the ARM layer
	* store all of the infrastructure information in a JSON file as an ARM template and store it within github ()
	* Every time someone wants to change the infrastructure they have to change the template, then re-deploy
	* It’s a way of documenting your infrastructure and how it changes
	* see video 36 @2:50

* Compliance Manager
    * track **your company's compliance** with regulatory standards and regulations

* Azure Mobile App to check resource status, stop/start resources etc

