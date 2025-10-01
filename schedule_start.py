import schedule
import time
import subprocess
import socket

startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
startupinfo.wShowWindow = subprocess.SW_HIDE


def run_script():
    # Replace 'your_script.py' with the path to the script you want to run
    #subprocess.run("python main.py")
    #subprocess.run(["python", "main.py"])
    subprocess.Popen("python main.py", startupinfo=startupinfo)
    #subprocess.Popen(["python", "main.py"], startupinfo=startupinfo)

# Schedule the script to run at 7 AM
schedule.every().day.at("18:12").do(run_script)

# Schedule the script to stop at 6 PM
schedule.every().day.at("18:15").do(lambda: exit())


while True:
    schedule.run_pending()
    time.sleep(1)
