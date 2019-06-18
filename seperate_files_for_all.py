#!/usr/bin/env python
# coding: utf-8

# In[100]:


from dateutil.parser import parse
from datetime import date
import feedparser
import pandas as pd
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
d = feedparser.parse('https://aws.amazon.com/about-aws/whats-new/recent/feed/')
title=[]
link=[]
published=[]
for data in d.entries:
    if (date.today() - parse(data.published).date()).days < 7:
        title.append(data.title)
        link.append(data.link)
        published.append(data.published)
datas={}
datas["titles"]=title
datas["links"]=link
datas["published"]=published
df=pd.DataFrame(datas)
df
df.to_csv(r'C:\Users\r.jadhav\Desktop\Rss_feed_file\aws.csv', index=False)

d1 = feedparser.parse('https://azurecomcdn.azureedge.net/en-in/updates/feed/')
title=[]
link=[]
published=[]
for data in d1.entries:
    if (date.today() - parse(data.published).date()).days < 7:
        title.append(data.title)
        link.append(data.link)
        published.append(data.published)
datas={}
datas["titles"]=title
datas["links"]=link
datas["published"]=published
df=pd.DataFrame(datas)
df.to_csv(r'C:\Users\r.jadhav\Desktop\Rss_feed_file\azure.csv', index=False)

d2 = feedparser.parse('https://cloudblog.withgoogle.com/rss/')
title=[]
link=[]
published=[]
for data in d2.entries:
    if (date.today() - parse(data.published).date()).days < 7:
        title.append(data.title)
        link.append(data.link)
        published.append(data.published)
datas={}
datas["titles"]=title
datas["links"]=link
datas["published"]=published
df=pd.DataFrame(datas)
df.to_csv(r'C:\Users\r.jadhav\Desktop\Rss_feed_file\gcp.csv', index=False)

fromaddr = "rachananjadhav@gmail.com"
toaddr = "r.jadhav@globant.com"
lpath = r'C:\Users\r.jadhav\Desktop\Rss_feed_file'
flist = ['aws.csv', 'azure.csv','gcp.csv']
# instance of MIMEMultipart 
msg = MIMEMultipart() 

# storing the senders email address 
msg['From'] = fromaddr 

# storing the receivers email address 
msg['To'] = toaddr 

# storing the subject 
msg['Subject'] = "Updated RSS Feed"

# string to store the body of the mail 
body = "This is updated rss feeds of aws azure and GCP"

# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 

for item in flist:
# open the file to be sent 
# instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 

# To change the payload into encoded form 
    p.set_payload(open(lpath + '\\' + item, "rb").read())

# encode into base64 
    encoders.encode_base64(p) 

    p.add_header('Content-Disposition','attachment; filename="%s"' % item)

# attach the instance 'p' to instance 'msg' 
    msg.attach(p) 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login(fromaddr, "Namita@19") 

# Converts the Multipart msg into a string 
text = msg.as_string() 

# sending the mail 
s.sendmail(fromaddr, toaddr, text) 

# terminating the session 
s.quit() 


# In[ ]:




