import requests # Allows function to send a http get request to url

def IsSslVaild(url):

    response = " " # Defining variable to access outside try scope 

    try: # defining try scope to ignore sslerror output error

    # Making a get request to the argument of a specified url
        response = requests.get(url)
    
    except requests.ConnectionError: # Ignore connection error
        pass # pass response variable 

    # apply variable to str
    value = str((response))

    # if value is 200 meaning the request was sucesfull and therfoure there is a valid SSL/TLS certitfcate.
    if value == "<Response [200]>":
        return "Clear"
    else:
        return "Invalid"

  
# Invalid
#response = requests.get("https://expired.badssl.com/")                                                               # Invalid 1
#response = requests.get("https://wrong.host.badssl.com/")                                                            # Invalid 2
#response = requests.get("https://self-signed.badssl.com/")                                                           # Invalid 3
#response = requests.get("https://untrusted.badssl.com/")                                                             # Invalid 4
#response = requests.get("https://revoked.badssl.com/")                                                               # Invalid 5
#response = requests.get("https://pinning-test.badssl.com/")                                                          # Invalid 6

# Valid
#response = requests.get("https://learn.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010")        # Valid 1
#response = requests.get("https://learn.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010")        # Valid 2
#response = requests.get("https://attack.mitre.org/")                                                                 # Valid 3
#response = requests.get("https://www.virustotal.com/gui/home/upload")                                                # Valid 4
#response = requests.get("https://tryhackme.com/")                                                                    # Valid 5
#response = requests.get("https://osintframework.com/")                                                               # Valid 6

