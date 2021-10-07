# [Azure Sentinel Hackathon 2021](https://github.com/MSSAPSCA1/Azure_Sentinel)
**Azure Resource Manager (ARM) Templates and ARM Template Editor for Bulk Activation and Modification of Azure Sentinel Analytics Rules.**

The following process enables optimized deployment and modification of Azure Sentinel Analytics Rules. By accelerating the configuration of Analytics Rules, this process enables the Administrator to save time and resources.

___
## How to bulk activate the default Azure Sentinel Analytics Rules

### Operating Instructions:

**Prerequisites:**
  * Active Azure Subscription.
  * Resource group with Azure Sentinel service created.
  
 [Create a free subscription with 200 USD](https://azure.microsoft.com/en-us/free/)
 
**Procedure:**
   
   1. Download a ZIP file of the rules from the repository using the green "Code" button. Extract the file.
   2. Login to Microsoft Azure.
   3. Search for "Azure Sentinel" using the search bar at the top of the window.
   4. Select "Azure Sentinel" under Services.
   5. Select the appropriate Resource group for your organization.
   6. Select "Analytics" under the Configuration section.
   7. Locate and select the "Import" button near the top of the window.
   8. Select the preferred JSON file from the previously downloaded and extracted file.
   9. The Deployment process will start.

___
## How to edit the Azure Sentinel Analytics Rules to fit your organization's requirements

## [ARM Template Editor for Analytics Rules](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/AZ_Sentinel_Analytics_Rules_Editor.py)

### Description:
Python script to modify properties of ARM templates for bulk modification of Azure Sentinel Analytics Rules. Currently capable of modifying Rule Status (Enabled/Disabled), Rule Frequency, and Rule Period for any number of Azure Sentinel Analytics Rules contained within any number of ARM template files.

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
2.  Enter the path to the ARM template file(s) (i.e. C:\fakepath\AZ_Sentinel\Vectra_Detect_AZ_Sentinel_Analytics_Rules.json), or drag-and-drop each file, one at a time. Separate each file using a comma (,).
3.  Select options by entering the number associated with the option.
4.  Enter requested data based on constraints specified in the program and in the Notes from Azure Sentinel.
5.  Once the process is completed, a new file or new files will be created at the same address as the original file(s) with the user-specified prefix appended as the prefix of the filename(s). You will now have two files for each ARM template, the orignal and the new file.

 
### [Watch this video for a detailed explanation](https://youtu.be/f0YaSqNwJCM)

___
## [ARM Templates for Default Analytics Rules](https://github.com/MSSAPSCA1/Azure_Sentinel/tree/main/Default_AZ_Sentinel_Rule_Templates)

Default ARM templates for most of Azure Sentinel's built-in Scheduled Analytics Rules.
* Rule Frequency = Default
* Rule Period = Default

### Analytics Rules:
* [0-A](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/(1)%200-A_Azure_Sentinel_Scheduled_Analytics_Rules.json)
* [A-F](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/(2)%20A-F_Azure_Sentinel_Scheduled_Analytics_Rules.json)
* [F-N](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/(3)%20F-N_Azure_Sentinel_Scheduled_Analytics_Rules.json)
* [N-S](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/(4)%20N-S_Azure_Sentinel_Scheduled_Analytics_Rules.json)
* [S-Z](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/(5)%20S-Z_Azure_Sentinel_Scheduled_Analytics_Rules.json)
*  [(Preview) Anomalous Account Creation](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/(Preview)_Anomalous_Account_Creation_AZ_Sentinel_Analytics_Rule.json)
*  [(Preview) Anomalous Code Execution](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/(Preview)_Anomalous_Code_Execution_AZ_Sentinel_Analytics_Rule.json)
*  [(Preview) TI map...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/(Preview)_TI_map_AZ_Sentinel_Analytics_Rules.json)
*  [Account added and removed from privileged groups](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Account_added_and_removed_from_privileged_groups__AZ_Sentinel_Analytics_Rule.json)
*  [Active Directory](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Active_Directory_AZ_Sentinel_Analytics_Rules.json)
*  [Anomalous login followed by Teams action](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Anomalous_AZ_Sentinel_Analytics_Rules.json)
*  [Anomalous sign-in location by user account and authenticating application](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Anomalous_AZ_Sentinel_Analytics_Rules.json)
*  [Anomalous User Agent connection attempt](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Anomalous_AZ_Sentinel_Analytics_Rules.json)
*  [AppServices AV Scan](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/AppServices_AV_Scan_AZ_Sentinel_Analytics_Rules.json)
*  [Attempt to bypass conditional access rule in Azure AD](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Attempt..._AZ_Sentinel_Analytics_Rules.json)
*  [Attempts to sign in to disabled accounts](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Attempt..._AZ_Sentinel_Analytics_Rules.json)
*  [Audit policy manipulation using auditpol utility](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Audit_policy_manipulation_using_auditpol_utility_AZ_Sentinel_Analytics_Rule.json)
*  [Azure Active Directory PowerShell accessing non-AAD resource](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Azure_Active_Directory_PowerShell_accessing_non-AAD_resource_AZ_Sentinel_Analytics_Rule.json)
*  [Azure DevOps](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Azure_DevOps_AZ_Sentinel_Analytics_Rules.json)
*  [Azure Key Vault access TimeSeries anomaly](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Azure_Key_Vault_access_TimeSeries_anomaly_AZ_Sentinel_Analytics_Rule.json)
*  [Base64 encoded Windows process command-lines](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Base64_encoded_Windows_process_command-lines_AZ_Sentinel_Analytics_Rule.json)
*  [Brute force attack against...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Brute_force_attack_against..._AZ_Sentinel_Analytics_Rules.json)
*  [Changes made to AWS CloudTrail logs](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Changes..._AZ_Sentinel_Analytics_Rules.json)
*  [Changes to Amazon VPC settings](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Changes..._AZ_Sentinel_Analytics_Rules.json)
*  [Changes to AWS Elastic Load Balancer security groups](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Changes..._AZ_Sentinel_Analytics_Rules.json)
*  [Changes to AWS Security Group ingress and egress settings](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Changes..._AZ_Sentinel_Analytics_Rules.json)
*  [Changes to internet facing AWS RDS Database instances](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Changes..._AZ_Sentinel_Analytics_Rules.json)
*  [Cisco...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Cisco..._AZ_Sentinel_Analytics_Rules.json)
*  [Correlate Unfamiliar sign-in properties and atypical travel alerts](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Correlate_Unfamiliar_sign-in_properties_and_atypical_travel_alerts_AZ_Sentinel_Analytics_Rule.json)
*  [Create incidents based on Azure Active Directory Identity Protection alerts](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Create_incidents_based_on..._AZ_Sentinel_Analytics_Rules.json)
*  [Create incidents based on Azure Defender alerts](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Create_incidents_based_on..._AZ_Sentinel_Analytics_Rules.json)
*  [Create incidents based on Azure Defender for IOT alerts](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Create_incidents_based_on..._AZ_Sentinel_Analytics_Rules.json)
*  [Create incidents based on Microsoft Cloud App Security alerts](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Create_incidents_based_on..._AZ_Sentinel_Analytics_Rules.json)
*  [Create incidents based on Microsoft Defender for Endpoint alerts](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Create_incidents_based_on..._AZ_Sentinel_Analytics_Rules.json)
*  [Create incidents based on Microsoft Defender for Identity alerts](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Create_incidents_based_on..._AZ_Sentinel_Analytics_Rules.json)
*  [Create incidents based on Microsoft Defender for Office 365 alerts](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Create_incidents_based_on..._AZ_Sentinel_Analytics_Rules.json)
*  [Creation of expensive computes in Azure](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Creation_of_expensive_computes_in_Azure_AZ_Sentinel_Analytics_Rule.json)
*  [Credential added after admin consented to Application](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Credential_added_after_admin_consented_to_Application_AZ_Sentinel_Analytics_Rule.json)
*  [DEV-0322 Serv-U related IOCs-July 2021](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/DEV-0322_Serv-U_related_IOCs-July%202021_AZ_Sentinel_Analytics_Rule.json)
*  [DNS events related to...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/DNS_events_related_to_AZ_Sentinel_Analytics_Rules.json)
*  [Distributed Password cracking attempts in AzureAD](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Distributed_Password_cracking_attempts_in_AzureAD_AZ_Sentinel_Analytics_Rule.json)
*  [Email access via active sync](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Email_access_via_active_sync_AZ_Sentinel_Analytics_Rule.json)
*  [Excessive NXDOMAIN DNS Queries (Normalized DNS)](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Excessive..._AZ_Sentinel_Analytics_Rules.json)
*  [Excessive Windows logon failures](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Excessive..._AZ_Sentinel_Analytics_Rules.json)
*  [Exchange...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Exchange..._AZ_Sentinel_Analytics_Rules.json)
*  [Explicit MFA Deny](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Explicit%20_MFA_Deny_AZ_Sentinel_Analytics_Rule.json)
*  [External Upstream Source Added to Azure DevOps Feed](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/External..._AZ_Sentinel_Analytics_Rules.json)
*  [External user added and removed in short timeframe](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/External..._AZ_Sentinel_Analytics_Rules.json)
*  [Failed...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Failed..._AZ_Sentinel_Analytics_Rules.json)
*  [First access credential added to Application or Service Principal where no credential was present](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/First_access_credential_added_to_Application_or..._AZ_Sentinel_Analytics_Rule.json)
*  [GitHub Signin Burst from Multiple Locations](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/GitHub_Signin_Burst_from_Multiple_Locations_AZ_Sentinel_Analytics_Rule.json)
*  [Group created then added to built in domain local or global group](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Group_created_then_added_to_built_in_domain_local_or_global_group_AZ_Sentinel_Analytics_Rule.json)
*  [HAFNIUM...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/HAFNIUM..._AZ_Sentinel_Analytics_Rules.json)
*  [High count of...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/High_count_of..._AZ_Sentinel_Analytics_Rules.json)
*  [IP with multiple failed Azure AD logins successfully logs in to Palo Alto VPN](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/IP_with_multiple_failed_Azure_AD_logins_successfully_logs_in_to_Palo_Alto_VPN_AZ_Sentinel_Analytics_Rule.json)
*  [Known Barium...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Known_Barium..._AZ_Sentinel_Analytics_Rules.json)
*  [Known CERIUM domains and hashes](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Known_CERIUM_domains_and_hashes_AZ_Sentinel_Analytics_Rule.json)
*  [Known GALLIUM domains and hashes](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Known_GALLIUM_domains_and_hashes_AZ_Sentinel_Analytics_Rule.json)
*  [Known IRIDIUM IP](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Known_IRIDIUM_IP_AZ_Sentinel_Analytics_Rule.json)
*  [Known Manganese IP and UserAgent activity](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Known_Manganese_IP_and_UserAgent_activity_AZ_Sentinel_Analytics_Rule.json)
*  [Known STRONTIUM group domains - July 2019](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Known_STRONTIUM_group_domains-July_2019_AZ_Sentinel_Analytics_Rule.json)
*  [Known ZINC...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Known_ZINC..._AZ_Sentinel_Analytics_Rules.json)
*  [Linked Malicious Storage Artifacts](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Linked_Malicious_Storage_Artifacts_AZ_Sentinel_Analytics_Rule.json)
*  [Login to AWS Management Console without MFA](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Login_to_AWS_Management_Console_without_MFA_AZ_Sentinel_Analytics_Rule.json)
*  [Mail...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Mail..._AZ_Sentinel_Analytics_Rules.json)
*  [Malformed user agent](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Malformed_user_agent_AZ_Sentinel_Analytics_Rule.json)
*  [Malicious Inbox Rule](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Malicious_Inbox_Rule_AZ_Sentinel_Analytics_Rule.json)
*  [Malicious web application requests linked with Microsoft Defender for Endpoint (formerly Microsoft Defender ATP) alerts](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Malicious_web_application_requests_linked_with_Microsoft_Defender_for_Endpoint_(formerly_Microsoft_Defender_ATP)_alerts_AZ_Sentinel_Analytics_Rule.json)
*  [Malware in the recycle bin](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Malware_in_the_recycle_bin_AZ_Sentinel_Analytics_Rule.json)
*  [Mass secret retrieval from Azure Key Vault](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Mass_secret_retrieval_from_Azure_Key_Vault_AZ_Sentinel_Analytics_Rule.json)
*  [MFA disabled for a user](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/MFA_disabled_for_a_user_AZ_Sentinel_Analytics_Rule.json)
*  [Microsoft COVID-19 file hash indicator matches](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Microsoft_COVID-19_file_hash_indicator_matches_AZ_Sentinel_Analytics_Rule.json)
*  [Modified domain federation trust settings](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Modified_domain_federation_trust_settings_AZ_Sentinel_Analytics_Rule.json)
*  [Monitor AWS Credential abuse or hijacking](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Monitor_AWS_Credential_abuse_or_hijacking_AZ_Sentinel_Analytics_Rule.json)
*  [Multiple Password Reset by user](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Multiple_Password_Reset_by_user_AZ_Sentinel_Analytics_Rule.json)
*  [Multiple RDP connections from Single System](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Multiple_RDP_connections_from_Single%20System_AZ_Sentinel_Analytics_Rule.json)
*  [Multiple Teams deleted by a single user](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Multiple_Teams_deleted_by_a_single_user_AZ_Sentinel_Analytics_Rule.json)
*  [Multiple users email forwarded to same destination](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Multiple_users_email_forwarded_to_same_destination_AZ_Sentinel_Analytics_Rule.json)
*  [Network endpoint to host executable correlation](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Network_endpoint_to_host_executable_correlation_AZ_Sentinel_Analytics_Rule.json)
*  [New access credential added to Application or Service Principa](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/New_access_credential_added_to_Application_or_Service_Principa_AZ_Sentinel_Analytics_Rule.json)
*  [New Agent Added to Pool by New User or of a New OS Type](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/New_Agent_Added_to_Pool_by_New_User_or_of_a_New_OS_Type_AZ_Sentinel_Analytics_Rule.json)
*  [New CloudShell User](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/New_CloudShell_User_AZ_Sentinel_Analytics_Rule.json)
*  [New executable via Office FileUploaded Operation](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/New_executable_via_Office_FileUploaded_Operation_AZ_Sentinel_Analytics_Rule.json)
*  [New internet-exposed SSH endpoints](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/New_internet-exposed_SSH_endpoints_AZ_Sentinel_Analytics_Rule.json)
*  [New PA, PCA, or PCAS added to Azure DevOps](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/New_PA%2C_PCA%2C_or_PCAS_added_to_Azure_DevOps_AZ_Sentinel_Analytics_Rule.json)
*  [New user created and added to the built-in administrators group](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/New_user_created_and_added_to_the_built-in_administrators_group_AZ_Sentinel_Analytics_Rule.json)
*  [New UserAgent observed in last 24 hours](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/New_UserAgent_observed%20in_last_24_hours_AZ_Sentinel_Analytics_Rules.json)
*  [NOBELIUM...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/NOBELIUM..._AZ_Sentinel_Analytics_Rules.json)
*  [Non Domain Controller Active Directory Replication](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Non_Domain_Controller_Active_Directory_Replication_AZ_Sentinel_Analytics_Rules.json)
*  [Office policy tampering](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Office_policy_tampering_AZ_Sentinel_Analytics_Rule.json)
*  [Palo Alto...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Palo_Alto..._AZ_Sentinel_Analytics_Rules.json)
*  [Password spray attack against Azure AD application](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Password_spray_attack_against_Azure_AD_application_AZ_Sentinel_Analytics_Rule.json)
*  [Possible contact with a domain generated by a DGA](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Possible_contact_with_a_domain_generated_by_a_DGA_AZ_Sentinel_Analytics_Rule.json)
*  [Possible STRONTIUM attempted credential harvesting - Sept 2020andOct2020](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Possible_STRONTIUM_attempted_credential_harvesting-Sept_2020andOct2020_AZ_Sentinel_Analytics_Rules.json)
*  [Potential Build Process Compromise...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Potential_Build_Process_Compromise..._AZ_Sentinel_Analytics_Rule.json)
*  [Potential DGA detected](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Potential_DGA_detected_AZ_Sentinel_Analytics_Rule.json)
*  [Potential Kerberoasting](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Potential_Kerberoasting_AZ_Sentinel_Analytics_Rule.json)
*  [Powershell Empire cmdlets seen in command line](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Powershell_Empire_cmdlets_seen_in_command_line_AZ_Sentinel_Analytics_Rule.json)
*  [Probable AdFind Recon Tool Usage](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Probable_AdFind_Recon_Tool_Usage_AZ_Sentinel_Analytics_Rule.json)
*  [Process executed from binary hidden in Base64 encoded file](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Process_executed_from_binary_hidden_in_Base64_encoded_file_AZ_Sentinel_Analytics_Rule.json)
*  [Process execution frequency anomaly](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Process_execution_frequency_anomaly_AZ_Sentinel_Analytics_Rule.json)
*  [Rare...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Rare..._AZ_Sentinel_Analytics_Rules.json)
*  [RDP Nesting](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/RDP_Nesting_AZ_Sentinel_Analytics_Rule.json)
*  [Request for single resource on domain](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Request_for_single_resource_on_domain_AZ_Sentinel_Analytics_Rule.json)
*  [Security Event log cleared](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Security_Event_log_cleared_AZ_Sentinel_Analytics_Rule.json)
*  [Security Service Registry ACL Modification](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Security_Service_Registry_ACL_Modification_AZ_Sentinel_Analytics_Rule.json)
*  [SecurityEvent - Multiple authentication failures followed by a success](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/SecurityEvent-Multiple_authentication_failures_followed_by_a_success_AZ_Sentinel_Analytics_Rules.json)
*  [Sensitive Azure Key Vault operations](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Sensitive_Azure_Key_Vault_operations_AZ_Sentinel_Analytics_Rule.json)
*  [SharePointFileOperation via...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/SharePointFileOperation_via..._AZ_Sentinel_Analytics_Rules.json)
*  [Sign-ins from IPs that attempt sign-ins to disabled accounts](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Sign-ins_from_IPs_that_attempt_sign-ins%20to_disabled_accounts_AZ_Sentinel_Analytics_Rule.json)
*  [Solorigate...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Solorigate..._AZ_Sentinel_Analytics_Rules.json)
*  [Squid proxy events...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Squid_proxy_events..._AZ_Sentinel_Analytics_Rules.json)
*  [Successful logon from IP and failure from a different IP](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Successful_logon_from_IP_and_failure_from_a_different_IP_AZ_Sentinel_Analytics_Rule.json)
*  [SUNBURST...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/SUNBURST..._AZ_Sentinel_Analytics_Rules.json)
*  [SUNSPOT...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/SUNSPOT..._AZ_Sentinel_Analytics_Rules.json)
*  [SUPERNOVA webshell](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/SUPERNOVA_webshell_AZ_Sentinel_Analytics_Rule.json)
*  [Suspicious...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Suspicious..._AZ_Sentinel_Analytics_Rules.json)
*  [TEARDROP memory-only dropper](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/TEARDROP_memory-only_dropper_AZ_Sentinel_Analytics_Rule.json)
*  [THALLIUM domains included in DCU takedown](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/THALLIUM_domains_included_in_DCU_takedown_AZ_Sentinel_Analytics_Rule.json)
*  [Time series anomaly...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Time_series_anomaly..._AZ_Sentinel_Analytics_Rules.json)
*  [User...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/User..._AZ_Sentinel_Analytics_Rules.json)
*  [Vectra AI Detect...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Vectra_AI_Detect..._AZ_Sentinel_Analytics_Rules.json)
*  [Vectra Detection...](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Vectra_Detection..._AZ_Sentinel_Analytics_Rules.json)
*  [Wazuh - Large Number of Web errors from an IP](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Default_AZ_Sentinel_Rule_Templates/Wazuh-Large_Number_of_Web_errors_from_an_IP_AZ_Sentinel_Analytics_Rule.json)
___
## [ARM Templates for Quick Response Analytics Rules](https://github.com/MSSAPSCA1/Azure_Sentinel/tree/main/Quick_Response_AZ_Sentinel_Rule_Templates)

ARM templates for most of Azure Sentinel's built-in Scheduled Analytics Rules, modified for quick response. 
* Rule Frequency = 10 minutes
* Rule Period = 30 minutes

### Analytics Rules:
* [0-A](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Quick_Response_AZ_Sentinel_Rule_Templates/QR_0-A_Azure_Sentinel_Scheduled_Analytics_Rules.json)
* [A-F](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Quick_Response_AZ_Sentinel_Rule_Templates/QR_A-F_Azure_Sentinel_Scheduled_Analytics_Rules.json)
* [F-N](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Quick_Response_AZ_Sentinel_Rule_Templates/QR_F-N_Azure_Sentinel_Scheduled_Analytics_Rules.json)
* [N-S](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Quick_Response_AZ_Sentinel_Rule_Templates/QR_N-S_Azure_Sentinel_Scheduled_Analytics_Rules.json)
* [S-Z](https://github.com/MSSAPSCA1/Azure_Sentinel/blob/main/Quick_Response_AZ_Sentinel_Rule_Templates/QR_S-Z_Azure_Sentinel_Scheduled_Analytics_Rules.json)
___

Disclaimer: The Analytics rules above do not include all the available rules in Azre Sentinel. They do not include any rules that monitor activity from a third party Data Connectors or any rules that require a pre-created data tables. The remaining rules will need to be created and configured based on the Organization's specification. 
