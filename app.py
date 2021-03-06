from flask import Flask
import markdown
import markdown.extensions.fenced_code
import markdown.extensions.codehilite
from pygments.formatters import HtmlFormatter


app = Flask(__name__)


def markdown_to_web(input_file):
    markdown_file = open(input_file, "r")
    md_template_string = markdown.markdown(
        markdown_file.read(), extensions=["fenced_code", "codehilite"]
    )

    formatter = HtmlFormatter(style="emacs", full=True, cssclass="codehilite")
    css_string = formatter.get_style_defs()
    md_css_string = f"<style>{css_string}</style>"

    return md_css_string + md_template_string


@app.route('/', methods=['GET'])
def index():
    return markdown_to_web("index.md")


@app.route('/concurrency', methods=['GET'])
def concurrency():
    return markdown_to_web("concurrency/overview.md")


@app.route('/hashing', methods=['GET'])
def hashing():
    return markdown_to_web("hashing/overview.md")


@app.route('/sorting', methods=['GET'])
def sorting():
    return markdown_to_web("sorting/overview.md")


@app.route('/linked-lists', methods=['GET'])
def linked_lists():
    return markdown_to_web("linked-lists/overview.md")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
