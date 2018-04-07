from smtplib import SMTP
host="smtp.gmail.com"
port="587"
username="prasanthmaverick@gmail.com"
password="printf(\"123\");"
conn=SMTP(host,port)
conn.ehlo()
conn.starttls()
conn.login(username,password)
subject="hello message"
body="hello! Sent from python"
message="Subject:{}\n\n{}".format(subject,body)
conn.sendmail(username,username,message)
