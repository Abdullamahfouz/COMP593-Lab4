import sys
import os
import re

# TODO: Step 3
def get_log_file_path_from_cmd_line(pram_num):
   
    num_prams = len(sys.argv) -1
    if num_prams >= pram_num:
        log_file_path = sys.argv[pram_num]
        if os.path.isfile(log_file_path):
            return log_file_path
        else:
            print("Error: Specfied path is not a file.")
            sys.exit(1)
    else:
        print("Error: Missing log file path.")
        sys.exit(1)
    

# TODO: Steps 4-7
def filter_log_by_regex(log_file, regex, ignore_case=True, print_summary=False, print_records=False):
  
  records = []
  captured_data = []
  regex_flags = re.IGNORECASE if ignore_case else 0
  
  with open(log_file, 'r') as file:
      for line in file:
          match = re.search(regex, line, regex_flags)
          if match:
              records.append(line)
              if match.lastindex:
                  captured_data.append(match.groups())
  if print_records is True:
        print (*records, sep= '' , end= "\n")
  if print_summary is True:
      print(f'The log file conatains {len(records)} records that case- {"in" if ignore_case else""} sentstive match the regex "{regex}".')
  
  return records, captured_data