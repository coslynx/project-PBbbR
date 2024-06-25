import pandas as pd

def read_csv_files(group_file_path, hostel_file_path):
    group_data = pd.read_csv(group_file_path)
    hostel_data = pd.read_csv(hostel_file_path)
    return group_data, hostel_data

def allocate_rooms(group_data, hostel_data):
    allocated_rooms = pd.DataFrame(columns=['Hostel Name', 'Room Number', 'Group ID', 'Member Name', 'Gender'])
    
    for index, group_row in group_data.iterrows():
        group_id = group_row['Group ID']
        group_size = group_row['Number of Members']
        group_gender = group_row['Gender']
        
        available_hostels = hostel_data[(hostel_data['Capacity'] >= group_size) & (hostel_data['Gender'] == group_gender)]
        
        for index, hostel_row in available_hostels.iterrows():
            allocated_rooms = allocated_rooms.append({'Hostel Name': hostel_row['Hostel Name'], 
                                                      'Room Number': hostel_row['Room Number'], 
                                                      'Group ID': group_id, 
                                                      'Member Name': 'Member 1', 
                                                      'Gender': group_gender}, 
                                                     ignore_index=True)
            group_size -= 1
            if group_size == 0:
                break
    
    return allocated_rooms

group_data, hostel_data = read_csv_files('data/group.csv', 'data/hostel.csv')
allocated_rooms = allocate_rooms(group_data, hostel_data)
allocated_rooms.to_csv('output/allocated_rooms.csv', index=False)