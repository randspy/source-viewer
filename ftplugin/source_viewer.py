import os
import re

def extract_pattern(content, pattern):
    regex = re.compile(pattern)
    search_match = regex.search(content)

    if search_match:
        return content[search_match.start():search_match.end()]
    else:
        return ""


def extract_file_name(line):
    content = extract_pattern(line, '<.+#\d+>')
    content = extract_pattern(content, '.+#')

    return content[1:-1]


def extract_line_number(line):
    content = extract_pattern(line, '<.+#\d+>')
    content = extract_pattern(content, '#\d+')[1:]

    if content:
        return int(content)
    else:
        return 0


def source_signature(current_line, path):

    if len(path) == 0 or len(current_line) == 0:
        return '', 0

    file_path = ""
    for root, subFolders, files in os.walk(path):
        file_name = extract_file_name(current_line)
        if file_name in files:
            file_path = os.path.join(root,file_name)

    return file_path, extract_line_number(current_line)
