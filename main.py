# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os, glob, json, csv
import pandas as pd
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    directory = "C:\\Users\\Arzhang\\PycharmProjects\\redditDataProcessing\malware\\"
    list_of_data = []
    dict1 = {}
    data_dict = {
        "Title": [],
        "Post ID": [],
        "Username": [],
        "Thread ID": [],
        "Post Content": [],
        "Date": []
    }
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        #new_name = str(f) + ".json"
        #os.rename(f, new_name)
        with open(f, 'r') as file:
            temp_data = json.load(file)
            list_of_data.append(temp_data)
        #list_of_data.append(temp_data)
    total_number_comments = 0



    data_dict = {
        "Title": [],
        "Post ID": [],
        "Username": [],
        "URL": [],
        "Post Content": [],
        "Date": []
    }
    for i in list_of_data:

        op_data = i['op']
        post_data = i['posts']
        total_number_comments = op_data['commsNum'] + total_number_comments



        data_dict['Post Content'].append(str(op_data['selftext']))
        data_dict['Date'].append(str(op_data["timeStamp"]))
        data_dict['Username'].append(str(op_data["author_name"]))
        data_dict['Post ID'].append(str(op_data["id"]))
        data_dict['Title'].append(str(op_data["title"]))
        data_dict['URL'].append(str(op_data["url"]))


        for j in post_data:

            temp_post_data = post_data[str(j)]


            post_id = str(temp_post_data["link_id"])

            post_id = post_id[3:]
            if "comment" in temp_post_data:
                data_dict['Post Content'].append(str(temp_post_data['comment']))
                data_dict['Date'].append(str(temp_post_data["timeStamp"]))
                data_dict['Username'].append(str(temp_post_data["author_name"]))
                data_dict['Post ID'].append(post_id)
                data_dict['Title'].append(str(op_data["title"]))
                data_dict['URL'].append(str(op_data["url"]))

   #data_dict.drop(data_dict.index[data_dict['Username'] == "Automoderator"], inplace=True)
    df = pd.DataFrame(data_dict)
    df.drop(df[df['Username'] == "AutoModerator"].index, inplace=True)
    df.to_csv("C:\\Users\\Arzhang\\PycharmProjects\\redditDataProcessing\\post_data.csv")
    # open in readonly mode

    # do your stuff

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
