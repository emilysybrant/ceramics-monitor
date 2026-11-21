import os
import re
import urllib.request

URL = "https://www.evanstonartcenter.org/school/dept/adult-classes-department/ceramics"

request = urllib.request.Request(
    URL,
    headers={"User-Agent": "Mozilla/5.0 (compatible; CeramicsClassMonitor/1.0)"},
)
with urllib.request.urlopen(request, timeout=30) as response:
    html = response.read().decode("utf-8", errors="replace")

# Remove markup and normalize whitespace before looking for the season label.
text = re.sub(r"<script\\b[^>]*>.*?</script>|<style\\b[^>]*>.*?</style>", " ", html, flags=re.I | re.S)
text = re.sub(r"<[^>]+>", " ", text)
text = re.sub(r"&nbsp;|&#160;", " ", text, flags=re.I)
text = re.sub(r"\\s+", " ", text)
found = bool(re.search(r"\\bSpring\\s+2027\\b", text, flags=re.I))

with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as output:
    output.write(f"spring_2027_found={'true' if found else 'false'}\\n")

print("Spring 2027 ceramics classes detected." if found else "No Spring 2027 ceramics classes found yet.")
