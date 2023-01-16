Title: Azure Databricks
Date: 2018-03-28
Category: Cloud
Slug: azure_databricks
Summary: Azure Databricks
Status: draft


<br>
### Connecting Databricks to Azure Storage Account

<br>
  
#### Key Vault Approach

* A Key Vault holds secrets.
* Key Vaults have a pricing plan

1. Create Key Vault resource 
   * go to resource > Secrets
     * under settings > +Generate/Import
     * provide recognisable secret name e.g. StorageAccountSecret
     * provide storage key for the Azure Blob storage account
     * NOTE: secret value must be changed every 3 months 
2. 

<br>
#### Service Principal for DBFS
1. Azure Active Directory > App Registration
   * give recognisable name e.g. ADLSApp
   * leave defaults
   * Note: this IS the service principal
2. click on the newly registered app
   * get Application ID (1)
   * get Directory (Tenant) ID (2)
   * click on Certificates and Secrets
     * create new secret
     * give it a name e.g. ADLSAppSecret
     * copy secret value (3)
3. go to storage account > Access Control (IAM)
   * add role assignment
     * select "Storage Blob Data Contributor"
     * select Service Principal created in step 1
4. (1), (2), and (3) can be used hardcoded in Databricks notebook
