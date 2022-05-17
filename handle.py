#Handler to display any errors and Audit Logs.
import config

name = input("Please login\n")
if name == (config.name):
    print ("Welcome " + config.name + ", " + config.ai + " is booting")
    exec(open("hector.py").read())
elif config.name not in name:
    print ("Sorry, You are not authorised!")
    


