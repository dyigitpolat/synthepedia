json_format_prefix = """{ "title": \""""

main_prompt_template = """
provide the main aspects (or types) of "{}" using the following json format:
{{ "title": "concise topic max 5 words", "introduction": "informative introduction about the topic", "aspects": [{{"aspect": "aspect name here", "description": "a paragraph of very detailed and elaborate description here"}}, ...] }}


"""

subtopic_prompt_template = """
{3}
"{0} ({1})": {2}

provide the main aspects (or types) of "{0} ({1})" using the following json format:
{{ "title": "concise topic max 5 words", "introduction": "informative introduction about the topic", "aspects": [{{"aspect": "aspect name here", "description": "a paragraph of very detailed and elaborate description here"}}, ...] }}


"""