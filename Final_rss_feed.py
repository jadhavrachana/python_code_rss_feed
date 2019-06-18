#!/usr/bin/env python
# coding: utf-8

# In[25]:


from dateutil.parser import parse
from datetime import date
import feedparser
import pandas as pd
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
from tabulate import tabulate

d = feedparser.parse('https://aws.amazon.com/about-aws/whats-new/recent/feed/')
d1 = feedparser.parse('https://azurecomcdn.azureedge.net/en-in/updates/feed/')
d2 = feedparser.parse('https://cloudblog.withgoogle.com/rss/')
link1=[]
link1.append(d)
link1.append(d1)
link1.append(d2)

for a in link1:
    title=[]
    link=[]
    published=[]
    datas={}
    for data in a.entries:
        if (date.today() - parse(data.published).date()).days < 7:
            title.append(data.title)
            link.append(data.link)
            published.append(data.published)
    datas["titles"]=title
    datas["links"]=link
    datas["published"]=published
    df=pd.DataFrame(datas)
    data=df
    fromaddr = "rachananjadhav@gmail.com"
    toaddr = "jadhavrachana123@gmail.com"
    text = """
    Hello Everyone,

    Here is your data:

    {table}

    Regards,

    Me"""

    html = """
    <html><body><p>Hello Everyone,</p>
    <p>The latest seven days updations in AWS ,Azure and GCP are:</p>
    {table}
    <p>Regards,</p>
    <p>Rachana Jadhav</p>
    <p>8408998688</p>
    </body></html>
    """
    text = text.format(table=tabulate(data, headers="firstrow", tablefmt="grid"))
    html = html.format(table=tabulate(data, headers="firstrow", tablefmt="html"))
    msg = MIMEMultipart("alternative", None, [MIMEText(text), MIMEText(html,'html')])
    # storing the senders emaiddl address 
    msg['From'] = fromaddr
    # storing the receivers email address
    msg['To'] = toaddr 
    # storing the subject
    msg['Subject'] = "Updated RSS Feed"
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
    s.quit()


# In[ ]:




