import time
import colorama

# Initialize colorama
colorama.init()

def getAMPM(hh: int, mm: int, ss: int) -> str:
    """Returns 'AM' or 'PM' based on the hour"""
    return "AM" if hh < 12 else "PM"

def display_time12():
    while True:
        # Get the current time
        currentTime = time.localtime()
        hh, mm, ss = currentTime.tm_hour, currentTime.tm_min, currentTime.tm_sec

        # Format the time
        formattedTime = f"{hh-12 if hh > 12 else hh:02d}:{mm:02d}:{ss:02d}"

        # Change color based on AM/PM
        ampm = getAMPM(hh, mm, ss)
        color = colorama.Fore.CYAN+colorama.Back.BLACK if ampm == "AM" else colorama.Fore.CYAN+colorama.Back.BLACK

        # Print the time
        print(f"{colorama.Fore.WHITE+colorama.Back.BLACK}Time: {color}{formattedTime} {ampm}{colorama.Style.RESET_ALL}", end="\r")

        # Sleep for 1 second
        time.sleep(1)
        
def display_time24():
    while True:
        # Get the current time
        currentTime = time.localtime()
        hh, mm, ss = currentTime.tm_hour, currentTime.tm_min, currentTime.tm_sec

        # Format the time
        formattedTime = f"{hh:02d}:{mm:02d}:{ss:02d}"

        color = colorama.Fore.CYAN+colorama.Back.BLACK

        # Print the time
        print("\r",end="")
        time.sleep(1)
        print(f"{colorama.Fore.WHITE+colorama.Back.BLACK}Time: {color}{formattedTime}{colorama.Style.RESET_ALL}", end="")

        # Sleep for 1 second



def ask():
    while True:
        format=input("\n12hr format or 24hr format,just type 12 or 24 based on your preferred format [or try 36]: ")
        if format.strip()=="12":
            display_time12()
        elif format.strip()=="24":
            display_time24()
        elif format.strip()=="36":
            print(f"\ngot you!!\n")
            exit()
        else:
            print("Invalid value sensed,try again.\n")
            continue

ask()
