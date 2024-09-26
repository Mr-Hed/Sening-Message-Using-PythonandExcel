import pandas as pd
import pywhatkit as kit
import time

# Step 1: Read phone numbers from Excel
file_path = r'C:\Users\hemre\PycharmProjects\pythonProject\phone_numbers.xlsx' # You have to save your excel file which includes phone number here.
                                                                               #If your file is different you have to change las part.
df = pd.read_excel(file_path)

# Step 2: Loop through the phone numbers and send a message
message = "Hello, this is a test message!"  # Your message content
for index, row in df.iterrows():
    phone_number = row['Phone Number'] #You have to write your Row's name here.

    # Step 3: Send the WhatsApp message
    try:
        kit.sendwhatmsg_instantly(f"+{phone_number}", message, 5, True, 1)  # 5-second wait between messages
        print(f"Message sent to {phone_number}")

        time.sleep(10)  # Adjust this delay as needed
    except Exception as e:
        print(f"Failed to send message to {phone_number}. Error: {e}")

