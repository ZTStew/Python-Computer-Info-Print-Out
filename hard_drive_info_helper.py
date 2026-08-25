def get_drive_types():
    system = platform.system()

    if system == "Windows":
        command = [
            "powershell",
            "-NoProfile",
            "-Command",
            "Get-PhysicalDisk | "
            "Select-Object FriendlyName, MediaType, BusType | "
            "ConvertTo-Csv -NoTypeInformation"
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        return result.stdout

    elif system == "Linux":
        result = subprocess.run(
            ["lsblk", "-d", "-o", "NAME,ROTA,TRAN,MODEL"],
            capture_output=True,
            text=True
        )

        return result.stdout

    elif system == "Darwin":  # macOS
        result = subprocess.run(
            ["diskutil", "list"],
            capture_output=True,
            text=True
        )

        return result.stdout

    else:
        return "Unsupported operating system"


print(get_drive_types())