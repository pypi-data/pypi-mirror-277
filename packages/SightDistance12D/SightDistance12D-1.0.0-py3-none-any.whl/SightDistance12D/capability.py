"""
Sight Distance Capability
-this function summerises the capbaility of 12D sight distance reports located in the file path that the script is run in.  
-observe naming convention in DEFAULT_SORT_ORDER

Author: Jacob Barton 08/11/2023
HTML Titile check added by Janelle ogg 09/11/2023
Code trasfered into sight distance package as a function  Janelle Ogg 06/06/2024

"""
def sightcapability ():
    import os
    import re
    import pandas as pd
    import numpy as np
    from bs4 import BeautifulSoup
    import matplotlib.pyplot as plt
    import matplotlib.ticker as tck


    DATA_HEADERS = ['Chainage', 'Sight_Distance_Achieved', 'Sight_Distance_Required', 'Status', 'Obstruction_Type', 'Obstruction_Chainage', 'Obstruction_Offset', 'Obstruction_Height', 'Obstruction_Name']


    DEFAULT_SORT_ORDER = ['NDD BC1 (F)', 'NDD BC1 (R)', 'NDD BC2T (F)', 'NDD BC2T (R)', 'EDD BC1 (F)', 'EDD BC1 (R)',
                        'EDD BC2T (F)','EDD BC2T (R)','EDD CC1 (F)', 'EDD CC1 (R)', 'EDD CC2T (F)', 'EDD CC2T (R)',
                        'EDD CC3 (F)', 'EDD CC3 (R)', 'EDD CC4 (F)', 'EDD CC4 (R)','EDD SC1 (F)','EDD SC1 (R)',
                        'EDD SC2 (F)','EDD SC2 (R)']




    def extract_dataframe_from_html_table(html_table,direction='forward'):
        """
        Function takes html table object and converts it to pandas dataframe 
        """

        data_table = []
        r = 0
        for tr in html_table.find_all("tr"):
            if r < 2:
                r += 1
                continue
            else:
                r += 1
            #print(tr)
            #chainage = float(tr.find("td",{"class": "chainage"}).text)
            _chainage1, _length1, _length2, _status, _type, _chainage2, _offset, _height, _name = tr.find_all("td")

            Chainage = float(_chainage1.text)
            Sight_Distance_Achieved = float(_length1.text)
            Sight_Distance_Required = float(_length2.text)
            Status = _status.text
            if _status.text == 'passed':
                Status = 0 # 0 for pass
            else:
                Status = 1 # 1 for failure
                
            Obstruction_Type = _type.text
            if _chainage2.text == '':
                Obstruction_Chainage = None
            else:
                Obstruction_Chainage = float(_chainage2.text)
            if _offset.text == '':
                Obstruction_Offset = None
            else:
                Obstruction_Offset = float(_offset.text)
            if _height.text == '':
                Obstruction_Height = None
            else:
                Obstruction_Height = float(_height.text)
            Obstruction_Name = _name.text


            data_row = [Chainage, Sight_Distance_Achieved, Sight_Distance_Required, Status, Obstruction_Type, Obstruction_Chainage, Obstruction_Offset, Obstruction_Height, Obstruction_Name]
            data_table.append(data_row)

        
        df = pd.DataFrame(data_table, columns = DATA_HEADERS)
        return df


    def sort_func(val, list2):
        """helper function to sort lists into prefered format"""
        if val in list2:
            return list2.index(val)
        else:
            return 99

    """
    loop through all html files in folder
    extract forward and reverse html tables
    convert tables to pandas data frames
    add data frames to a dictionary called test_cases, with (F) or (R) prefix to indicate direction

    """

    test_cases = {}
    for filename in os.listdir('.'):#['NDD BC1.html']: # ['NDD BC1.html', 'NDD BC2T.html']:#os.listdir('.')
        if filename.endswith('.html'):
            with open(filename, 'r',encoding="utf-16") as f:
                
                case_ref = filename.split(".")[0]
                contents = f.read()
                #x = re.search(r'<table id="sd_params">[\s\S]*?<\/table>',contents)
                soup = BeautifulSoup(contents, 'html.parser')
                # find all the title tags
                titles = soup.find_all("title")

                # loop over the titles and print their text
                for title in titles:
                    #print(title.text)
                    X=title.text
            
                if X=="Sight Distance Report - 12d Model":

                    ssd_table_fwd, ssd_table_rev  = soup.find_all("table", {"class": "setout"})

                    df_fwd = extract_dataframe_from_html_table(ssd_table_fwd)
                    df_rev = extract_dataframe_from_html_table(ssd_table_rev, "reverse")
                    df_rev = df_rev.sort_values('Chainage') #make same as df_fwd
                    test_cases['{0} {1}'.format(case_ref, '(F)')] = df_fwd
                    test_cases['{0} {1}'.format(case_ref, '(R)')] = df_rev
                    #print("'{0} {1}'".format(case_ref, '(F)'))
                    #print("'{0} {1}'".format(case_ref, '(R)'))
        
        


    #sort the test case list out in default format
    sorted_test_case_list = list(test_cases.keys())
    sorted_test_case_list.sort()
    sorted_test_case_list = sorted(sorted_test_case_list, key=lambda x: sort_func(x,DEFAULT_SORT_ORDER))

    #get the min/max chainage range across all html files to plot envelope for
    min_chainage = 10000000.0
    max_chainage = 0.0
    for case_ref in sorted_test_case_list:
        df = test_cases[case_ref]
        min_chainage = min(min_chainage, df['Chainage'].min())
        max_chainage = max(max_chainage, df['Chainage'].max())

    min_chainage = np.round(min_chainage)
    max_chainage = np.round(max_chainage)

    #initialise mask data frame to hold envelope data
    chg_range = np.arange(min_chainage, max_chainage+1.00,1.00)
    df_mask = pd.DataFrame(
        {'Chainage' : chg_range,
        'Status' : np.zeros(len(chg_range),dtype=int)
        })

        
    i = 0
    for case_ref in sorted_test_case_list:
        i += 1 #this will be the y position to plot case at
        
        df = test_cases[case_ref] #extract dataframe for reference case
        df['g'] = df['Status'].ne(df['Status'].shift()).cumsum() #find descreet groups
        #iterate through each unique group
        if int(df.g.unique().max()) == 1 and int(df[df.g==1].head(1).Status) == 0:
            print("{0} - passes at all locations.".format(case_ref))
        else:
            print("{0} - fails at the following locations:".format(case_ref))
            
            
        for g in df.g.unique():
            chainage_start = df[df.g==g]['Chainage'].min()
            chainage_end = df[df.g==g]['Chainage'].max()
            obstruction_type = str(df[df.g==g].iloc[0].Obstruction_Type)
            obstruction_name = str(df[df.g==g].iloc[0].Obstruction_Name)
            
            status = df[df.g==g].head(1).Status #get first row

            xvals = [chainage_start, chainage_end]
            yvals = [i,i]

            #print results to output window and plot pass/fail locations
            if int(status) == 1:
                print("Ch{0} - Ch{1} ({2}, {3})".format(chainage_start,chainage_end,obstruction_type,obstruction_name))
                df_mask.loc[(df_mask['Chainage'] >= chainage_start) & (df_mask['Chainage'] <= chainage_end), 'Status'] = 1 #mask the chainages that fail
                plt.plot(xvals, yvals, color='red', linewidth = 4)
                #print("fail")
            else:
                plt.plot(xvals, yvals, color='green', linewidth = 2)
                #print("pass")


    ## Now plot the failure envelope
    i += 1
    df_mask['g'] = df_mask['Status'].ne(df_mask['Status'].shift()).cumsum() #find descreet groups
    if int(df_mask.g.unique().max()) == 1 and int(df_mask[df_mask.g==1].head(1).Status) == 0:
        print("{0} - passes at all locations.".format("Envelope of all cases"))
    else:
        print("{0} - fails at the following locations:".format("Envelope of all cases"))
    for g in df_mask.g.unique():
        chainage_start = df_mask[df_mask.g==g].Chainage.min()
        chainage_end = df_mask[df_mask.g==g].Chainage.max()        
        status = df_mask[df_mask.g==g].head(1).Status #get first row
        xvals = [chainage_start, chainage_end]
        yvals = [i,i]
        if int(status) == 1: #fails
            print("Ch{0} - Ch{1}".format(chainage_start,chainage_end))
            plt.plot(xvals, yvals, color='magenta', linewidth = 6)
        else: #passes
            plt.plot(xvals, yvals, color='green', linewidth = 2)



    #format the plot
    sorted_test_case_list.append("ENVELOPE")
    plt.yticks(range(1,len(sorted_test_case_list)+1), sorted_test_case_list)
    plt.grid(axis = 'x',color = 'grey', linestyle = '--', linewidth = 0.5, which="both")
    plt.minorticks_on()
    plt.xlabel('Chainage (m)')
    plt.title('Sight Distance Capability')


    #make plot visible to user
    plt.show()

