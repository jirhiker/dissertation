#===============================================================================
# Copyright 2013 Jake Ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#===============================================================================

#============= enthought library imports =======================

#============= standard library imports ========================
#============= local library imports  ==========================

#============= EOF =============================================
import yaml
import subprocess
import os
def temp2tex(name):
    p = './tex/{}.temp'.format(name)
    with open(p, 'r') as fp:
        temp = fp.read()

    c = './tex/{}.yaml'.format(name)
    with open(c, 'r') as fp:
        cfg = yaml.load(fp)
    kw = {}
    for k, v in cfg.iteritems():
        kw[k] = '{{{}}}'.format(v)

    # make abstract
    for p in ('abstract',):
        v = cfg[p]
        root = os.path.join('.', 'src',)
        convert_doc(root, p)

        with open(os.path.join(root, '{}.txt'.format(v)), 'r') as fp:
            kw[p] = fp.read()

    # make body
    kw['body'] = make_body(cfg)
    kw['appendix'] = make_appendix(cfg)

    o = './tex/{}.tex'.format(name)
    with open(o, 'w') as fp:
        fp.write(temp.format(**kw))

def make_body(cfg):
    btxt = ''
    for ci, ts in cfg['body']:
        root = os.path.join('.', 'src', ci)
#         btxt += '\chapter{{{}}}\n'.format(ti)

        for ti in ts:
            if isinstance(ti, list):
                for tii in ti:
                    if isinstance(tii, list):
                        for tiii in tii:
                            btxt += make_section('subsection', tiii, root)
                    else:
                        btxt += make_section('section', tii, root)
            else:
                btxt += make_section('chapter', ti, root)

    return btxt

def make_appendix(cfg):
    ap = cfg['appendices']
    txt = '\\appendix\n'
    for ti in ap:
        txt += '\chapter{{{}}}\n'.format(ti)
    return txt

def make_section(tag, name, root):
    body = ''
    if '|' in name:
        name, p = name.split('|')
        convert_doc(root, p)
#         docp = os.path.join(root, '{}.doc'.format(p))
#         if os.path.isfile(docp):
#             subprocess.call(['textutil', '-convert', 'txt', docp])

        with open(os.path.join(root, '{}.txt'.format(p)), 'r') as fp:
            body = fp.read()

    txt = '\{}{{{}}}\n{}'.format(tag, name, body)
    return txt

def convert_doc(root, path):
    docp = os.path.join(root, '{}.doc'.format(path))
    if os.path.isfile(docp):
        subprocess.call(['textutil', '-convert', 'txt', docp])

if __name__ == '__main__':
    name = 'dissertation'
    temp2tex(name)

    os.chdir('./tex')
#     print os.getcwd()
#     subprocess.call(['make.sh'])





