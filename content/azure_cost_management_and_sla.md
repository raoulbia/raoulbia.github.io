Title: Azure Cost Management and SLA
Date: 2018-03-23
Category: Cloud
Slug: azure_cost_management_and_sla
Summary: Azure Cost Management and SLA
Status: draft

<br>

## Availability SLA

* 99.99% for all PaaS services 
    * Daily: 8s
    * Weekly: 1m
    * Monthly: 4m
    * Yearly: 50m

* 99.95% for Availability Sets of two or more VMs

<br>

## Account Types 
    
* Free 
    * can be used for Prod!
    * Azure Free account has a limit for the amount of data that can be uploaded to Azure
    * A basic support plan is included in an Azure free account
    * All Azure free accounts expire after a certain period

* Pay-as-you-Go

## Support Plans

* Basic
* Developer
* Standard
* Professional Direct: Microst provides regular architectural reviews

<br>

## Factors that affect cost

* Resource types
	
	* Different services are billed based on different factors

    * to see service costs, go to "Subscription" > "Invoices"
	
	* Free resource types
        * **Private IP address**
	    * Resource groups
	    * Virtual network (up to 50)
	    * Load balancer (basic)
	    * Azure AD (basic)
	    * Network Security Groups (NSG) ; recall also aka “access control list”
	    * Free-tier web-apps (up to 10)
	    * Azure functions 
	    	* **opportunity for cost savings**
	    	* 1M executions free per month
	        * 0.20$ per million executions
	        * Compare that to Cheapest VM is 20$ per month…
	
	* Metered costs: time, GB, CPU utilisation, nbr of executions	   		 
	    * Pay per usage (consumption model) e.g. 1M function runs
	        * Functions
	        * Logic apps
	        * Storage (per 
	        * Ingress and egress traffic
	            * Outbound bandwidth (5GB free)
	            * Inbound data is free
	        * Cognitive Services API	    
	    * Pay for time
	        * VMs: pay per second + pay for storage    
	    * Location
	
	* Stability in pricing
	    • Pay fixed price per month for computing power or storage, whether you use it or not
	    • Discount for reserved VM instance (1yr, 3yr)
	    • Multi-tenant or isolated environment 

<br>
          
## Factors that can reduce costs

* Azure Adisor (see settings > cost tab)
* Alerts when billing exceeds a certain level (doesn’t stop the services)
* Auto shutdown of resources when not being used
* Utilise cool/archive storage where possible
    * E.g. for backup files
* Reserved instances
    * If you know you are going to use your VM for the coming year
    * 20%+ savings
* Use policy to restrict access to certain expensive resources
* Auto scaling
* Ensure every resource has an owner (tags) ; all resources are accounted for
* Spot pricing
    * Ability to use VMs for discounted price when nobody is using them
    * Bidding on low-priced VM time
* Hybrid use benefit: related to on-prem

<br>

## Pricing calculator [link](https://azure.microsoft.com/en-us/pricing/calculator/)

* Configurable options
    * Region,
    * Tier,
    * Subscription type
    * Support options
    * Dev/test pricing
* Can save and share

<br>


## Azure Cost Management

* [Total Cost of Ownership calculator](https://azure.microsoft.com/en-ca/pricing/tco/calculator/)
* Cost management and billing section
* Track spending over time






