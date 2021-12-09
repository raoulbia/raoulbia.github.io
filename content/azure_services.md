Title: Azure Services
Date: 2018-03-28
Category: Cloud
Slug: azure_services
Summary: Azure Services
Status: draft

<br>

### Core Azure Services


#### Compute services 

Compute services execute code in the cloud.

* VMs
	* IaaS 
	* Note: Hypervisor is a program used to run VMs on a computer

* VM Sale Sets
    * create and manage a group of load balanced VMs
    * apps are distributed across multiple instance
 
* Azure App Services
	* PaaS 
	* promise of performance but no access to HW
	* plans and levels
    * size of web app is determined by choice of App Service Plan 
 
* Azure Container Instances (ACI)
	* Single instance
	* fastest and easiest way to deploy code
 
 
* Azure Kubernetes Service (AKS)
	* Runs on a cluster of servers
 	* enterprise grade

 
* Windows Virtual Desktop
	* VM that acts like a desktop
	* Files anywhere

	* to reduce admin effort to create e.g. 50 custom VMs
	
* Misc
    * Vertical scaling – adds more power to your pool of resources
    * Horizontal scaling – adds more machines to your pool of resources
    * Resiliency – is the ability of a system to recover from failures
    * Fault Tolerance – is the ability for a system to remain in operation

<br>

#### Protection services

* Distributed Denial of Service (DDoS) attack protection
* Azure Firewall (allow/block traffic)
* Network security groups (access control list, IP whitelisting)

<br>

#### Monitoring services

* Network Watcher, ExpressRoute monitor, Azure Monitor
* also see (Azure Management Tools)[https://raoulbia.github.io/azure_management_tools.html]  

                
#### Storage services 

* is Iaas
  
* Azure Storage Account
	* *V2* is most common: Blobs, Tables, Queues, files
	* Azure data lake storage (**cheapest**, 1.8 cent per GB)
  
* Storage Account access tiers
	* Hot for real time access
	* Cool: for rare access
	* Archive: cheapest for storing , most expensive for accessing; for regulatory requirements
  
* Storage Account Performance tiers for faster access

* Different locations have different prices for storage

* Replication / Redundancy: by default Microsoft keeps three copies of every file but can be increased to six
	* Can set up failover: files available in other regions in case of issues
    
* Types of storage services
	* Blob Storage
        * Azure VM Disks
        * best option for storing disaster recovery files and archives.
    * File Storage
    * Queue	Storage
    * Disk storage
        * managed
        * pay for reservation

<br>
                
#### Database services

* Frequent vs. infrequent access
	* transactional DBs (frequent access): SQL, PostGreSQL, CosmosDB
	* infrequent access: Data Warehouse, Data Lake

* Cosmos DB
	* fully managed
	* Is a NoSQL db
	* extremely fast storage: sub 5-ms
	* suitable for small pieces of data that need to be fast
	* Designed for mobile video games, social networks, and things requiring thousands of global replications
	* NOT suitable for big enterprise applications e.g. customer CRM
	* Supports many open-source APIs and protocols e.g. Cassandra, MongoDB, Tables, Gremlin API

* Azure SQL database
    * is PaaS (but also aka DBaaS)
	* does require user administration efforts
	* Runs SQL Server engine underneath
	* Relational DB
    * Geo-replication
    	* Easy to **replicate** into different regions and scale    
        * maximum of four secondary replicas can be created
        * secondary replicas can be promoted to primary
	* Easy to migrate from on-prem SQL Server
    * cannot be applied to an existing VM

* Azure database for MySQL  
	* Used by WordPress
	* If using on your website, migrating to a managed version is easy

* Azure database for PostgreSQL
	* For bigger DBs that require clusters and more complex server setups
	* Migration easy

* SQL Managed instance
	* Most compatible with existing SQL Server
	* Minimal code changes
	* Fully managed by Azure
	* Always up-to-date	

* Azure Redis Cache
    * data or content cache, a session store, a message broker, and more. 
    * can be deployed as a standalone or it can be deployed along with other Azure database services, such as Azure SQL or Cosmos DB.
     
 
<br>
    
#### ETL Service.

* Data Factory      

<br>
     
#### Azure Marketplace

* Is a service!
* To find pre-build VMs, Web Apps e.g. PowerApps
