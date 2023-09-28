#!/bin/bash
function getIP {
   (Get-NetIPAddress | Where-Object AddressFamily -eq 'IPv4').IPAddress
}

 # Get IP, User, PowerShell Version, Hostname, and Date
$IP = getIP
$User = $env:UserName
$Ver = $PSVersionTable.PSVersion.ToString()
$Hostname = $env:ComputerName
$DATE = Get-Date -Format "dddd, MMMM d, yyyy"
# Define the email body
$BODY = "This machine's IP is $IP. User is $User. Hostname is $Hostname. PowerShell Version $Ver. Today's Date is $DATE."

# Send the email using Gmail SMTP server
$SMTPServer = "smtp.gmail.com"
$SMTPPort = 587
$SMTPUsername = "marshalltahj@gmail.com"
$SMTPPassword = "vnnj qtxr mgbz mijn"
# Create a credential object
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $SMTPUsername, (ConvertTo-SecureString -String $SMTPPassword -AsPlainText -Force)

# Send the email
Send-MailMessage -To "botheaj@ucmail.uc.edu" -From "marshalltahj@gmail.com" -Subject "IT3038c Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)
