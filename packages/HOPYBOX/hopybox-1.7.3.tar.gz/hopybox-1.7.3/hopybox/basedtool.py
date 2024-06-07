import os

def terminal(command):
  os.system(command)

def clear():
  print("\033c",end="")
  terminal('cls' if os.name == 'nt' else 'clear')