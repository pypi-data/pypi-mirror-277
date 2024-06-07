"""
Author: Janelle Ogg 
This function summerises (in excel format) the paramaters used in each 12D sight distance report located in the folder were the script is run

"""

def sightparameters():
    
    import os
    import re
    import pandas as pd
    from bs4 import BeautifulSoup
    import matplotlib.pyplot as plt
    import matplotlib.ticker as tck
    from tabulate import tabulate
    import numpy as np

    values=np.array([])
    parameters=np.array([])
    paramvalues = {}
    paramvalues["PARAMETERS"]=""

    for filename in os.listdir('.'):#['NDD BC1.html']: # ['NDD BC1.html', 'NDD BC2T.html']:#os.listdir('.')
        if filename.endswith('.html'):
            with open(filename, 'r',encoding="utf-16") as f:
                contents = f.read()
                soup = BeautifulSoup(contents, 'html.parser')
                # find all the title tags
                titles = soup.find_all("title")

                # loop over the titles and print their text
                for title in titles:
                    #print(title.text)
                    X=title.text
            
                if X=="Sight Distance Report - 12d Model":
                    
                    table = soup.find("table", id="sd_params") # this finds the table tag with id="mytable"
                    name=filename
                    name=filename.replace(".html","")
                            
                    W=np.array([])
                    rows = table.find_all("tr")
                    # Loop through the rows and print each cell
                    for row in rows:
                        cells = row.find_all(["td", "th"])
                        for cell in cells:
                        
                                #print(cell.get_text(), end="\t")
                            W=np.append(W,[cell.get_text()])
                    
                    
                    values=(W[21],W[25],W[30],W[32],W[34])
                    parameters=(W[20],W[24],W[29],W[31],W[33])

                    paramvalues[filename.split('.')[0]]=values
                    


    paramvalues["PARAMETERS"]=parameters
    table = tabulate(paramvalues, headers="keys")

    # Print the table
    print(table)

    df=pd.DataFrame(paramvalues)
    df.to_excel('output1.xlsx', engine='xlsxwriter')  # doctest: +SKIP

    print('')
    x = input("Press enter to plot table above to output1.xlsx and visually plot Sight Distance Capability...")
