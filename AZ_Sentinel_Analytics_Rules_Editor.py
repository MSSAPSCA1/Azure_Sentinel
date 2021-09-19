import json

# Prompts user for path to AZ Sentinel JSON rule template and checks the validity.
def read_in():
    test = True
    while test == True:
        test = False
        
        path = str(input("Enter the file path of a JSON rule template (CTRL+C to Exit):\n"))

        if path.split(".")[-1] != "json":
            print("\nIncorrect file type. Please try again.")
            test = True
            continue

        try:
            with open(path, "r") as rule_template:
                data = json.load(rule_template)
        except FileNotFoundError:
            print("\nThe file path you entered does not exist. Please try again.")
            test = True
            continue

    # Creates path to new file and modifies the data retrieved from the original file.
    file_name = path.split("\\")[-1]
    new_path = path.replace(file_name, ("NEW_" + file_name))
    return data, new_path

# Statements for future user input and separation by functions
def modify(data, properties):

    val_dict = {"enabled":{"Name":"Rule Status", "Selection":{"1":"Enabled", "2":"Disabled"}, "Value":{"1":True, "2":False}}, "queryFrequency":{"Name":"Rule Frequency", "Selection":{"1":"Enter frequency in Days", "2":"Enter frequency in Hours", "3":"Enter frequency in Minutes"}, "Value":{"1":"P_D", "2":"PT_H", "3":"PT_M"}}, "queryPeriod":{"Name":"Rule Period", "Selection":{"1":"Enter period in Days", "2":"Enter period in Hours", "3":"Enter period in Minutes"}, "Value":{"1":"P_D", "2":"PT_H", "3":"PT_M"}}}

    rule_index = len(data['resources'])
    for name in properties:    
        test = True
        while test == True:
            test = False          
            print("\nSelect an option to modify the " + val_dict[name]["Name"] + ":\n*** Example Input: 1 ***\n")
            
            for i in val_dict[name]["Selection"]:
                print(i + ": " + val_dict[name]["Selection"][i])
            
            user_val = input("\nEnter value here: ").strip(". ")

            try:
                val = val_dict[name]["Value"][user_val]
            except KeyError:
                print("\nYour Input \"" + ", ".join(user_val) + "\" is not valid.\nThe option you selected does not exist.\nPlease try again.\n")
                input("Press Enter to try again or CRTL+C to exit.")
                test = True
                continue

        test = True
        while test == True:
            test = False   
            
            if name == "queryFrequency" or name == "queryPeriod":
                try:
                    time_val = input("\n" + val_dict[name]["Selection"][user_val] + " as a positive integer greater than 0:\n*** Example Input: 30 ***\n\nEnter value here: ").replace("-","")
                    test2 = int(time_val)
                except ValueError:
                    print("\nYour Input \"" + time_val + "\" is not valid.\nThe value you entered is not an integer.\nPlease try again.\n")
                    input("Press Enter to try again or CRTL+C to exit.")
                    test = True
                    continue

                val = val.replace("_", time_val)

                if time_val == "1":
                    time_type = val_dict[name]["Selection"][user_val].split(" ")[-1]
                    time_type = time_type.replace("s", "")
                else:
                    time_type = val_dict[name]["Selection"][user_val].split(" ")[-1]

                print("\nSetting " + val_dict[name]["Name"] + " to " + time_val + " " + time_type + "...")

            else:
                val_type = val_dict[name]["Selection"][user_val]
                print("\nSetting " + val_dict[name]["Name"] + " to " + val_type + "...")

        for index in range(rule_index):
            data['resources'][index]['properties'][name] = val

    return data
    # print(data['resources'][rule_index]['properties']['enabled'])

# Exports modified data into new JSON file.
def write_out(data, new_path):

    with open(new_path, "w") as new_rule_template:
        json.dump(data, new_rule_template, indent = 4)

# Controls script
def main():
    data = read_in()

    user_sel_dict = {"1":"enabled", "2":"queryFrequency", "3":"queryPeriod"}
    properties = set()
    test = True
    while test == True:
        test = False
        
        user_sel = input("\nSelect the properties to be modified by entering each selection separated by a comma:\n*** Example Input: 1,2,3 ***\n\n1. Rule Status (Enabled/Disabled)\n2. Rule Frequency\n3. Rule Period\n\nEnter values here: ").replace(" ", "").split(",")

        try:
            for num in user_sel:
                properties.add(user_sel_dict[num])
        except KeyError:
            print("\nYour Input \"" + ", ".join(user_sel) + "\" is not valid.\nOne or more of the options you selected does not exist.\nPlease try again.\n")
            input("Press Enter to try again or CRTL+C to exit.")
            test = True
            continue

    mod_data = modify(data[0], properties)
    write_out(mod_data, data[1])

    print("Process Completed.")
    input("\nPress Enter to Exit.")

main() # Script source: https://github.com/nathanjalston/Azure_Sentinel_Hackathon_2021