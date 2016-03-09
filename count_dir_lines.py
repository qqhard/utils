import os
import sys

def fun(path, endw):
    ret = 0
    fileList = os.listdir(path)
    for f in fileList:
        new_path = path + '/' +f
        if os.path.isdir(new_path):
            ret += fun(new_path, endw)
        if os.path.isfile(new_path) and f.endswith(endw):
            ret += count_line(new_path)
    return ret

def count_line(path):
    f = open(path,'r')
    ret = len(f.readlines())
    f.close()
    print('{0} {1}'.format(ret, f.name))
    return ret

if __name__ == '__main__':
    path = sys.argv[1]
    endw = sys.argv[2]
    print fun(path,endw)
