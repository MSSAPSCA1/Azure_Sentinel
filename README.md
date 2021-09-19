# Azure_Sentinel
**Bulk turn on analytics rules in Azure Sentinel**
___
## [AZ Sentinel Analytics Rules Template Editor](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/AZ_Sentinel_Analytics_Rules_Editor.py)

Python script to modify properties of Azure Resource Manager (ARM) templates for Azure Sentinel Analytics Rules.

Notes:
1.  The Rule Frequency (queryFrequency) value must be between 5 minutes and 14 days.
2.  The Rule Period (queryPeriod) value must be between 5 minutes and 14 days.
3.  The Rule Frequency must be less than, or equal to, the Rule Period.
4.  When the Rule Period is greater than, or equal to, 2 days, the Rule Frequency must be greater than, or equal to, 1 hour.
___
