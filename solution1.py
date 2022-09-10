from csv import DictReader, DictWriter
import csv
from datetime import datetime


def open_csv() :
    output_data = []
    # output_index = 1
    comp_list = []
    duplicates = False
    file_handle = open("sent_for_review/weather_review.csv", "r", encoding="UTF8")
    reader = DictReader(file_handle)
    for row in reader :
        out_row = {
            'account' : row['account'],
            'date' : row['date']
            # 'index' : output_index
        }
        # If dupe_count > 1, don't add to final file
        dupe_count = 0
        # Account get() to compare to list
        acc_num = out_row.get('account')
        input_date = datetime.strptime(out_row.get('date'), "%d/%m/%Y")
        # If comp_list is empty, add first out_row then continue to 2nd iteration
        if len(comp_list) == False :
            comp_list.append(out_row)
            output_data.append(out_row)
            # output_index +=1
            continue
        # If not empty, compare account
        else :
            for comp_dict in comp_list :
                comp_acc_num = comp_dict.get('account')
                comp_date = datetime.strptime(comp_dict.get('date'), "%d/%m/%Y")
                # No duplicate, assign False
                if acc_num != comp_acc_num :
                    duplicates = False
                # If equal, proceed to compare dates
                else :
                    duplicates = True
                    dupe_count += 1
                    # Datetime comparision to figure out what is the instance with the latest date
                    # If out_row is a more up-to-date, update comp_list
                    if input_date > comp_date :
                        comp_dict.update(out_row)
                        

        # Outside of comparison loop
        if duplicates == False and dupe_count == 0:
            output_data.append(out_row)  
            # output_index += 1
            

        # Add to comp_list no matter the result for comparison
        comp_list.append(out_row)    


    file_handle.close()
    write_csv(output_data)


def write_csv(in_data) :
    csvfile = open("sent_for_review/output_file2.csv", "w",  newline= "", encoding="utf-8") 
    writer = DictWriter(csvfile, fieldnames = ['account', 'date'])
    
    writer.writeheader()
    writer.writerows(in_data)


    csvfile.close()



if __name__ == "__main__" :
    open_csv()