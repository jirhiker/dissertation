p='/Users/ross/Programming/git/dissertation/src/config.yaml'

import yaml
import os
with open(p, 'r') as fp:
    cfg = yaml.load(fp)
    

#print cfg['body']['chapters']

#for c in cfg['body']['chapters']:
#    print c
def make_section(tag, name, root):
    body = ''
#     if '|' in name:
#         name, p = name.split('|')
#         #convert_doc(root, p)
# #         docp = os.path.join(root, '{}.doc'.format(p))
# #         if os.path.isfile(docp):
# #             subprocess.call(['textutil', '-convert', 'txt', docp])
# 
#         with open(os.path.join(root, '{}.txt'.format(p)), 'r') as fp:
#             body = fp.read()
    body=''
    txt = '\{}{{{}}}\n{}'.format(tag, name, body)
    return txt
    
root=''
for chapter in cfg['body']['chapters']:
    root=os.path.join(root, chapter['root'])
    btxt=make_section('chapter', chapter['title'], root)
    sec=None
    if chapter.has_key('sections'):
        sec=chapter['sections']

    print sec
    if sec:
        for section in sec:
            btxt+=make_section('section', section['title'], root)
            subsec=None
            if section.has_key('subsections'):
                subsec=section['subsections']
            
            print subsec
            if subsec:
                for subsection in subsec:
                    btxt+=make_section('subsection', subsection['title'], root)
                    subsubsec=None
                    if subsection.has_key('subsubsections'):
                        subsubsec=subsection['subsubsections']
                    if subsubsec:
                        for subsubsection in subsubsec:
                            btxt+=make_section('subsubsection', subsubsection['title'], root)
print btxt
