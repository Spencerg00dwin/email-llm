import mailbox
import json
import sys

def get_email_body(message):
    if message.is_multipart():
        parts = message.get_payload()
        body = ''
        for part in parts:
            if part.get_content_type() == 'text/plain':
                body += part.get_payload(decode=True).decode('utf-8', errors='replace')
        return body
    else:
        return message.get_payload(decode=True).decode('utf-8', errors='replace')

def mbox_to_json(mbox_path, output_path):
    mbox = mailbox.mbox(mbox_path)
    messages = []

    for message in mbox:
        msg = {
            'subject': message['subject'],
            'from': message['from'],
            'to': message['to'],
            'date': message['date'],
            'body': get_email_body(message)
        }
        if msg['body'] != "":
            messages.append(msg)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)

# Define the path to the uploaded .mbox file and the output .json file
mbox_path = sys.argv[1]
json_path = sys.argv[2]

# Convert the provided .mbox file to .json
mbox_to_json(mbox_path, json_path)

json_path
