''' 
my project

check name of the registered people of list_1 in
 list_0 - list of a students of Capital English

'''
import re
import my_check
f = open('out_file.csv', 'w')

data = open ('all_list.csv')
#create list from spisok groups
list_gr = my_check.check_l(data)
print '------------------'
print list_gr
print '------------------'

out_list = []
out_list2 = []
data2 = open('reg_list.csv')
for line in data2:
    if re.search('[a-zA-Z0-9\._-]+@[a-z\.]+', line):
#        print "LINE:", line
        p = re.compile('[a-zA-Z0-9\._-]+@[a-z\.]+')
#        print '___',p
        n = p.findall(line)
        print '--',n
        for i in list_gr:
#            print "i:", i
            if i == n[0][:]:
                print "Ok"
                out_list.append(i)
                out_list2.append(line)
                print "ADD::::", line
                f.write(line + '\n')
#            else: print "No"
        print '____'
print out_list
#print out_list2
print 'the end'
