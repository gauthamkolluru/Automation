import os
import json
import glob

OFFICIAL = ['cisco', 'salesforce', 'sso', 'smartsheet',
            'journeys', 'automation', 'dsx', 'rtb']

# [constraint for constraint in OFFICIAL if constraint in word.lower()]


def read_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as fp:
            return json.load(fp)
    else:
        return {'cisco': [], 'personal': []}


def write_json(dict_data, file_path):
    with open(file_path, 'w') as fp:
        return json.dump(dict_data, fp)


def extract_links(root, links_file):
    file_path = os.path.join(root, links_file)
    links_dict = read_json(file_path)
    for item in glob.glob(os.path.join(root, '*.md')):
        with open(os.path.join(root, item), 'r') as fp:
            content_list = fp.read()
        if 'http' in content_list:
            for word in [word for word in content_list.split() if 'http' in word]:
                if word not in links_dict['cisco'] + links_dict['personal']:
                    # if 'cisco' in word.lower() or 'smartsheet' in word.lower() or 'salesforce' in word.lower():
                    if any([constraint for constraint in OFFICIAL if constraint in word.lower()]):
                        links_dict['cisco'].append(word)
                    else:
                        links_dict['personal'].append(word)
    return write_json(links_dict, file_path)


if __name__ == '__main__':
    root = os.path.expanduser('~\\Documents\\task_keeper')
    links_file = 'links_list.json'
    extract_links(root, links_file)
