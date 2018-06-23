from os.path import abspath
from os import listdir
import json
import copy

def print_output(index):

    # Initialize the data list which contains the dict
    data = []

    # when url is - https://myapp/data/user
    if index==0:
        for values in userData.values():
            # print(values)
            v2 = copy.copy(values)
            data.append(v2)

    # when url is - https://myapp/data/user?top=true
    elif index==1:
        for user in top_user:
            v2 = userData[user[0]]
            data.append(v2)

    # when url is - https://myapp/data/user?sort=asc
    elif index==2:
        sorted_by_activityNum = sorted(userData.items(), key=lambda x: x["activityNum"])
        for values in sorted_by_activityNum.values():
            v2 = copy.copy(values)
            data.append(v2)

    # when url is - https://myapp/data/user?sort=desc
    elif index==3:
        sorted_by_activityNum = sorted(userData.items(), key=lambda x: x["activityNum"])
        for values in sorted_by_activityNum.values():
            v2 = copy.copy(values)
            data.insert(0, v2)

    # when url is - https://myapp/data/resource
    elif index==4:
        for values in resourceData.values():
            v2 = copy.copy(values)
            data.append(v2)

    # when url is - https://myapp/data/resource?top=true
    elif index==5:
        for resource in top_resource:
            v2 = resourceData[resource[0]]
            data.append(v2)
            
    # when url is - https://myapp/data/resource?sort=asc
    elif index==6:
        sorted_by_activityNum = sorted(resourceData.items(), key=lambda x: x["activityNum"])
        for values in sorted_by_activityNum.values():
            v2 = copy.copy(values)
            data.append(v2)

    # when url is - https://myapp/data/resource?sort=desc
    else:
        sorted_by_activityNum = sorted(resourceData.items(), key=lambda x: x["activityNum"])
        for values in sorted_by_activityNum.values():
            v2 = copy.copy(values)
            data.insert(0, v2)

    # copying the data into new dict
    newdict = {"data" : data}

    # converting the dict into json format
    json_string = json.dumps(newdict, indent=4)
    return json_string

    
def update_user_resource_data(line, flag, userData, resourceData, top_user, top_resource):

    '''
    user_id - contains the current user id
    resource_id - contains the current resource id
    data_consumed - contains the amount of data consumed
    '''
    
    user_id = int(line[4])
    resource_id = int(line[5])
    data_consumed = int(line[-2])
    new_activity_num = 1

    # flag = 1 means the user is new & it is not in the list
    
    if flag==1:
        previous_activity_num = userData[str(user_id)]["activityNum"]
        new_activity_num += previous_activity_num
        
        previous_data_consumed = userData[str(user_id)]["dataConsumed"]
        data_consumed += previous_data_consumed
        
    userData[str(user_id)] = {"userId": user_id, "activityNum": new_activity_num, "dataConsumed": data_consumed}
    resourceData[str(resource_id)] = {"resourceId": resource_id, "activityNum": new_activity_num, "dataConsumed": data_consumed}


    # algorithm which is used to maintain the top user and top resource
    if top_user[0][1] < new_activity_num:
        top_user = [(user_id, new_activity_num)]
    elif top_user[0][1] == new_activity_num:
        top_user.append((user_id, new_activity_num))

    if top_resource[0][1] < new_activity_num:
        top_resource = [(resource_id, new_activity_num)]
    elif top_resource[0][1] == new_activity_num:
        top_resource.append((resource_id, new_activity_num))

def input_output():

    # print(userData)
    # print(resourceData)

    # allowed urls
    allowed_options = ["user", "user?top=true", "user?sort=asc", "user?sort=desc", "resource", "resource?top=true", "resource?sort=asc", "resource?sort=desc"]

    url = "https://myapp/data/"

    # path of the file which contains the input
    inputFile = "sample_input"

    # open the file which contain the inputs
    fileName = open(inputFile, "r")
    
    for line in fileName:
        
        # print(line[19:-1])
        
        if line[19:-1] in allowed_options:
            index = allowed_options.index(line[19:-1])
            # print(index)
            ans = print_output(index)
            print(ans)
            
        else:
            # to handle wrong urls
            error_dict = {"error" : "Incomplete url"}
            json_string = json.dumps(error_dict, indent=4)
            print(json_string)

            
def mine_information(userData, resourceData, resourceId, userId, top_user, top_resource):

    # Server File Path
    serverFilePath = abspath("server")

    # serverFilesList - Stores the name of all the server files in form of list
    serverFilesList = listdir(serverFilePath)
    # print(serverFilesList)

    # Traverse through all server files
    for files in serverFilesList:
        
        # This will determine the path of all the files
        logFilePath = serverFilePath + "\\" + files

        # print(logFilePath)

        # Opens the file which contains the Logging Details 
        logFile = open(logFilePath, "r")

        # Traverse through all the line in the file and update the user and resource data
        for line in logFile:
            line = line.split()
            if line == "Starting":
                continue
            elif len(line) > 5:
                if line[4] not in userId and line[5]:
                    userId.append(line[4]) 
                    resourceId.append(line[5])
                    update_user_resource_data(line, 0, userData, resourceData, top_user, top_resource)
                else:
                    update_user_resource_data(line, 1, userData, resourceData, top_user, top_resource)

    # Print the JSON formatted output
    input_output()

# Error Handling
try:
    '''
    # userData - Contains the info about users
    # resourceData -  Info about resource
    # userId - Determines the user
    # resourceId - Determines the resource
    # top_user - Determines the top users
    # top_resource - Determines the top_resources
    '''
    userData, resourceData, resourceId, userId = {}, {}, [], []
    
    top_user = [(0, 0)]
    top_resource = [(0, 0)]

    # Function which will mine the information from all the servers
    mine_information(userData, resourceData, resourceId, userId, top_user, top_resource)
    
except IOError:
    pass















    
