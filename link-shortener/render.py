import json
import os
import textwrap

CWD = os.path.join(os.path.dirname(__file__))
JSON_DATA = os.path.join(CWD, 'links.json')
LINKS_DIR = os.path.join(CWD, '..', 'docs', 'l')


def main():
    with open(JSON_DATA, 'r') as link_data_file:
        json_data = json.load(link_data_file)

    for link_filename, link_data in json_data.items():
        target_filepath = os.path.join(LINKS_DIR, link_filename)
        with open(target_filepath, 'w') as target_file:
            target_file.write(
                textwrap.dedent(
                    f"""\
                    <html>
                    <meta http-equiv="Refresh"
                          content="0; url={link_data['link']}" />
                    </html>
                    """))

    index_filepath = os.path.join(LINKS_DIR, 'index.html')
    with open(index_filepath, 'w') as index:
        index.write("<html>\n")
        index.write("<h1>Links related to EP-RSN</h1>\n")
        index.write("<ul>\n")
        for link_filename, link_data in json_data.items():
            index.write(
                f'<li><a href="{link_data['link']}">'
                f'{link_data['title']}</a></li>\n')
        index.write("</ul>\n")
        index.write("</html>\n")




if __name__ == '__main__':
    main()
