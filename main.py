import time, subprocess
import win32com.client
import pyautogui

def try_password(password):
    # Here you can add the code to try unlocking the hard drive using the password
    # For this example, we assume the correct password is "12345"
    correct_password = "12345"
    return password == correct_password

def disconnect_usb():
    """
    This function disconnects the USB Mass Storage device.
    """
    try:
        wmi = win32com.client.GetObject("winmgmts:")
        devices = wmi.InstancesOf("Win32_PnPEntity")
        for device in devices:
            if "USB" in str(device.PNPClass):
                if "USB-Massenspeichergerät" in str(device.Name):
                    print(f"Checking device: {device.Name}")
                    print(" Waiting for device to disconnect... (5 seconds)...")
                    device.ExecMethod_("Disable")
    except Exception as e:
        print(f"Error while disconnecting device: {e}")

def reconnect_usb():
    """
    This function reconnects the USB Mass Storage device.
    """
    try:
        wmi = win32com.client.GetObject("winmgmts:")
        devices = wmi.InstancesOf("Win32_PnPEntity")
        for device in devices:
            if "USB" in str(device.PNPClass):
                if "USB-Massenspeichergerät" in str(device.Name):
                    print(f"Reconnecting device: {device.Name}")
                    print(" Waiting for device to reconnect... (5 seconds)...")
                    device.ExecMethod_("Enable")
    except Exception as e:
        print(f"Error while reconnecting device: {e}")

def run_wd_unlock():
    """
    This function runs the WD Drive Unlock executable.
    """
    try:
        # Path to the WD Drive Unlock executable
        wd_unlock_path = r"E:\WD Drive Unlock.exe"
        
        # Run the executable
        print("Running WD Drive Unlock...")
        subprocess.run(wd_unlock_path, shell=True)
    except Exception as e:
        print(f"Error while running WD Drive Unlock: {e}")

def brute_force():
    attempt_count = 0  # Counter for the number of attempts
    for i in range(100000):  # From 0 to 99999
        password_guess = str(i)  # Convert the number to a string without leading zeros
        print(f"Trying password: {password_guess}")
        attempt_count += 1

        if try_password(password_guess):
            print(f"Password found: {password_guess}")
            return password_guess

        # Every 5 attempts, disconnect and reconnect the USB device
        if attempt_count % 5 == 0:
            print("Disconnecting and reconnecting the device...")
            disconnect_usb()
            time.sleep(5) 
            reconnect_usb()
            time.sleep(5)
            run_wd_unlock()
            time.sleep(5)

            
            ##TODO:

            # # Move the mouse to position (100, 200) and click
            # pyautogui.click(x=100, y=200) # click ok to run WD Drive Unlock
            # time.sleep(2)
            # pyautogui.click(x=100, y=200) # click ok to write Password in WD Drive Unlock
            # time.sleep(2)
            

    print("Password not found.")
    return None

# Run the function
brute_force()


