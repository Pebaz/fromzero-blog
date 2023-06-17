import sys
import jinja2
import markdown
from markdown.extensions.fenced_code import FencedCodeExtension
from pathlib import Path

file = Path(sys.argv[1]) if len(sys.argv) == 2 else sys.exit(
    print('Usage: main.py <template>')
)

md_to_html = markdown.markdown(
    file.read_text(),
    extensions=[FencedCodeExtension()]
)

environment = jinja2.Environment()
template = environment.from_string(open('template.j2').read())
j2_html = template.render(html_body=md_to_html)

with open(f'{file.stem}.html', 'w') as html_file:
    html_file.write(j2_html)
