#/* encoding=gbk */
#/* vim: set expandtab ts=4 sw=4 sts=4 tw=100: */

with open("gbkInOct.data", "r") as f:
    line = f.readline().strip('"\n')
    while line:
        print "Before   : "
        print line
        print "After    : "
        print line.decode("string_escape").decode('gbk').encode('utf-8')
        print ""

        line = f.readline().strip('"\n')
