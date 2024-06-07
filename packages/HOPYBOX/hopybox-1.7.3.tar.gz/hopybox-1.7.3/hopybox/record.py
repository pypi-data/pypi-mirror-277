import os
import linecache

if not os.path.exists('./HOPYBOX'):
  os.mkdir('./HOPYBOX')

def history_record(text):
  with open('./HOPYBOX/.history','a+') as file:
    file.write(f'{text}\n')
  file.close()

def history_read(all=False):
  linecache.clearcache()
  file = open('./HOPYBOX/.history','r')
  if all:
    return file.read()
  else:
    return linecache.getline('./HOPYBOX/.history',len(file.readlines()))