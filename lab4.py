from log_anaylis import get_log_file_path_from_cmd_line, filter_log_by_regex
def main():
    log_file = get_log_file_path_from_cmd_line(1)
    records = filter_log_by_regex(log_file, 'SRC=(.*?) DST=(.*?) LEN=(.*?) ', print_summary= True,print_records=True)
    port_traffic = tally_port_traffic(log_file)
   
    pass

# TODO: Step 8
def tally_port_traffic(log_file):
   data = filter_log_by_regex(log_file, r'DPT = (.+?)')[1]
   port_tarffic = {}
   for d in data:
       port= [0]
       port_tarffic[port] = port_tarffic.get(port,0) + 1
   
   return port_tarffic

# TODO: Step 9
def generate_port_traffic_report(log_file, port_number):
    regex = r'({6}) (.{8}0)    r
    ecords, data = filter_log_by_regex(log_file, 'SRC=(.*?) DST=(.*?) LEN=(.*?) ', print_summary= True,print_records=True)
    
    
    
    
    return

# TODO: Step 11
def generate_invalid_user_report(log_file):
    return

# TODO: Step 12
def generate_source_ip_log(log_file, ip_address):
    return

if __name__ == '__main__':
    main()