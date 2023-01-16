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

High Level
----------

* in AKV we create a secret 
* in ADB we create a secret scope
  * the secet scope points to the AKV URI abd Resource ID
* in ADB notebook re reference
  * the stoage account name
  * the name of the ADB secret scope
  * the name of the AKV secret     

Detailed
--------

1. Create Key Vault resource
   * go to resource > Secrets
     * under settings > +Generate/Import
     * provide recognisable **key vault secret name** e.g. StorageAccountSecret
     * provide storage key for the Azure Blob storage account
     * NOTE: secret value must be changed every 3 months 
     
2. To use Azure Key Vault in Databricks notebooks, a **Secret scope** must be created in Databricks. The Secret scope can be used in Databricks notebook to retrieve secret values from Azure Key Vault. 
   * go to `<Databricks URL>/#secrets/createScope`
   * create a new scope and name it e.g. KeyVaultScope
   * Manage Principal > All USers
   * DNS name is "Vault URI" in Key Vault **Overview** page
   * Reosurce ID can be found in Key Vault **Properties** page
   
3. Notebook implementation: 

   Storage account key is stored in Azure Key-Vault as a sceret. 
   KeyVaultScope is the name of the scope we have created
      
   ```
   storageAccount="<name of storage account>"
   storageKey = dbutils.secrets.get(scope = "KeyVaultScope", 
                                    key = "<name of secret in KeyVault>")
   mountpoint = "/mnt/KeyVaultBlob"
   storageEndpoint = "wasbs://marketbasket@{}.blob.core.windows.net".format(storageAccount)
   storageConnSting = "fs.azure.account.key.{}.blob.core.windows.net".format(storageAccount)

   try:
      dbutils.fs.mount(
      source = storageEndpoint,
      mount_point = mountpoint,
      extra_configs = {storageConnSting:storageKey})
   except:
      print("Already mounted...."+mountpoint)
   ```


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
