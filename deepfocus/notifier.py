try:
    from plyer import notification
except ImportError:
    notification = None

def notify(title, message):
    if notification:
        notification.notify(
            title=title,
            message=message,
            timeout=5
        )
    else:
        print(f"\n🔔 {title}: {message}")
