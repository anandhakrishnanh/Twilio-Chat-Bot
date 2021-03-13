# Twilio-Chat-Bot
This repository is for sending a daily message _( right now it's a daily quote )_ to any number with whatever text. I am using Twilio's API for this.

## How to run

1. First I woudld suggest reading [this article](https://betterprogramming.pub/i-wrote-a-script-to-whatsapp-my-parents-every-morning-in-just-20-lines-of-python-code-5d203c3b36c1) which inspired me to make this in the first place.
2. As mentioned in the aritcle change the whatsapp_messaging.py with your credentials and whatever is that you need to send. 
3. Setup your AWS account
4. Setup your Lamda function and upload your zipped copy of the folder called aws_deploy_package
5. Specify the function that you want to run 

## Troubleshooting

1. Sometimes your functions will not work properly so you might need to run `pip3 install -t ./ twilio datetime boto3` 
which will install libraries in the same folder

## To-Do ( Maybe ;) 

1. Add scripts send the text to more than one person 
2. Add a ICBM button to spam the person XD
3. Right now I am using the Twilio Sandbox only works for 3 days. 

## Common Commands 
These are just common commands that help me ;)

1. `chmod -R 755 .`
2. `pip3 install -t ./ twilio datetime boto3`
3. `zip -r ../package_name.zip .`
