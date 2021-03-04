
import sys
from ruamel.yaml import YAML

f = open('t.yaml', 'r')


yaml = YAML()
raw = yaml.load(f)
print(raw)
yaml.indent(mapping=2, sequence=2, offset=2)
res = ''
res = yaml.dump_all(raw, sys.stdout)
# print(new)
