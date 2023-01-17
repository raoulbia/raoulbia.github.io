Title: Azure Data Factory
Date: 2022-12-24
Category: Azure Data Factory
Slug: azure_data_factory
Summary: Azure Data Factory

<br>


#### Linked Services

Create a Linked Service to connect ADF to Databricks using Key Vault

* Pre-requisite: an existing Key Vault resource with a secret holding the Databricks PAT
* This requires two linked services
  * Databrick ls > get it from 'Compute' tab
  * within this ls you are asked to specify an AKV linked service > click on 'New'
* AKV linked Service
  * Base URL should be prefilled
  * Authentication Method: *System Assigned Managed Identity*

<br>

#### Parameterizing ADF

Create dynamic folder name for COPY activity (egress)
 
* source ADLSGen2:  
  `@concat('@concat('custom_dataset/shared_team_data/CG_BPT/BPT_CLIENT_EXCELS/', formatdatetime(utcnow(),'yyyy-MM-dd'))`
    
* sink NAS Drive:   
  `@concat('Azure/CG/static_output_files/', formatDateTime(utcNow(),'yyyy'), '-' ,formatDateTime(utcNow(),'MM'), '-', formatDateTime(utcNow(),'dd'))`
