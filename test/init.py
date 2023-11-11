import re

pattern = "https://%s/manga/([^/]+)" % "komiku.id"
target = "https://komiku.id/manga/all-hail-the-sect-leader/"
m = re.match(pattern, target)
name = None
if m:
    name = m.group(1)
    print(name)


print(re.match("/ch/%s-chapter-[0-9.]+" % name, "/ch/all-hail-the-sect-leader-chapter-285/"))


