# [Azure Sentinel Hackathon 2021](https://github.com/MSSAPSCA1/Azure_Sentinel)
**Azure Resource Manager (ARM) Templates for Bulk Activation of Azure Sentinel Analytics Rules.**
___
## [ARM Templates for Default Analytics Rules](https://github.com/MSSAPSCA1/Azure_Sentinel/tree/main/Default_AZ_Sentinel_Rule_Templates)

ARM templates for specific sets of default Azure Sentinel Analytics Rules, including:

*  [Vectra Detection and AI Detection](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Vectra_Detect_AZ_Sentinel_Analytics_Rules.json)
___
## [ARM Templates for Quick Response Analytics Rules]()

Modified ARM templates for specific sets of high frequency Azure Sentinel Analytics Rules, including:

* [Placeholder]()
___
## [ARM Template Editor for Analytics Rules](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/AZ_Sentinel_Analytics_Rules_Editor.py)

Python script to modify properties of Azure Resource Manager (ARM) templates for bulk modification of Azure Sentinel Analytics Rules. Currently capable of modifying Rule Status (Enabled/Disabled), Rule Frequency, and Rule Period for any number of Azure Sentinel Analytics Rules contained within a single ARM template.

### Notes from Azure Sentinel:
* The Rule Frequency (queryFrequency) value must be between 5 minutes and 14 days.
* The Rule Period (queryPeriod) value must be between 5 minutes and 14 days.
* The Rule Frequency must be less than, or equal to, the Rule Period.
* When the Rule Period is greater than, or equal to, 2 days, the Rule Frequency must be greater than, or equal to, 1 hour.

### Operating Instructions:

**Prerequisites:**
* Python 3 Interpreter. (see Microsoft Docs/ Microsoft Learn for [validation](https://docs.microsoft.com/en-us/learn/modules/python-install-vscode/2-python-programming-language?pivots=windows) or [install](https://docs.microsoft.com/en-us/learn/modules/python-install-vscode/3-exercise-install-python3?pivots=windows) instructions)
* Path to ARM template/ ARM template file address in directory.

**Procedure:**
1.  Open the AZ_Sentinel_Analytics_Rules_Editor.py using a Python 3 Interpreter.
2.  Enter the path to the ARM template file. (i.e. C:\fakepath\AZ_Sentinel\Vectra_Detect_AZ_Sentinel_Analytics_Rules.json)
3.  Select options by entering the number associated with the option.
4.  Enter requested data based on constraints specified in the program and in the Notes from Azure Sentinel.
5.  Once the process is completed, a new file will be created at the same address of the original file with the word "NEW" appended as the prefix of the filename. You will now have two files, the orignal and the new file.
___
