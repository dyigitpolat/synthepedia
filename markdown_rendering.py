import markdown
import json
import base64

class Json2MarkdownHTML:
    def str_to_base64(self, string):
        return base64.b64encode(string.encode('utf-8')).decode('utf-8')
    
    def get_html(self, json_text):
        dict = json.loads(json_text)
        markdown_source = ''

        markdown_source += """# {}  \n""".format(dict['title'])
        markdown_source += """{}    \n""".format(dict['introduction'])

        introduction = self.str_to_base64(dict['introduction'])
        topic = self.str_to_base64(dict['title'])

        for item in dict['aspects']:
            subtopic = self.str_to_base64(item['aspect'])
            description = self.str_to_base64(item['description'])

            markdown_source += f"""
## [{item['aspect']}](/search/?topic={topic}&subtopic={subtopic}&description={description}&introduction={introduction})
{item['description']}    
"""
        return markdown.markdown(markdown_source)