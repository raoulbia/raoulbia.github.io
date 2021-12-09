Title: Azure Solutions
Date: 2018-03-27
Category: Cloud
Slug: azure_solutions
Summary: Core Azure Solutions
Status: draft

<br>


## IoT

* is SaaS
* Azure IoT Hub 
	* a managed service
	* acts as a message center for bi-directional communication between your IoT application and the devices it manages. 

* Azure IoT Central 
	* a dashboard that allows you to connect, monitor, and manage your IoT devices 

* Azure Sphere 
	* both a chip AND and OS
	* security protocol for IoT devices

* Azure Time Series Insights
    * exploration and telemetry
        * Note: telemetry is the in situ collection of measurements or other data at remote points and their automatic transmission to receiving equipment 

<br>

#### Big Data and Analytics Solutions

* Azure Synapse Analytics
    * formerly SQL Data Warehouse
    * brings together Enterprise Data Warehouse and Big Data Analytics
    * analytics service for BI and machine learning 
    * automatic scaling and high availability
    * Azure SQL Data Warehouse is a cloud-based service that leverages massively parallel processing (MPP) to quickly run complex queries across petabytes of data in a relational database 
    * either serverless or provisioned

* HD Insight
	* Hadoop family open source analytics service for entreprises
	* Umbrella for all Apache big data solutions
	* fully managed Hadoop services
	* interact with them in a SaaS or PaaS way
	* Hadoop Apache Spark, Hive, Kafka, Storm



* Azure Databricks
	* open-source data analytics platform

<br>
    
#### AI Solutions

* Azure Machine Learning
    * build, test, and deploy predictive analytics solutions
* Cognitive Services
    * recommender system, ...
* Azure Bot Service

<br>

#### Serverless computing

* Azure Functions  (see video 31 @ 1:40 for DEMO)
	* Small pieces of code hosted in Azure that run after some trigger e.g. timer, data change, file being stored
    * valid azure function triggers
        * Queue trigger
        * Blob trigger
	* Called serverless because no instance involved
		* you don’t define nbr of CPUs, size of RAM, storage
		* you don’t chose a hosting plan like you do in a web app
	* Consumption-based billing

	* see “Functions Editor” 
	* Search “Function” in marketplace

* Logic Apps 
	* Is a **workflow service**
	* A logic app can call an Azure Function we created!
	* e.g. *when a new file is created in dropbox, copy it to one drive* or *get daily reminders emailed to you* or
	*after executing function, store file on Azure Blob file storage* …
	* Has lots of “external connectors”
 	* Consumption-based billing
	* Search “logic” in marketplace
	* see video 32 @ 0:50 for DEMO

* Event Grid
	* Messaging communication with the outside world 
	* Configurable but not programmable
        
<br>

     
#### DevOps Solutions

* Azure DevOps
	* Tie in development functions (scripts, automation) into your company’s operations (IT infrastructure) e.g. CI/CD 
	* See DevOps pipelines, Agile development processes
	 
* Github
	* See Github Actions: 
	* allows to push code from Github into Azure automatically when source code changes (CI) 
	* check for errors (similar to pre-commit)
	
* Azure DevTest Labs: ??

<br>

#### Entreprise MEssaging Solutions

* Service Bus
