import os 
import sys 


old_dir = sys.argv[1]
new_dir = sys.argv[2]
print(old_dir)
print(new_dir)


print("Checking old dir files")

old_names = []

for files in os.listdir(old_dir):
	print(files)
	old_names.append(files)

new_names = []
print("Checking new dir files")
for files in os.listdir(new_dir):
	print(files)
	new_names.append(files)

count = 0
for o_name in old_names:
	if o_name in new_names:
		count +=1

print("Total Number of changes: ", len(new_names) - count)
print("Human Error Rate ", float(len(new_names) - count)/len(new_names) )







