# Kaltura

## **Description:**
An application that goes to Ynet RSS notifications site - where the latest news alerts are - via an HTTP request and downloads it in XML format and then converts to an Excel(csv format) spreadsheet and then pulls the data from Excel into HTML and builds/styles the table using CSS and JINJA2.

## **Requirements:**
- Jdk: 
```sudo apt install default-jdk```
- Docker:
`sudo apt install docker.io`
- Jenkins: 
`wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > \
    /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update
sudo apt-get install jenkins`

### **Install plugins in Jenkins**
1. Docker Plugin
2. Docker Pipeline
3. Slack Notification Plugin
