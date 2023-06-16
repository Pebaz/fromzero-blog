import sys, json, jinja2, markdown
from pathlib import Path
from markdown.extensions.fenced_code import FencedCodeExtension

# file = Path(sys.argv[1]) if len(sys.argv) == 2 else sys.exit(
#     print('Usage: main.py <template>')
# )

# md_to_html = markdown.markdown(
#     file.read_text(),
#     extensions=[FencedCodeExtension()]
# )

# environment = jinja2.Environment()
# template = environment.from_string(open('template.j2').read())
# j2_html = template.render(html_body=md_to_html)

# with open(f'{file.stem}.html', 'w') as html_file:
#     html_file.write(j2_html)

environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader("blog/templates/")
)
template = environment.from_string(open('blog/templates/post.j2').read())

blog_root = Path('blog')

for post_dir in (blog_root / 'posts').iterdir():
    print(post_dir)
    properties = json.load((post_dir / 'properties.json').open())
    print('    ', properties)
    j2_html = template.render(body='hi', **properties)
    print('    ', repr(j2_html))

    with (Path('docs') / post_dir.name).with_suffix('.html').open('w') as file:
        file.write(j2_html)
