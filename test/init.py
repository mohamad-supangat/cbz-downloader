import re

def regexGroup(pattern, target, group=1):
    """ Given a pattern and a string, return capturing group 1 by default
    """
    m = re.search(pattern, target)
    print(m)

    if m:
        return m.group(group)

print(regexGroup(r'(\d+)\.(jpg|jpeg|png|gif|webp)$', "https://yuucdn.org/images/105/23/milf-hunting-in-another-world/00_001.png", 1))

# print(regexGroup(r'(\d+)-(\d+)', " https://img.komiku.id/uploads2/2655177-123.jpg", 2))
