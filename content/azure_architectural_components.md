Title: Azure Architectural Components
Date: 2018-03-28
Category: Cloud
Slug: azure_architectural_components
Summary: Azure Architectural Components
Status: draft


<br>

### Architectural componets


* Regions and Region Pairs
    * Microsoft Azure datacenters are organized and made available by *Regions*
	* (geo) regions (60+) and region pairs
	* Pairs are in same geography
	* Data connection btw pairs is fastest speed available i.e. lowest latency
	* SW rollouts are deployed to one region of a pair and the other is not touched
	* If multiple regions go down, one region of each pair is treated as a priority 
	* Put your backups into the paired region!

* Availability Zones
	* attached to the concept of **data centre failure**
		* Physically separated from each other, running on its own power, its own heating and cooling and on its own network
        * same land, different building
	* NOT available in all regions: if you have VMs in all regions doesn't mean you can avail of availability zones for all VMs
	* two or more availability zones within one region!
	* An application can be deployed to multiple availability zones 

* Availability Sets
	* it is recommended availability sets for two or more VMs
	* logical grouping of VMs that allow Azure to understand how your application is built to provide
	for redundancy and resilience.
	* no cost

* Azure Subscriptions
	* billing unit
    * is an object that represents a "folder" that you can put resources in
    * Azure subscriptions provide you with authenticated and authorized access to Azure products and services and allows you to provision resources. An account can have multiple subscriptions, one for each department, that have different billing models and to which you apply different access-management policies.
    * can be transferred but to merged
    * only one admin per subscription
    * Micrososft account (email) only
	* support plans
		* basic support plan with free account
		* standard support plan gives access to support engineer phone / email
	* one account holder can have multiple subscriptions
	* ability to have different levels of access to different subscriptions e.g. owner or global admin vs. contributor
	* **a resource must be associated with a subscription**
    * Gold is highest subscription tier,
    * subscription templates: Azure Blueprints; have pre-defined roles and policies

* Resource 
	* is an instance of some azure service
    * **inherits permissions configured at the resource group level**
    * if you delete a resource group, all the resources in the group will be deleted
    * if VM has a read-only lock applied, you can add a Delete lock as well
    * do NOT inherit tag applied at resource level

* Resource groups
	* **logical groupings of related things** e.g. by subscriptions, project, people who work on a project, ...
    * from here can contro RBAC and compliance (policies)
    * can manage compliance of resources across multiple subscriptions
	* can be used to delegate RBAC permissions to several VMs simultaneously
    * Respurce groups provide organizations with the ability to **manage the compliance** of Azure resources across multiple subscriptions
	
* Management groups
	* a hierarchy of subscriptions;
	* used to organise subscriptions
	* can be nested
	* good for setting varying **policies** depending on the users of the subscription 
	* i.e. apply rules to groups rather each individual subscription
	* can be viewed as a **governance model**

* Tags
    * let you organise resources and resource grousps 
    * name:value pairs
    * is metadata

* Azure Resource Manager (ARM)
	* resource deployment model that underlies all resource creation or modification
	* no matter whether you use, the portal, PowerShell, or the SDK, ARM takes those commands and executes them


