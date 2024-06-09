import mailbox
import sys
import os

def split_mbox(input_path, num_splits=4):
    mbox = mailbox.mbox(input_path)
    total_messages = len(mbox)
    messages_per_split = total_messages // num_splits

    base_name, ext = os.path.splitext(input_path)

    for i in range(num_splits):
        start_index = i * messages_per_split
        end_index = (i + 1) * messages_per_split if i < num_splits - 1 else total_messages

        output_path = f"{base_name}_part{i+1}{ext}"
        output_mbox = mailbox.mbox(output_path, create=True)

        for j in range(start_index, end_index):
            output_mbox.add(mbox[j])

        output_mbox.close()
        print(f"Created {output_path} with messages from {start_index} to {end_index-1}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python split_mbox.py <MBOX_FILE>")
        sys.exit(1)

    input_mbox_path = sys.argv[1]
    print(f"Mailbox length: {len(mailbox.mbox(input_mbox_path))}")
    split_mbox(input_mbox_path)
