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
        with open('./src/{}'.format(v), 'r') as fp:
            kw[p] = fp.read()

    o = './tex/{}.tex'.format(name)
    with open(o, 'w') as fp:
        fp.write(temp.format(**kw))



if __name__ == '__main__':
    name = 'dissertation'
    temp2tex(name)
#     rst2pdf(name)


