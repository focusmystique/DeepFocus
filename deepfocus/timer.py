import time

def countdown(minutes, label):
    total_seconds = minutes * 60
    print(f"\n🔹 {label} for {minutes} minute(s)")
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        print(f"\r⏳ {mins:02d}:{secs:02d}", end="")
        time.sleep(1)
        total_seconds -= 1
    print(f"\n✅ {label} finished!")
