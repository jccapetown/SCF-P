#Generate a file development template file
import datetime
import os



projectname = raw_input('Project Name:')
description = raw_input('Description:')
author = raw_input('Author:')

os.mkdir('projects/%s' % projectname, 0755 );
f = open('projects/%s/%s.py'% (projectname, projectname), 'wb')

#File details

f.write('#File Name   : %s.py \n' % projectname)
f.write('#Description : %s \n' % description)
f.write('#Author      : %s \n' % author)
f.write('#Date        : %s \n' % datetime.datetime.now())
f.write('\n')
f.write('\n')
f.write('#Import Section\n')
f.write('import os,sys\n')
f.write('sys.path.append(\'../../includes\') \n')
f.write('#import func_file\n')
f.write('#import func_strings\n')
f.write('#import func_ftp\n')
f.write('#import func_inifile\n')
f.write('\n')
f.write('\n')
f.write('#Global Variables\n')
f.write('\n')
f.write('\n')
f.write('#Function/Methods/class definition\n')
f.write('\n')
f.write('\n')
f.write('#Main Section\n')
f.close()
