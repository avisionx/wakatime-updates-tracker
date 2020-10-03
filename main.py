import os
import re
import json
import imaplib
import email

from dotenv import load_dotenv
from email.header import decode_header

# load .env files
load_dotenv()

# enable allow less secure app settings in gmail for this to work
# account credentials
username = os.getenv("EMAIL_ID")
password = os.getenv("EMAIL_PASSWORD")

# create an IMAP4 class with SSL
imap = imaplib.IMAP4_SSL("imap.gmail.com")

# authenticate
imap.login(username, password)

status, messages = imap.select("INBOX")

# total number of emails
messages = int(messages[0])

messageList = []

for i in range(messages, 0, -1):
    # fetch the email message by ID
    res, msg = imap.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            # parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])
            # decode the email subject
            subject = decode_header(msg["Subject"])[0][0]
            if isinstance(subject, bytes):
                # if it's a bytes, decode to str
                subject = subject.decode()

            msgString = ""

            if msg.is_multipart():
                # iterate over email parts
                for part in msg.walk():
                    # extract content type of email
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # get the email body
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        # add text/plain emails and skip attachments
                        msgString += body
            else:
                # extract content type of email
                content_type = msg.get_content_type()
                # get the email body
                body = msg.get_payload(decode=True).decode()
                if content_type == "text/plain":
                    # add only text email parts
                    msgString += body

            if content_type == "text/html":
                subjectSplit = subject.split(" ")
                datefrom = subjectSplit[-3]
                dateto = subjectSplit[-1]

            messageList.append({
                "data": msgString,
                "datefrom": datefrom,
                "dateto": dateto
            })

imap.close()
imap.logout()

monthReportList = []

for i in range(13):
    monthReportList.append([])

for i in range(len(messageList)):
    month = int(messageList[i]["dateto"].split("-")[1])
    messageList[i]["data"] = re.sub(r"\r", "", messageList[i]["data"])
    cleanedMsg = []
    for msg in messageList[i]["data"].split("\n"):
        if msg:
            cleanedMsg.append(msg)
    monthReportList[month].append(cleanedMsg[6:])

yearlyData = []

for month in range(1, 13):
    monthData = monthReportList[month]
    monthReport = {
        'totalTimeStr': "",
        'totalTime': {'hrs': 0,
                      'mins': 0},
        'totalMins': 0,
    }
    totalMins = 0
    for weekData in monthData:
        weekHrs = weekData[0]
        projects = []
        languages = []
        i = 0
        isProjects = False
        isLanguages = False
        projectsMap = {}
        languagesMap = {}
        for data in weekData:
            if(data == "Projects:"):
                isProjects = True
                isLanguages = False
                continue
            elif(data == "Languages:"):
                isLanguages = True
                isProjects = False
                continue
            elif(data == "Editors:"):
                isLanguages = False
                isProjects = False
                continue
            if(isProjects):
                projects.append(data)
            elif(isLanguages):
                languages.append(data)

        for project in projects:
            projSplit = project.split("*")
            timeProj = projSplit[2].split(" ")[1:]
            if(len(timeProj) > 2):
                timeProj = (int(timeProj[0]) * 60 + int(timeProj[2]))
            else:
                timeProj = int(timeProj[-2])
            try:
                projectsMap[projSplit[1]] += timeProj
            except:
                projectsMap[projSplit[1]] = timeProj

        for key in projectsMap.keys():
            projMins = projectsMap[key]
            tempObj = {
                'totalTimeStr': "",
                'totalTime': {'hrs': 0,
                              'mins': 0},
                'totalMins': 0,
            }
            tempObj['totalMins'] = projMins
            tempObj['totalTimeStr'] = "{hrs} hrs {mins} mins".format(
                hrs=projMins//60, mins=projMins % 60)
            tempObj['totalTime']['hrs'] = projMins//60
            tempObj['totalTime']['mins'] = projMins % 60
            projectsMap[key] = tempObj

        for language in languages:
            langSplit = language.split("*")
            timeLang = langSplit[2].split(" ")[1:]
            if(len(timeLang) > 2):
                timeLang = (int(timeLang[0]) * 60 + int(timeLang[2]))
            else:
                timeLang = int(timeLang[-2])
            try:
                languagesMap[langSplit[1]] += timeLang
            except:
                languagesMap[langSplit[1]] = timeLang

        for key in languagesMap.keys():
            langMins = languagesMap[key]
            tempObj = {
                'totalTimeStr': "",
                'totalTime': {'hrs': 0,
                              'mins': 0},
                'totalMins': 0,
            }
            tempObj['totalMins'] = langMins
            tempObj['totalTimeStr'] = "{hrs} hrs {mins} mins".format(
                hrs=langMins//60, mins=langMins % 60)
            tempObj['totalTime']['hrs'] = langMins//60
            tempObj['totalTime']['mins'] = langMins % 60
            languagesMap[key] = tempObj

        weekHrs = weekHrs.split(" ")
        totalMins += (int(weekHrs[0]) * 60 + int(weekHrs[2]))
        monthReport['totalMins'] = totalMins
        monthReport['totalTimeStr'] = "{hrs} hrs {mins} mins".format(
            hrs=totalMins//60, mins=totalMins % 60)
        monthReport['totalTime']['hrs'] = totalMins//60
        monthReport['totalTime']['mins'] = totalMins % 60
        monthReport['projects'] = projectsMap
        monthReport['languages'] = languagesMap
    yearlyData.append(monthReport)

with open('data.json', 'w') as outfile:
    json.dump(yearlyData, outfile)
