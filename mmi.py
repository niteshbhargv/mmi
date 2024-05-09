import requests
import schedule
import time
import subprocess
from datetime import datetime

def poll_api():
    # Replace 'YOUR_API_ENDPOINT' with the actual API endpoint you want to poll
    f = open("demofile2.txt", "a")
    
    api_endpoint = 'https://api.tickertape.in/mmi/now'
    response = requests.get(api_endpoint)
    response_json = response.json()
    if response.status_code == 200:
        print('API polled successfully at', time.strftime('%Y-%m-%d %H:%M:%S'))
    current_value = response_json["data"]["currentValue"]
    print("current_value")
    print(current_value)
    f.write( datetime.today().strftime('%Y-%m-%d') + " : " + str(current_value) + "\n")
    applescript_code = 'display dialog "{}"'.format(current_value)
    subprocess.run(['osascript', '-e', applescript_code])
    f.close()

# Schedule the API polling task every day at 9 AM
schedule.every().day.at('09:00').do(poll_api)
#schedule.every(1).seconds.do(poll_api)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
