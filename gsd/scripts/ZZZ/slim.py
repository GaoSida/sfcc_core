# coding:utf-8
# 将输出文件进行瘦身

import re
import sys

if __name__ == "__main__":
    f = open(sys.argv[1], 'r').read()
    f = re.sub(r'\.0', '', f)

    f_w = open(sys.argv[1], 'w')
    f_w.write(f)
    f_w.close()








