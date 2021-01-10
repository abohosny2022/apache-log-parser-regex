#####################################################################################################################
###########################################  TASK   ######################################################
# -	your tool will have the following features:
# -	Parse access.log files and extract all included information (IPs, URIs, Methods, Unique user agents )
# -	Extract unique IPs
# -	Let the user choose an IP to return all his requests
# -	give the user the option to choose between different status codes and return the URIs that are requested and returned these codes
# -	Use REGEX
######################################################################################################################

import csv
import re
import requests
from urllib.error import URLError,HTTPError
from urllib.request import urlopen

def Readfromurl():     ######### to request from url ################
    Righturl="http://www.almhuette-raith.at/apache-log/access.log"
    desired_URL = input("Please, enter the desired log-access-URL: ")
    try:
        response = urlopen(desired_URL)
    except HTTPError as e:
        print ('We failed to reach a server.')
        print('Error code: ', e.code)
        print("###################  Repeat Again ########################## ")
        Readfromurl()
    except URLError as e:
        print('Error reach a server.')
        print('Reason: ', e.reason)
        print("###################  Repeat Again ########################## ")
        Readfromurl()
    else:
        print('Good URL.')
        if (desired_URL == Righturl):
                logs_string = requests.get(desired_URL).text
                with open('logs.txt', 'w+') as log:
                    log.write(logs_string)
                    print('Data written in the txt file ')
                log.close()
        else:
                print("Not the Desired URL Rightnow to get logs in this case")
                Readfromurl()
def savedcsvpath():   ######### You can write in the run     anyname.csv    will shown in the path of program #########################
    print("############################################################################")
    output_path = input("Write the path or name of file that structed data will shown (.csv): ")
    return output_path
def csvconverted(inptxtfile,path):
    parts = (r'(?P<ip>.*?)\s'  # host %h
             r'(?P<identity>\S*)\s'  # indent %l (unused)
             r'(?P<user>\S*)\s'  # user %u
             r'\[(?P<time>.+)\]\s'  # time %t
             r'"(?P<request_method>.*) (?P<path>.*)(?: (?P<request_version>HTTP/.*))"\s'  # request "%r"
             r"(?P<status>\d+)\s"  # status %>s
             r'(?P<size>.\S*)\s'  # size %b (careful, can be '-')
             r'"(?P<referrer>.*?)"\s'
             r'"(?P<user_agent>.*?)"\s*')

    pattern = re.compile(parts)
    with open(path, 'w') as out:           #convert file to csv structred file
        csv_out = csv.writer(out)  # the headers will show in the csv file
        csv_out.writerow(
            ['host', 'identity', 'user', 'time', 'request method', 'path', 'request_version', 'status', 'size',
             'referer', 'user agent'])
        for line in inptxtfile:
            if (line !="\n"):
                m = pattern.match(line)  # match line by line with pattern
                result = m.groups()  # get all data groups and fill in this file
                csv_out.writerow(result)  # write in this file
    out.close()
    return out
def Getuniqueips():
                          #extract and Get unique IPS into csv File

    parts = (r'(?P<host>.*?)\s'  # host %h
             r'(?P<identity>\S*)\s'  # indent %l (unused)
             r'(?P<user>\S*)\s'  # user %u
             r'\[(?P<time>.+)\]\s'  # time %t
             r'"(?P<request_method>.*) (?P<path>.*)(?: (?P<request_version>HTTP/.*))"\s'  # request "%r"
             r"(?P<status>\d+)\s"  # status %>s
             r'(?P<size>.\S*)\s'  # size %b (careful, can be '-')
             r'"(?P<referrer>.*?)"\s'
             r'"(?P<user_agent>.*?)"\s*')
    pattern = re.compile(parts)
    ###########################################  Extract Unique IPS ########################################
    chossse=input("Enter desired input (f) write output file (r) write on Run : ")
    if (chossse=="f"):
            with open('logs.txt', 'r') as logs_file:
                file = logs_file.readlines()
            with open('uniqueips.csv', 'w+') as out2:
                csv_outunipueips = csv.writer(out2)
                csv_outunipueips.writerow(['Unique Hosts'])
                list2 = []                 #this list will contain all ips
                for line2 in file:
                    if (line2 != "\n"):
                        m2 = pattern.match(line2)
                        result2 = m2.group(1)
                        list2.append(result2)
                # print(list2)
                res_list = []              #this list will contain unique ips
                for item in list2:
                    if item not in res_list:
                        res_list.append(item)

                csv_outunipueips.writerow(res_list)
            out2.close()
    elif(chossse=="r"):
            with open('logs.txt', 'r') as logs_file:
                 file = logs_file.readlines()
            list2 = []  # this list will contain all ips
            for line2 in file:
                if (line2 != "\n"):
                    m2 = pattern.match(line2)
                    result2 = m2.group(1)
                    list2.append(result2)
            print(list2)
            res_list = []  # this list will contain unique ips
            for item in list2:
                if item not in res_list:
                    res_list.append(item)
            print(res_list)
    else:
            print("Error , You can Repeat Again")
            Getuniqueips()
def printuniqpue(log2):
    #this function will use in fuction searchip to avoid  not valid ip synatx like xxxx.xxx.xx.xxxx
    print("############################################################################")
    parts = (r'(?P<host>.*?)\s'  # host %h
             r'(?P<identity>\S*)\s'  # indent %l (unused)
             r'(?P<user>\S*)\s'  # user %u
             r'\[(?P<time>.+)\]\s'  # time %t
             r'"(?P<request_method>.*) (?P<path>.*)(?: (?P<request_version>HTTP/.*))"\s'  # request "%r"
             r'(?P<status>[0-9]+)\s'  # status %>s
             r'(?P<size>.\S*)\s'  # size %b (careful, can be '-')
             r'"(?P<referrer>.*?)"\s'
             r'"(?P<user_agent>.*?)"\s*')

    pattern = re.compile(parts)
    #test = open(log2)
    list2 = []  # this list will contain all ips
    for line2 in log2:
        if (line2 !="\n"):
            m2 = pattern.match(line2)
            result2 = m2.group(1)
            list2.append(result2)
    res_list = []  # this list will contain unique ips
    for item in list2:
        if item not in res_list:
            res_list.append(item)

    return res_list
def searchforip(csvfile,ipslist):       #funtion for search an user ip
                                # format of ipv4 xxx.xxx.xxx.xxx
    print(ipslist)
    yourip = input("Enter ip that you want to search like avaible list as shown above : ")  # let user to enter Ip or domain
    if (yourip in ipslist): #check enter user ip with correct format like txt file
            csv_out = csv.DictReader(open(csvfile, 'r'))
            print("Choose if you want to show result in File --->> (f) in Run --->> (r)")
            choose=input("Enter your choose :  ")
            if ( choose == "f" ):
                path = input("Enter the name or path for your result file like (x.txt) or (full path.txt) : ")
                file = open(path, 'w')
                for line in csv_out:
                    if (line !="\n"):                   #to escape empty line
                        if yourip == line['host']:      #comparing between ips
                            file.writelines(str(line.items()))      #write the reult into the file
            elif (( choose == "r" )):
                for line in csv_out:
                    if (line != "\n"):
                        if yourip == line['host']:
                            if line['request method'] == 'GET' or line['request method'] == 'POST':
                                print(line['host'], line['path'], line['request method'], line['user agent'])
            else:
                print("Invaild input :)))))")

    else:
             print("Invalid IP synatx or Ip Not in the logs file , TRY Again")
             searchforip(csvfile,ipslist)
def checkstatus(csvfiles):  # funtion for check status ( (200) -- (303) -- (404) -- (304) -- (403) )
        print("############################################################################")

        print("Choose your status code if  (200) -- (303) -- (404) -- (304) -- (403) ")
        statuss = input("Enter status code that you want to search: ")  # let user to enter status code
        if (statuss == '200'):
                csvoutput = csv.DictReader(open(csvfiles, 'r'))
                chos = input("Enter Your chose (f) write in file or (r) read in Run : ")
                if (chos == "f"):
                    pathh = input("Enter the name or path for your result file like (x.txt) or (full path.txt) : ")
                    out200 = open(pathh, 'w')
                    for line in csvoutput:
                        if (line != "\n"):
                            if statuss == line['status']:  # comparing between status code
                                out200.writelines(str(line.items()))  # write the result into the file
                elif (chos == "r"):
                    for line in csvoutput:
                        if (line != "\n"):
                            if statuss == line['status']:
                                if line['status'] == '200':
                                    print(line['status'], "  ", line['host'], " ", line['request method'], "  ",
                                          line['path'], "  ", line['user agent'])
                else:

                        print("Invaild input :)))))")

        elif (statuss == '303'):
                csvoutput = csv.DictReader(open(csvfiles, 'r'))  # read from csv file after converted with structured data
                chos = input("Enter Your chose (f) in file or (r) read in Run : ")
                if (chos == "f"):
                    pathm = input("Enter the name or path for your result file like (x.txt) or (full path.txt) : ")
                    out303 = open(pathm, 'w')
                    for line in csvoutput:
                        if (line != "\n"):
                            if statuss == line['status']:  # comparing between status codes
                                out303.writelines(str(line.items()))  # write the result into the file
                elif (chos == "r"):
                    for line in csvoutput:
                        if (line != "\n"):
                            if statuss == line['status']:
                                if line['status'] == '303':
                                    print(line['status'], "  ", line['host'],"  ", line['request method'], "  ",
                                          line['path'], "  ", line['user agent'])
                else:

                        print("Invaild input :)))))")

        elif (statuss == '403'):
                csvoutput = csv.DictReader(open(csvfiles, 'r'))  # read from csv file after converted with structured data
                chos = input("Enter Your chose (f) in file or (r) read in Run : ")
                if (chos == "f"):
                    pathm = input("Enter the name or path for your result file like (x.txt) or (full path.txt) : ")
                    out303 = open(pathm, 'w')
                    for line in csvoutput:
                        if (line != "\n"):
                            if statuss == line['status']:  # comparing between status codes
                                out303.writelines(str(line.items()))  # write the result into the file
                elif (chos == "r"):
                    for line in csvoutput:
                        if (line != "\n"):
                            if statuss == line['status']:
                                if line['status'] == '403':
                                    print(line['status'], "  ", line['host'], "  ", line['request method'], "  ",
                                          line['path'], "  ", line['user agent'])
                else:

                    print("Invaild input :)))))")
        elif (statuss == '304'):
                csvoutput = csv.DictReader(open(csvfiles, 'r'))  # read from csv file after converted with structured data
                chos = input("Enter Your chose (f) in file or (r) read in Run : ")
                if (chos == "f"):
                    pathm = input("Enter the name or path for your result file like (x.txt) or (full path.txt) : ")
                    out303 = open(pathm, 'w')
                    for line in csvoutput:
                        if (line != "\n"):
                            if statuss == line['status']:  # comparing between status codes
                                out303.writelines(str(line.items()))  # write the result into the file
                elif (chos == "r"):
                    for line in csvoutput:
                        if (line != "\n"):
                            if statuss == line['status']:
                                if line['status'] == '304':
                                    print(line['status'], "  ", line['host'], "  ", line['request method'], "  ",
                                          line['path'], "  ", line['user agent'])
                else:

                    print("Invaild input :)))))")
        elif (statuss == '404'):
                csvoutput = csv.DictReader(open(csvfiles, 'r'))  # read from csv file after converted with structured data
                chos = input("Enter Your chose (f) in file or (r) read in Run : ")
                if (chos == "f"):
                    patt = input("Enter the name or path for your result file like (x.txt) or (full path.txt) : ")
                    out404 = open(patt, 'w')
                    for line in csvoutput:
                        if (line != "\n"):
                            if statuss == line['status']:  # comparing between status code
                                out404.writelines(str(line.items()))  # write the result into the file
                elif (chos == "r"):
                    for line in csvoutput:
                        if (line != "\n"):
                            if statuss == line['status']:
                                if line['status'] == '404':
                                    print(line['status'], "  ", line['host'],"  ", line['request method'], "  ",
                                          line['path'], "  ", line['user agent'])
                else:

                        print("Invaild input :)))))")

        else:
                print("Invalid status code :(((((((( ")


####################################### Call Functions #####################################


Readfromurl()
Getuniqueips()
with open('logs.txt', 'r') as logs_file:
     loggs = logs_file.readlines()
returnedips=printuniqpue(loggs)
csvpath=savedcsvpath()
csvconverted(loggs,csvpath)
searchforip(csvpath,returnedips)
checkstatus(csvpath)