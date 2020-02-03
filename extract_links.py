import os

root = os.path.expanduser('~\Documents\\task_keeper')

links_file = 'links_list.md'

for item in os.listdir(root):
    if item.split('.')[-1] == 'md':
        with open(os.path.join(root,item), 'r') as fp:
            content_list = fp.read()
        if 'http' in content_list:
            for word in content_list.split():
                if 'http' in word:
                    if os.path.exists(os.path.join(root, links_file)):
                        fp = open(os.path.join(root,links_file), 'r+')
                        if word not in fp.read().split('\n'):
                            fp.write(word+'\n\n')
                    else:
                        fp = open(os.path.join(root,links_file), 'w')
                        fp.write(word+'\n\n')
                    fp.close()
