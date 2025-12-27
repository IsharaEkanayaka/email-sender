import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# --- CONFIGURATION ---
SMTP_SERVER = "smtp.gmail.com" # or smtp.office365.com
SMTP_PORT = 587
SENDER_EMAIL = "e20094@eng.pdn.ac.lk"
SENDER_PASSWORD = "ykwl fsqf asna epag" # NOT your normal login password

# Load the data
df = pd.read_csv("teams.csv")

# Connect to the server
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    print("Login Success")

    for index, row in df.iterrows():
        # Extract variables
        team_name = row['team_name']
        uni_name = row['university_name']
        recipient_email = row['team_lead_email']
        hr_user = row['hackerrank_username']
        hr_pass = row['hackerrank_pw']
        hr_email = row['hackerrank_email']

        subject = f"OFFICIAL: ICPC Sri Lanka Preliminary Round Credentials - {team_name}"

        # HTML Content
        html_body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; color: #333; line-height: 1.6;">
            <div style="max-width: 600px; margin: auto; border: 1px solid #ddd; padding: 20px; border-radius: 8px;">
                <h2 style="color: #0056b3; border-bottom: 2px solid #0056b3; padding-bottom: 10px;">
                    ICPC Sri Lanka National Contest
                </h2>
                <p><strong>Attention Team {team_name} ({uni_name}),</strong></p>
                
                <p>Welcome to the <strong>Online Preliminary Round</strong> of the ICPC Sri Lanka. 
                This round serves as the qualifier for the Onsite Regional at the University of Peradeniya.</p>
                
                <p>Below are your team's confidential access credentials for the contest platform:</p>
                
                <div style="background-color: #f9f9f9; padding: 15px; border-left: 4px solid #0056b3; margin: 20px 0;">
                    <p style="margin: 5px 0;"><strong>HackerRank Username:</strong> {hr_user}</p>
                    <p style="margin: 5px 0;"><strong>Password:</strong> {hr_pass}</p>
                    <p style="margin: 5px 0;"><strong>Registered Email:</strong> {hr_email}</p>
                </div>

                <p><strong>Instructions:</strong></p>
                <ol>
                    <li>Log in immediately to verify access.</li>
                    <li>Do <strong>not</strong> share these credentials outside your team.</li>
                    <li>Ensure your internet connection is stable 30 minutes prior to the start time.</li>
                </ol>

                <p style="font-size: 0.9em; color: #666;">
                    <em>Note: The top teams from this round will be invited to the Onsite Regional to compete for the chance 
                    to represent Sri Lanka at the ICPC Asia West Continent Finals and World Finals.</em>
                </p>

                <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
                <p style="font-size: 0.8em; color: #888;">
                    Organizing Committee<br>
                    ICPC Sri Lanka
                </p>
            </div>
        </body>
        </html>
        """

        msg = MIMEMultipart()
        msg['From'] = f"ICPC Sri Lanka <{SENDER_EMAIL}>" # Display Name
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(html_body, 'html'))

        server.send_message(msg)
        print(f"Sent to {team_name}")
        time.sleep(2) 

    print("All credentials dispatched.")

except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()