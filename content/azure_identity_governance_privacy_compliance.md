Title: Azure Identity, Governance, Privacy and Compliance Features 
Date: 2018-03-24
Category: Cloud
Slug: azure_identity_governance_privacy_compliance
Summary: Azure Identity, Governance, Privacy and Compliance Features 
Status: draft

<br>

## Identity Services

Who people are and what access they have.

Identity IS A digital representation of a person, applications or device (e.g. printer).

Authenticated does not mean authorised for everything.

* MF Authentication
    * is an Azure AD feature
	* Authentication items must be distinct i.e. sth you know (password), sth you have (SMS code) or sth you are (fingerprint)
	* deployment options
		* Conditional Access Policies (only approved devices)
		* MFA Settings
	* NO need to sync on-prem identity to the cloud 
	* NO need to deploy federation solution

* Privileged Identity Management: 
    * MFA for admins but not regular users.


* Azure Active Directory
    * Azure Tenant: represents an organisation in Active Directory (AD)
    * **is NOT related to authorisation based on roles**
	* has built-in capability for securing authentication AND authorisation
	* **Identity as a Service** i.e. don’t have to write any code
		* e.g. Comes with feature such as pw reset etc
	* Azure AD is NOT the same as Windows AD (there is some overlap)
		* Traditional AD does not work with internet protocols
	* Authentication open standards: SAML, OpenID, WS Federation
	* AD powers other micrososft services: outlook, skype, onedrive, xbox, office365

* Benefits of Azure AD
	* Security, tested and proven
	* Reduced development time, easier support
	* More features besides basic authentication e.g. MFA, just-in-time elevation of privileges, conditional access
	* Centralised administration, API’s
	* **SSO**
        * Integration with Windows AD allowing for single sign on using **AD Connect**. 
        * SSO is Free for up to 10 Apps
	* Note SSO is how you disable leavers.
	* Integrates with other Azure services e.g. can grant access to storage accounts and SQL DB’s using their windows sign on credentials

	
* Azure AD Conditional Access
	* allow access only from approved devices
	* Can detect unusual activity and require extra authentication from user

<br>

##  Governance Features

Governance is a set of policies and procedures of your company that protect your account and your data.

* Role-based access control
	* What privileges the user gets 
	* Roles = common tasks e.g. accounting, developer
	* Predefined roles: reader, contributor, owner
    *  allow some users to control the virtual machines in each environment but prevent them from modifying networking and other resources in the same resource group or Azure subscription

* Resource locks 
	* prevent accidental deletion

* Tags
	* Metadata associated with the resource
	* Helps with billing and support issues

* Azure Policy
	* Implement standards for your organization across Azure.
    * a set of policies is called *Initiative*
    * provide organizations with the ability to manage the compliance of Azure resources **across multiple subscriptions**.

* Governance 
	* create rules across all of your Azure resources
	* e.g. Creating groups and subscriptions and associate rules that way
	
* Built-in policies:
	* Require SQL Server 12.0
	* Allowed storage accounts (nbr units)
	* Allowed locations
	* Allowed VMs (nbr units, types)
	* Apply tag and its default value
	* Not allowed resource types

* Azure Blueprints
	* subscription templates with **Roles and Policies** already defined

* Cloud Adoption Framework (CAF) for Azure
	* **For migrating to the cloud**
	* Set of docs and tools to help you on your journey from on-prem apps, and self-hosted, into the cloud
	* Best practices for organisations who are looking to make this move


<br>

## Privacy and Compliance Resources

* **Resource groups** provide organizations with the ability to **manage the compliance of Azure resources** across multiple subscriptions.
* Security Centre vs. Trust Center
    * Security Centre: check compliance for a specified environment
    * Trust Centre
        * is about Microsoft's compliance
    	* Has info about the standards MS complies with: GDPR. ISO,…

* The trusted Cloud initiative
	* Security: encryption, security tools,…
	* Privacy: you own your data, MS will not mine the data, you control where data is located … 
	* Compliance: international standards, MS has compliance certificates, follows regional standards
	* Resiliency: always available, backups, high availability, disaster recovery
	* Intellectual Property protection: Azure offers protection against frivolous infringement claims

* Online Service Terms (OST) and Data Protection Addendum (DPA)
	* MS Privacy Terms: personal we collect, why we collect it
	* OST: level of service we promise you …
	* DPA: how they handle data, where they store it, what they do if there is a security incident, how data is retained 

* Compliance documentation
    * assigning policy compliance responsibilities

* Azure Sovereign regions (US government and China)`
	* Isolated, not connected to public cloud
	
* Azure Information Protection
	* document processing and adding labels
