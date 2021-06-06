# Kaltura

## **Description:**
An application that goes to Ynet RSS notifications site - where the latest news alerts are - via an HTTP request and downloads it in XML format and then converts to an Excel(csv format) spreadsheet and then pulls the data from Excel into HTML and builds/styles the table using CSS and JINJA2.

## **Requirements:**
- Jdk:    
`sudo apt install default-jdk`
- Docker:     
`sudo apt install docker.io`
- Jenkins:     
    ```
    wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
    sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > \
        /etc/apt/sources.list.d/jenkins.list'
    sudo apt-get update
    sudo apt-get install jenkins
    ```

### **Install plugins in Jenkins**
1. Docker Plugin
2. Docker Pipeline
3. Slack Notification Plugin

## **How to run the project:**

### **First: create new job in Jenkins:**
1. Create new job, choose: Pipeline
2. Job configurations: go to the project repo and check the file "Jenkins configurations" or click on the following link:
  https://github.com/AtrashAyoub/Kaltura/blob/9376f23f71847965ba3c8f059e834a1ea788fcae/Jenkins%20job%20configurations.pdf
3. Connect to the Jenkins server and enter the following commands in terminal:
  - `sudo -s`
  - `sudo chmod 666 /var/run/docker.sock`
4. Build the project.. when it's done you will recieve notification on your slack channel:
![Slack](https://user-images.githubusercontent.com/82280550/120929988-00a40080-c6f4-11eb-8c9a-9c02353638fe.jpg)

5. When the building is completed successfully, you can see that the docker image has been pushed into your docker-hub account repo:
![Screenshot 2021-06-06 182412](https://user-images.githubusercontent.com/82280550/120930169-e74f8400-c6f4-11eb-8ae8-6e3bd97dd19f.jpg)

6. To view the notifications table you can open any browser and enter the following url: localhost:port    
for example: `http://127.0.0.1:5000/`    
![Screenshot 2021-06-06 182233](https://user-images.githubusercontent.com/82280550/120930029-334df900-c6f4-11eb-9c91-834d047f50a6.jpg)     



### **Video_Example:** https://drive.google.com/file/d/1S4I9NcR2P3StQVogiMeC9qrdKS56U-fQ/view?usp=sharing






