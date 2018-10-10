import os
import sys
import numpy
import pandas as pd



# first old, second new
#old_dir = "testdir/old"
#new_dir = "testdir/new"
old_dir = sys.argv[1]
new_dir = sys.argv[2]
print("old names are : " + old_dir)
print("new names are : " + new_dir)


# Collect old file names 
print("Collecting old names")

old_names = []
for files in os.listdir(old_dir):
	print(files)
	old_names.append(files)

print("Collecting new names")
new_names = []
for files in os.listdir(new_dir):
	print(files)
	new_names.append(files)




o_files_split = pd.DataFrame(columns = ['id','visit','score'])
for o_files in old_names:
	# split up names
	splits = o_files.split("_")
	if len(splits) > 2:
		o_files_split = o_files_split.append({'id':splits[0],
										  'visit':splits[1],
										  'score':splits[2]},ignore_index=True)
	else:
		print(o_files)



n_files_split = pd.DataFrame(columns = ['id','visit','score'])
for n_files in new_names:
	# split up names 
	splits = n_files.split("_")
	if len(splits) > 2:
		n_files_split = n_files_split.append({'id':splits[0],
										  'visit':splits[1],
										  'score':splits[2]},ignore_index=True)
	else:
		print(n_files)


o_files_split.to_csv('old_names_split.csv')
n_files_split.to_csv('new_names_split.csv')


