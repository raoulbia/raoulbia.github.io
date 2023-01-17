Title: Azure
Date: 2022-12-24
Category: Azure
Slug: azure
Summary: Azure

<br>

#### Parameterization

* create folder name for COPY activity sink egress: `@concat('Azure/CG/static_output_files/', formatDateTime(utcNow(),'yyyy'), '-' ,formatDateTime(utcNow(),'MM'), '-', formatDateTime(utcNow(),'dd'))`


#### Key Vault and Service Principal

* [Connecting Databricks to Azure Blob storage]({filename}./azure_databricks.md)


#### AZ-900

* [Azure Cloud: Benefits and Categories]({filename}./azure_cloud_concepts.md)
* [Azure Architectural Components]({filename}./azure_architectural_components.md)
* [Azure Services]({filename}./azure_services.md)
* [Azure Solutions]({filename}./azure_solutions.md)
* [Azure Management Tools]({filename}./azure_management_tools.md)
* [Azure General Security Features]({filename}./azure_general_security_features.md)
* [Azure Network Security]({filename}./azure_network_security.md)
* [Azure Identity, Governance, Privacy and Compliance Features]({filename}./azure_identity_governance_privacy_compliance.md)
* [Azure Cost Management and SLA]({filename}./azure_cost_management_and_sla.md)
