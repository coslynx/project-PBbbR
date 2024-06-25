import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(host, port, sender_email, receiver_email, subject, body):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP(host, port)
        server.starttls()
        server.login(sender_email, "your_password_here")
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def generate_email_body(group_id, room_number, room_members):
    body = f"Room Allocation Details:\nGroup ID: {group_id}\nRoom Number: {room_number}\nRoom Members:\n"
    for member in room_members:
        body += f"- {member}\n"
    return body

def send_room_allocation_email(host, port, sender_email, receiver_email, group_id, room_number, room_members):
    subject = "Room Allocation Information"
    body = generate_email_body(group_id, room_number, room_members)
    
    if send_email(host, port, sender_email, receiver_email, subject, body):
        print("Room allocation email sent successfully!")
    else:
        print("Failed to send room allocation email.")