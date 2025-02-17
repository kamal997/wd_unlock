import win32com.client

def list_connected_devices():
    """
    This function lists all USB-connected devices.
    """
    try:
        # Get WMI object
        wmi = win32com.client.GetObject("winmgmts:")
        # Retrieve all PnP devices
        devices = wmi.InstancesOf("Win32_PnPEntity")
        usb_devices = []

        # Filter USB devices
        for device in devices:
            if "USB" in str(device.PNPClass):
                usb_devices.append(device)

        # Display connected USB devices
        if usb_devices:
            print("Connected USB Devices:")
            for i, device in enumerate(usb_devices, 1):
                print(f"{i}. Device Name: {device.Name} | Device ID: {device.DeviceID}")
        else:
            print("No USB devices connected.")
    except Exception as e:
        print(f"Error while listing connected devices: {e}")

# Call the function to list connected devices
list_connected_devices()