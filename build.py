"""
! IMPORTANT: The `docs/` folder is auto-generated except for the CNAME file.
"""

import json, jinja2, markdown, datetime
from pathlib import Path
from markdown.extensions.fenced_code import FencedCodeExtension
# from md_mermaid import MermaidExtension
from feedgen.feed import FeedGenerator


# file = Path(sys.argv[1]) if len(sys.argv) == 2 else sys.exit(
#     print('Usage: main.py <template>')
# )

# environment = jinja2.Environment()
# template = environment.from_string(open('template.j2').read())
# j2_html = template.render(html_body=md_to_html)

# with open(f'{file.stem}.html', 'w') as html_file:
#     html_file.write(j2_html)

environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader("blog/templates/")
)

blog_root = Path('blog')

# Create RSS feed generator
fg = FeedGenerator()
fg.title('From Zero Systems Blog')
fg.subtitle('Built From Zero')
fg.link(href='https://blog.fromzero.systems', rel='self')
fg.language('en')
# TODO(pbz): fg.id('http://lernfunk.de/media/654321')
# TODO(pbz): fg.author( {'name':'Pebaz','email':'john@example.de'} )
# TODO(pbz): fg.logo('http://ex.com/logo.jpg')
# TODO(pbz): fg.link( href='http://larskiesow.de/test.rss', rel='self')

post_j2 = environment.get_template('post.j2')
posts = {}

for post_dir in (blog_root / 'posts').iterdir():
    # Generate post HTML
    properties = json.load((post_dir / 'properties.json').open())
    post_body = markdown.markdown(
        (post_dir / 'post.md').read_text(),
        extensions=[
            FencedCodeExtension(),
            # MermaidExtension()
        ]
    )
    post_html = post_j2.render(body=post_body, **properties)
    (Path('docs/posts') / post_dir.name).with_suffix('.html').write_text(post_html)

    posts[post_dir.name] = properties

    # Add post to RSS feed
    fe = fg.add_entry()
    fe.title(properties['title'])
    PACIFIC_TIME = datetime.timedelta(hours=-7)
    date_only = datetime.datetime.strptime(properties['date'], "%Y-%m-%d")
    post_date = date_only.replace(tzinfo=datetime.timezone.utc) + PACIFIC_TIME
    fe.pubDate(post_date)
    fe.link(href="https://blog.fromzero.systems")
    # TODO(pbz): fe.id('http://lernfunk.de/media/654321/1')

# Write out RSS feed
fg.rss_file('docs/static/rss.xml', pretty=True)

for page in (blog_root / 'pages').iterdir():
    if page.is_dir():
        continue
    page_j2 = environment.from_string(page.read_text())
    page_html = page_j2.render(posts=posts)
    (Path('docs/pages') / page.name).with_suffix('.html').write_text(page_html)

# Write out index.html
# index_j2 = environment.get_template('index.j2')
# index_html = index_j2.render(posts=posts)
# (Path('docs/pages') / 'index.html').write_text(index_html)
