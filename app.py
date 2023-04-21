from openai_client import OpenAIClient
from prompts import *
from markdown_rendering import Json2MarkdownHTML

from flask import Flask, request, render_template
import base64

app = Flask(__name__, static_folder='static')

def base64_to_str(base64_string):
    return base64.b64decode(base64_string).decode('utf-8')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']
        client = OpenAIClient()
        response = client.respond(main_prompt_template.format(text) + json_format_prefix)
        response = json_format_prefix + response
        print(response)
        return render_template('result.html', content=Json2MarkdownHTML().get_html(response))
    return render_template('home.html')

@app.route('/search/', methods=['GET'])
def search():
    if request.method == 'GET':
        topic = base64_to_str(request.args.get('topic'))
        subtopic = base64_to_str(request.args.get('subtopic'))
        description = base64_to_str(request.args.get('description'))
        introduction = base64_to_str(request.args.get('introduction'))

        client = OpenAIClient()
        response = client.respond(subtopic_prompt_template.format(subtopic, topic, description, introduction) + json_format_prefix)
        response = json_format_prefix + response
        print(response)
        return render_template('result.html', content=Json2MarkdownHTML().get_html(response))

if __name__ == '__main__':
    app.run(debug=True)