import json
import re

combined_flags = re.DOTALL | re.IGNORECASE

# Define the cleaning function
def clean_email_body(body):
    # Remove signatures, greetings, and footers using regex patterns
    body = re.sub(r'--.*', '', body, flags=combined_flags)  # Remove text after "--" (common in signatures)
    body = re.sub(r'Best,*', '', body, flags=combined_flags)  # Remove text after "Best," (common in signatures)
    body = re.sub(r'Sincerely,*', '', body, flags=combined_flags)  # Remove text after "Sincerely," (common in signatures)
    body = re.sub(r'Warm Regards,*', '', body, flags=combined_flags)  # Remove text after "Warm Regards," (common in signatures)
    body = re.sub(r'\u202f.*', '', body, flags=combined_flags) # Remove text after "\u202f"
    body = re.sub(r'Hi.*?,', '', body)  # Remove greetings like "Hi [Name],"
    body = re.sub(r'Best regards.*', '', body, flags=combined_flags)  # Remove closing phrases like "Best regards"
    body = re.sub(r'\n.*Sent with Mixmax.*', '', body, flags=combined_flags)  # Remove Mixmax signatures
    body = re.sub(r'(\n\n\*Spencer Goodwin).*', '', body, flags=combined_flags) # remove all text after my email signature
    body = re.sub(r'(\n\n\nSpencer Goodwin).*', '', body, flags=combined_flags) # remove all text after my email signature
    body = re.sub(r'(\n\n\n\nSpencer Goodwin).*', '', body, flags=combined_flags) # remove all text after my email signature
    body = re.sub(r'(\n\n\n\n\nSpencer Goodwin).*', '', body, flags=combined_flags) # remove all text after my email signature
    body = re.sub(r'(\n\n\n\n\n\nSpencer Goodwin).*', '', body, flags=combined_flags) # remove all text after my email signature    
    return body

# Path to the input and output JSON files
input_file = ''
output_file = ''


# Read and clean the JSON data
with open(input_file, 'r') as f:
    emails = json.load(f)

# Filter out the emails where 'from' is not 'Spencer Goodwin'
filtered_emails = [email for email in emails
                    if email['from'] == "Spencer Goodwin <sigood@umich.edu>" 
                    and "---------- Forwarded message ---------" not in email['body']
                    and "Begin forwarded message" not in email['body']]

# Clean the body of the remaining emails
for email in filtered_emails:
    email['body'] = clean_email_body(email['body'])

with open(output_file, 'w') as f:
    json.dump(filtered_emails, f, indent=4)


print("Email bodies cleaned and saved successfully.")
