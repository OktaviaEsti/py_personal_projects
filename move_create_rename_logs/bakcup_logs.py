import time
import threading
import datetime
import os
import argparse
import stat

# Function to read target folders from user input
def read_folder():
    # Create the parser
    parser = argparse.ArgumentParser(description='Python program to backup collected logs and move the colected logs to new directory then reate new files for the incoming new logs. \n Example : pyhton3 backup_logs.py /var/log/collected_syslogs /var/log/collected_syslogs_backup')
    # Add arguments
    parser.add_argument('idir', type=str, help='Input directory path where the logs want to be processed')
    parser.add_argument('odir', type=str, help='Output directory path for the processed logs')

    # Parse the arguments
    args = parser.parse_args()
    # Validate if the directories exist
    if not os.path.exists(args.idir):
        print(f"Error: Directory '{args.idir}' does not exist.")
        exit(1)
    if not os.path.exists(args.odir):
        print(f"Error: Directory '{args.odir}' does not exist.")
        exit(1)
    return (args.idir, args.odir)

# Define the function to be executed
def test(input_folder, output_folder):
        dateformat=time_tracker()
        # Set the permissions (mode) for the node (default is 0o600)
        per = 0o600
        # Define the type of node to be created (file in this case)
        node_type = stat.S_IRUSR
        mode = per | node_type

        for each_log in os.listdir(input_folder):
            print ("log: "+each_log)
            if each_log.lower().endswith(".log"):
                old_path = os.path.join(input_folder, each_log)
                new_name = f"{each_log[:-4]}({dateformat}).log"
                new_path = os.path.join(output_folder, new_name)
                os.rename(old_path, new_path)
                #create_new_file = os.path.join(old_path, f"{each_log}")
                #print("cnf: " + create_new_file)
                os.mknod(old_path, mode)
                print(f"Renamed: {each_log} -> {new_name}")
            else:
                old_path = os.path.join(input_folder, each_log)
                if os.path.isdir(old_path):
                    print("Is a directory, not a log")
                    continue
                new_name = f"{each_log}({dateformat})"
                new_path = os.path.join(output_folder, new_name)
                os.rename(old_path, new_path)
                #create_new_file = os.path.join(old_path, f"{each_log}")
                os.mknod(old_path, mode)
                print(f"Renamed: {each_log} -> {new_name}")

# Define a function to run the test function every week
def time_tracker():
    now = datetime.datetime.now()
    # Display a message indicating what is being printed
    print("Current date and time : ")
    # Print the current date and time in a specific format
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    dateformat=(now.strftime("%Y-%m-%d_%H-%M")) #format for the renamed file
    return dateformat
infolder, outfolder = read_folder()
test(infolder,outfolder)
print("Pemindahan folder selesai")