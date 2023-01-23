Title: Azure
Date: 2022-12-24
Category: Azure
Slug: azure
Summary: Azure

<br>

### Misc.

#### Resouce Groups

* When creating a Databricks resource, Databricks will itself create a separate resource group (RG) with a storage account. This RG cannot be deleted via the porta;. See here for more: https://stackoverflow.com/questions/60694149/unable-to-remove-azure-databricks-managed-resource-group

### Azure ARM

#### Deploy via Powershell

* `New-AzResourceGroup RG01 "South Central US"`
* `New-AzResourceGroupDeployment` adds a deployment to an existing resource group. (https://learn.microsoft.com/en-us/powershell/module/az.resources/new-azresourcegroupdeployment?view=azps-9.3.0)

#### Useful Links

* https://samcogan.com/deploying-resource-groups-with-arm-templates/

<br>

### AZ-900

* [Azure Cloud: Benefits and Categories]({filename}./azure_cloud_concepts.md)
* [Azure Architectural Components]({filename}./azure_architectural_components.md)
* [Azure Services]({filename}./azure_services.md)
* [Azure Solutions]({filename}./azure_solutions.md)
* [Azure Management Tools]({filename}./azure_management_tools.md)
* [Azure General Security Features]({filename}./azure_general_security_features.md)
* [Azure Network Security]({filename}./azure_network_security.md)
* [Azure Identity, Governance, Privacy and Compliance Features]({filename}./azure_identity_governance_privacy_compliance.md)
* [Azure Cost Management and SLA]({filename}./azure_cost_management_and_sla.md)
