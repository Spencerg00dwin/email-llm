import json

input_file_json = './Json-mail/final_cleaned.json'
output_file_txt = './Json-mail/emails.txt'

# Read the JSON file
with open(input_file_json, 'r') as f:
    emails = json.load(f)

# Open the output text file in write mode
with open(output_file_txt, 'w') as f:
    for email in emails:
        # Extract the body of the email
        body = email['body']
        # Write the body to the text file followed by a newline
        f.write(body + "\n\n")
