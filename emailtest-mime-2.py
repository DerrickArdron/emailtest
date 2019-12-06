import email,smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "dardron@buckspgl.org"
receiver_email = "derrick.ardron@outlook.com"
#password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = 'dardron@buckspgl.org'
message["To"] = 'derrick.ardron@outlook.com'

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a>
       has many great tutorials.
    </p>
  </body>
</html>"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

filename = "Bucks PGL Survey v04.pdf"  # In same directory as script
print(filename)
# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    print(attachment)
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part3 = MIMEBase("application", "octet-stream")
    part3.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part3)

# Add header as key/value pair to attachment part
part3.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)
# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)
message.attach(part3)
#print(message.as_string())
# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP('smtp-mail.outlook.com', 587) as server:
    server.ehlo()
    server.starttls()
    server.login('dardron@buckspgl.org','J8unty*100')
    server.sendmail('dardron@buckspgl.org','derrick.ardron@outlook.com', message.as_string())
#server.quit()
