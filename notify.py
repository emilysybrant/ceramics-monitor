import json
import os
import urllib.error
import urllib.request

api_key = os.environ.get("RESEND_API_KEY")
from_email = os.environ.get("RESEND_FROM_EMAIL", "").strip()
recipient = os.environ.get("NOTIFY_EMAIL")
second_recipient = os.environ.get("NOTIFY_EMAIL_2")
recipients = list(dict.fromkeys(address.strip() for address in (recipient, second_recipient) if address and address.strip()))
test_mode = os.environ.get("TEST_MODE", "").lower() == "true"

if not api_key:
    raise SystemExit("Missing RESEND_API_KEY repository secret.")
if not from_email:
    raise SystemExit("Missing RESEND_FROM_EMAIL repository secret.")
if not recipients:
    raise SystemExit("Missing NOTIFY_EMAIL.")

if test_mode:
    subject = "Test: your ceramics class monitor email is working"
    message = (
        "This is a test notification from your Evanston Art Center ceramics class monitor.\n\n"
        "If you received this email, the monitor can successfully send messages to this address. "
        "You do not need to take any action.\n\n"
        "The monitor will continue checking the ceramics page for Spring 2027 classes."
    )
else:
    subject = "Spring 2027 ceramics classes are posted"
    message = (
        "Spring 2027 appears on the Evanston Art Center ceramics page.\n\n"
        "You can view the classes here:\n"
        "https://www.evanstonartcenter.org/school/dept/adult-classes-department/ceramics\n\n"
        "This is the one-time alert from your ceramics class monitor."
    )

payload = {
    "from": from_email,
    "to": recipients,
    "subject": subject,
    "text": message,
}
request = urllib.request.Request(
    "https://api.resend.com/emails",
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "ceramics-class-monitor/1.0",
    },
    method="POST",
)
try:
    with urllib.request.urlopen(request, timeout=30) as response:
        print("Email sent. Resend response:", response.read().decode("utf-8", errors="replace"))
except urllib.error.HTTPError as error:
    details = error.read().decode("utf-8", errors="replace")
    raise SystemExit(f"Resend rejected the email (HTTP {error.code}): {details}")
