import base64
from azure.communication.email import EmailClient
import os
import logging

file_path = f'/tmp/output.xlsx'
email_client = EmailClient.from_connection_string("endpoint=https://communicationserviceaih.unitedstates.communication.azure.com/......")
if os.path.getsize(file_path) > 0:
    """
    Check if the file at the specified path is not empty.
    
    If the file is not empty, read the file in binary mode, encode its content to base64,
    and prepare an email message with the encoded file as an attachment. Send the email
    using the Azure Communication Services EmailClient.

    :raises FileNotFoundError: If the file does not exist.
    :raises IOError: If there is an error reading the file.
    """
    
    with open(file_path, "rb") as file:
        file_bytes_b64 = base64.b64encode(file.read())
    
    message = {
        "content": {
            "subject": "Important Alert",
            "plainText": "This is an important message from MidellwareAlert. Please review the details.",
            "html": "<html><h1>Important Alert</h1><p>This is an important message from MidellwareAlert. Please review the details.</p></html>"
        },
        "recipients": {
            "to": [
                {
                    "address": sheets['email']
                }
            ]
        },
        "senderAddress": "MidellwareAlert@bb7d0f8d-f8fa-4f2a-adc7-bf10e1916d2a.azurecomm.net",
        "attachments": [
            {
                "name": "Name.xlsx",
                "contentType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                "contentInBase64": file_bytes_b64.decode()
            }
        ]
    }

    poller = email_client.begin_send(message)
    result = poller.result()
    logging.info(f"Result: {result}")
else:
    """
    Log a message indicating that the file is empty and the email will not be sent.
    
    This block is executed if the file at the specified path is empty.
    """
    logging.info("Skipping email sending because the file is empty.")
