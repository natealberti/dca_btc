import smtplib
from email.message import EmailMessage

# formatting for popular phone carriers
carriers = {
    'att': '@mms.att.net',
    'tmobile': ' @tmomail.net',
    'verizon': '@vtext.com',
    'sprint': '@pm.sprint.com'
}

def send(message):
    # Replace the number with your own, or consider using an argument\dict for multiple people.
    to_number = '0000000000{}'.format(carriers['sprint'])
    # replace with the email sending the message
    from_email = [your-email]

    msg = EmailMessage()
    msg.set_content(message)
    msg['to'] = to_number
    msg['from'] = from_email
    # replace with the app-speific password
    password = [password]
    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_email, password)

    # Send text message through SMS gateway of destination number
    server.send_message(msg)

    server.quit