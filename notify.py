import json
import os
import urllib.request

api_key = os.environ.get("RESEND_API_KEY")
recipient = os.environ.get("NOTIFY_EMAIL")
if not api_key:
    raise SystemExit("Missing RESEND_API_KEY repository secret.")
if not recipient:
    raise SystemExit("Missing NOTIFY_EMAIL.")

payload = {
    "from": "Ceramics Class Monitor <onboarding@resend.dev>",
    "to": [recipient],
    "subject": "Spring 2027 ceramics classes are posted",
    "text": (
        "Spring 2027 appears on the Evanston Art Center ceramics page.\n\n"
        "You can view the classes here:\n"
        "https://www.evanstonartcenter.org/school/dept/adult-classes-department/ceramics\n\n"
        "This is the one-time alert from your ceramics class monitor."
    ),
}
request = urllib.request.Request(
    "https://api.resend.com/emails",
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    },
    method="POST",
)
with urllib.request.urlopen(request, timeout=30) as response:
    print("Email sent. Resend response:", response.read().decode("utf-8", errors="replace"))
