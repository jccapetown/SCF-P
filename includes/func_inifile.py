#This function creates a dictionary from a ini config file.
def get_dict(filedict, filename):
    section = None
    for ix,fline in enumerate(filename):
        line = fline.strip()
        if (line != '') and  (('#' not in line) and (';' not in line)):
            #yeah lets work with the line
            #now lets get the sections
            if '[' == line[0]:
                section = line
                if section not in filedict:
                    filedict[section] = {}
            elif (section is not None) and ('=' in line):
                key,val = line.split('=',1)
                #print section, key, val
                if key not in filedict[section]:
                    filedict[section][key] = []
                filedict[section][key].append(val)

#write the new ini file from loaded file
def write_ini(inifilename, filedict) :               
    f = open(inifilename,'wb')
    for section in filedict:
        f.write('\n')
        f.write('%s\n'%section)
        for key in filedict[section]:
            for val in filedict[section][key]:
                #print section, key, val
                f.write('%s=%s\n'%(key, val))

    f.close()
