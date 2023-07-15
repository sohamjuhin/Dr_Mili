import sys
import email
from email.header import decode_header

# Function to decode email header
def decode_email_header(header):
    decoded_parts = decode_header(header)
    decoded_header = ""
    for part, encoding in decoded_parts:
        if isinstance(part, bytes):
            if encoding:
                decoded_header += part.decode(encoding)
            else:
                decoded_header += part.decode()
        else:
            decoded_header += part
    return decoded_header

# Function to analyze email headers
def analyze_email_headers(email_path):
    try:
        with open(email_path, "rb") as email_file:
            email_message = email.message_from_binary_file(email_file)

            # Extract relevant information from the email headers
            subject = decode_email_header(email_message.get("Subject"))
            sender = decode_email_header(email_message.get("From"))
            receiver = decode_email_header(email_message.get("To"))
            date = email_message.get("Date")

            # Print the extracted information
            print("Subject:", subject)
            print("Sender:", sender)
            print("Receiver:", receiver)
            print("Date:", date)

            # Additional analysis or processing can be performed on other email headers as needed

    except FileNotFoundError:
        print("Email file not found.")
    except Exception as e:
        print("Error occurred while analyzing email headers:", str(e))

# Usage example
email_file_path = "/path/to/email.eml"  # Replace with the path to the email file
analyze_email_headers(email_file_path)
