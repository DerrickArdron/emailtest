# Test whether I can send a plain text email
# DA 191206

import smtplib
smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('dardron@buckspgl.org','J8unty*100')
smtpObj.sendmail('dardron@buckspgl.org','derrick.ardron@outlook.com','Subject:Test.\nBody goes here')
smtpObj.quit()
