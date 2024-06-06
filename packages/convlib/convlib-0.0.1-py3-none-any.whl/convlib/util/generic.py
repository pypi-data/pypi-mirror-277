import re    

_url = r'(http[^\s]*)'

wikilink_regex     = re.compile(r'\[\[([^\]`]*?)(#[^\]]*?)?(?:\|([^\]]*?))?\]\]')
reflink_regex      = re.compile(rf'\[(\w*)\]: {_url} ?(?:\(([^\)]*)\))?(?:"([^"]*)")?')
footnote_regex     = re.compile(r'\[\^(\w*)\]: (.+)')
bookmark_regex     = re.compile(r'\[([a-zA-Z]{1,2})\]: (http[^\s]*) ?(?:\(([^\)]*)\))?(?:"([^"]*)")?')
heading_regex      = re.compile(r'(#{1,6}) (.*)')
data_regex         = re.compile(r'# Data\s+```yaml\s([\s\S]*?)\s+```')
yaml_regex         = re.compile(r'---\n(.*?)\n(---|\.\.\.)', flags=re.DOTALL)
external_url_regex = re.compile(_url)

