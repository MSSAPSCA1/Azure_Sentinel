# Azure Sentinel Hackathon 2021
**Azure Resource Manager (ARM) Templates for Bulk Activation of Azure Sentinel Analytics Rules.**
___
## [Azure Sentinel Analytics Rules: ARM Template Editor](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/AZ_Sentinel_Analytics_Rules_Editor.py)

Python script to modify properties of Azure Resource Manager (ARM) templates for bulk modification of Azure Sentinel Analytics Rules.

Notes from Azure Sentinel:
1.  The Rule Frequency (queryFrequency) value must be between 5 minutes and 14 days.
2.  The Rule Period (queryPeriod) value must be between 5 minutes and 14 days.
3.  The Rule Frequency must be less than, or equal to, the Rule Period.
4.  When the Rule Period is greater than, or equal to, 2 days, the Rule Frequency must be greater than, or equal to, 1 hour.
___
## [Default Azure Sentinel Analytics Rules Templates](https://github.com/MSSAPSCA1/Azure_Sentinel/tree/main/Default_AZ_Sentinel_Rule_Templates)

Default ARM templates for specific sets of Azure Sentinel Analytics Rules, including:

*  [Vectra Detection and AI Detection](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Vectra_Detect_AZ_Sentinel_Analytics_Rules.json)
