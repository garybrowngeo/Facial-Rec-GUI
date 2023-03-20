from FacialRec2_GUI import *
from FacialRec2_functions import *

#Redirect Stdout to log file
old_stdout = sys.stdout
log_file = open("Results.txt","w")
sys.stdout = log_file

#Define function to redirect Stdout and close log file
def close_log():
  sys.stdout = old_stdout
  log_file.close()       

# Run application
def main():
  main_menu()

if __name__ == '__main__':
  main()





