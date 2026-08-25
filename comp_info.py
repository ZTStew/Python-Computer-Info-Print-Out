import psutil, platform, cpuinfo, subprocess



computer_info = {}

# os_info = {
#     "system": platform.system(),
#     "release": platform.release(),
#     "version": platform.version(),
#     "architecture": platform.machine(),
#     "processor": platform.processor(),
#     "hostname": platform.node()
# }
# print(os_info)

# Gets computer OS infr
computer_info["OS"] = str(platform.system()) + " " + str(platform.release())
computer_info["Processor_Name"] = platform.processor()
computer_info["Processor"] = cpuinfo.get_cpu_info()["brand_raw"]
# Gets the total amount of RAM in a computer
computer_info["RAM"] = f"{psutil.virtual_memory().total / (1024**3):.2f} GB"
computer_info["Cores"] = psutil.cpu_count(logical=False)

print(computer_info)


# print("Processor:", platform.processor())
# print("CPU Cores:", psutil.cpu_count(logical=False))
# print("Logical CPUs:", psutil.cpu_count(logical=True))
# print("CPU Frequency:", psutil.cpu_freq())
# info = cpuinfo.get_cpu_info()

# # print(info)
# print(info["brand_raw"])





