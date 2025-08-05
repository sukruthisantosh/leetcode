from datetime import datetime

def convert_to_24_hour(time_str):
    # Convert the AM/PM time to 24-hour format
    time_obj = datetime.strptime(time_str, "%I:%M %p")
    return time_obj.strftime("%H:%M")

# Example usage:
time_am = "6:45 AM"
time_pm = "8:30 PM"

print(f"{time_am} → {convert_to_24_hour(time_am)}")
print(f"{time_pm} → {convert_to_24_hour(time_pm)}")
