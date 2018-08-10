#/* encoding=utf-8 */
#/* vim: set expandtab ts=4 sw=4 sts=4 tw=100: */

with open("unicode.data", "r") as f:
    line = f.readline().strip('"\n')
    while line:
        print "Before   : "
        print line
        print "After    : "
        print line.decode("unicode-escape")
        print ""

        line = f.readline().strip('"\n')
