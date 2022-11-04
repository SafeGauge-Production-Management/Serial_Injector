# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 12:03:40 2022

@author: 61477
"""

def write_serial_to_file(serialNo):

    lineUntilSerial = "<service uuid=\"477b695e-fb98-4cfc-9c89-539326"
    lineAfterSerial = "\" advertise=\"true\">\n"
    
    # import serial numbers as a list
    # fopen( )
    # filePath = filePicker( )
    
    #easygui.egdemo()
    
    with open("QPS_gatt_sensor.xml", "r") as file: #In future be able to pick the file path
        contents = file.readlines()
        
    
    # contents[17] = "<service uuid=\"477b695e-fb98-4cfc-9c89-539326BEEEEF\" advertise=\"true\">\n"
    
    joinTheseStrings = [lineUntilSerial, serialNo, lineAfterSerial]
    
    newSerialLine = ''.join(joinTheseStrings)
    contents[17] = newSerialLine
    #print(newSerialLine)
    
    # print(contents[17])
    # contents.insert(indexLine, value)
    
    with open("QPS_gatt_sensor.xml", "w") as file:
        contents = "".join(contents)
        file.writelines(contents)
    
    # take the first serial number https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
    
    file.close()