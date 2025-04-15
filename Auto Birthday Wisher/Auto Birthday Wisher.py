import pandas as pd
import datetime
import smtplib
import os


current_path = os.getcwd()
print (current_path)
# Change the path of the directory in which you are currently working
os.chdir(current_path)

# Provide email to which you want to send the wishes
GMAIL_ID = input("Enter your email: ")
GMAIL_PASSWORD = input("Enter password for email mentioned above: ")

def sendEmail(to, sub, msg):
    print(f"Email to {to} sent: \nSubject: {sub}, \nMessage: {msg}")
    # Creating server to send mail
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # Start a TLS session
    s.starttls()
    # The function will login with your Gmail credentials
    s.login(GMAIL_ID, GMAIL_PASSWORD)
    # Sending the mail
    s.sendmail(GMAIL_ID,to, f"Subject: {sub} \n\n {msg}")
    s.quit()

if __name__ == "__main__":
    # The datasheet where the data is stored
    df = pd.read_excel("data.xlsx")
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    
    writeInd = []
    for index, item in df.iterrows():
        bday = item["Birthday"]
        bday = datetime.datetime.strptime(bday, "%d-%m-%Y")
        bday = bday.strftime("%d-%m")
        if (today == bday) and yearNow not in str(item['LastWishedYear']):
            # Call the sendmail func
            sendEmail(item['Email'], "Happy Birthday", item['Dialogue'])
            writeInd.append(index)
            
            if writeInd != None:
                for i in writeInd:
                    oldYear = df.loc[i, 'LastWishedYear']
                    df.loc[i, 'LastWishedYear'] = str(oldYear)+ ", " + str(yearNow)
                    
                    df.to_excel('data.xlsx', index=False)