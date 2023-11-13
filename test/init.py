import re

def regexGroup(pattern, target, group=1):
    """ Given a pattern and a string, return capturing group 1 by default
    """
    m = re.search(pattern, target)
    print(m)

    if m:
        return m.group(group)

print(regexGroup(r'chapter-(\d+)', "https://komiku.id/ch/all-hail-the-sect-leader-chapter-204/"))
print(regexGroup(r'(\d+)-(\d+)', " https://img.komiku.id/uploads2/2655177-1.png", 2))
print(regexGroup(r'(\d+)-(\d+)', " https://img.komiku.id/uploads2/2655177-123.jpg", 2))
