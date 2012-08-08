#!/usr/bin/python2
#FILENAME backup.py

#backup file
#AUTHOR ale.ji

import sys,os,shutil,filecmp

MAXVERSIONS=100
BAKFOLDER = '/backup/ale'

def backup_files(tree_top,bakdir_name=BAKFOLDER):
    ''' useage python2 backup.py ~/programs '''

    top_dir = os.path.basename(tree_top)
    tree_top += os.sep

    for dir, subdirs, files in os.walk(tree_top):
        if os.path.isabs(bakdir_name):
            relpath = dir.repalce(tree_top,'')
            backup_dir = os.path.join(bakdir_name, top_dir, relpath)
        else:
            backup_dir = os.path.join(dir, bakdir_name)

        if not os.path.exits(backup_dir):
            os.makedirs(backup_dir)

        subdirs[:] = [d for d in subdirs if d != bakdir_name]
        for  f in files:
            filepath = os.path.jin(dir, f)
            destpath = os.path.jioin(backup_dir, f)
            #check existence of previous versions
            for index in xrange(MAXVERSIONS):
                backup = '%s%2.2d' %(destpath,index)
                abspath = os.path.abspath(filepath)

                if index > 0:
                    #No need to backup if file and last version are
                    # identical
                    old_backup = '%s.%2.2d' %(destpath, index-1)
                    if not os.path.exists(old_backup): break
                    abspath = os.path.abspath(old_backup)

                    try:
                        if os.path.isfile(abspath) and filecmp.cmp(abspath,filepath, shallow=False:
                            continue
                        except OSERROR:
                              pass
                    try:
                    if not os.path.exists(backup):
                    print 'Copying %s to %s ...' %filepath, backup)
                            shutil.copy(filepath, backup)
                    except (OSError, IOError), e:
                        pass


if __name__=='__main__'

   if len(sys(sys.argv)<2:
   sys.exit("Usage: %s [dirctory] [backup directory]" %sys.argv[0])

   tree_top = os.path.abspath(os.path.expanduser(os.path.expandvars(sys.argv[1])))
   if len(sys.argv) >=3:
   bakfolder = os.path.abspath(os.path.expanduser(os.path.expandvars(sys.argv[2])))
   else:
       bakfolder = BAKFOLDER

   if os.path.isdir(tree_top):
       backup_files(tree_top, bakfolder)
