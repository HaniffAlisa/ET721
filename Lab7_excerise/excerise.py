""" Alisa Haniff
September 23, 2024
Lab 7 Excerise Email address"""

def email_read():
    try:
        # Open the file and read email
        with open('user_email.txt', 'r') as infile:
            gmail_count = 0
            yahoo_count = 0
            hotmail_count = 0

            # Loop through each line 
            for line in infile:
                # Split the line by ',' to split the email address
                parts = line.split(',')
                if len(parts) > 1:  
                    email = parts[1]  

                    if '@gmail.com' in email:
                        gmail_count += 1
                    elif '@yahoo.com' in email:
                        yahoo_count += 1
                    elif '@hotmail.com' in email:
                        hotmail_count += 1
        
        # Append the results to reportemail.txt
        with open('reportemail.txt', 'a') as outfile:
            outfile.write(f"Gmail users: {gmail_count}\n")
            outfile.write(f"Yahoo users: {yahoo_count}\n")
            outfile.write(f"Hotmail users: {hotmail_count}\n")
        
        print("Report appended successfully to 'reportemail.txt'.")
    except FileNotFoundError:
        print("Error: The file 'user_email.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


email_read()
