# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:34:48 2018

@author: Michael Pesin
"""
from os import listdir, rename
from os.path import isfile
from re import search
from shutil import copy2

FILES_SOURCE_PATH = r"""C:\Users\Michael Pesin\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"""
def Validation(nameToCheck, existingNames):
        
    if nameToCheck in existingNames:
        print("passed on Previously Renamed")
        return False      
    else:  
        if search('[a-zA-Z]', nameToCheck) != None:        
            if search('.*\.jpg', nameToCheck) == None:    
                if search('.*\.txt', nameToCheck) == None:
                    if search('.*\.py', nameToCheck) == None:
                        return True
                    else:
                        print("passed on .py")
                else:
                    print("passed on .txt: %s" % nameToCheck)
            else:
                print("passed on .jpg: %s" % nameToCheck)
        else:
            print("passed on [a-zA-Z]: %s" % nameToCheck)
    print("passed on Other Reason")
    return False    

startMessage = input("Start Renaming? Y/N: ")

if startMessage == 'Y' or startMessage == 'y': 
    
    renamedFileNamesList = list()
    addToRenameFileNamesList = list()
    
#   Get Index for th efile name
    print("Getting Index for naming...")
    with open('NamingIndex.txt','r') as index:
        firstLineWithIndex = index.readline()
        fileNameIndex = int(search('[0-9]+', firstLineWithIndex).group(0))
    
#   Get Converted files  
    print("Getting list of converted files...")  
    with open('RenamedFiles.txt', 'r') as renamedSet:        
        for line in renamedSet:
            renamedFileNamesList.append(line.replace("\n", ''))
    
#   Copy the file to the folder
    print("Copying new files...")
    for filename in listdir(FILES_SOURCE_PATH):
        res = Validation(filename, renamedFileNamesList)
        if res:
            copy2("%s\\%s" % (FILES_SOURCE_PATH, filename), "%d.jpg" % fileNameIndex)
            fileNameIndex += 1
            addToRenameFileNamesList.append(filename)
#   Add newly converted files to the list
    print("Indexing newly %d converted files..." % len(addToRenameFileNamesList))
    with open('RenamedFiles.txt', 'a') as renamedSet:
        for item in addToRenameFileNamesList:
            renamedSet.write("%s\n" % item)
            
#   Update Index 
    print("Updating naming index to %d..." % fileNameIndex)       
    with open('NamingIndex.txt','w') as index:
        newIndex = "Last_Index=%d" % fileNameIndex
        index.write(newIndex)
    
    print("Finished! Good Day!")
else:
    print("Nothing was executed. Goodbye!")
    
input()