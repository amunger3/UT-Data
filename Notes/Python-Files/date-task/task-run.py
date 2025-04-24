import datetime

now = datetime.datetime.now()
timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")

try:
    with open("date_time_log.txt", "a") as file:
        file.write(timestamp_str + "\n")
    print(f"Successfully wrote '{timestamp_str}' to 'date_time_log.txt'")
except Exception as e:
    print(f"An error occurred: {e}")