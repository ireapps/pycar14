# import built-in python modules
# we'll want to access csv files and download files
# csv, which stands for comma-separated values, a file format that resembles a spreadsheet or database table in a text file.
# csv is a module that helps Python work with tabular data extracted from spreadsheets and databases
# urllib is a module that allows Python to make http requests to URLs on the web to fetch HTML
import csv
import urllib

# we're going to download a csv file
# what should we name it
file_name = "banklist.csv"

# use urllib.urlretrieve() to download the csv file from a url and save it to a directory
# csv link found at https://www.fdic.gov/bank/individual/failed/banklist.html
target_file = urllib.urlretrieve("http://www.fdic.gov/bank/individual/failed/banklist.csv", file_name)

# open the file to write
output_file = open('colorado_banks.csv', 'wb')

# create the writer object
writer = csv.writer(output_file, delimiter=',')

# open the csv file
with open(file_name, "rbU") as file:
    # use python's csv reader to access the contents
    # and create an object that represents the data
    csv_data = csv.reader(file)
    # write our header row to the output csv
    header_row = csv_data.next()
    writer.writerow(header_row)
    # loop through each row of the csv
    for row in csv_data:
        # if the state field equals georgia
        if row[2] == "CO":
            # write the row to the new csv file
            writer.writerow(row)
            print(row)
        # otherwise continue on
        else:
            continue
    # close the output file
    output_file.close()

# if you want to try similar code to create csvs for all 50 states, check out this extra credit:
# https://github.com/rnagle/pycar/blob/master/project1/extra_credit_state_banks_complete.py
