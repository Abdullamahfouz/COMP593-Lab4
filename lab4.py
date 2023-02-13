from log_anaylis import get_log_file_path_from_cmd_line, filter_log_by_regex
import pandas as pd
import csv
def main():
    log_file = get_log_file_path_from_cmd_line(1)
    port_traffic = tally_port_traffic(log_file)
    generate_invalid_user_report(log_file)
    generate_invalid_user_report(log_file)
    generate_source_ip_log('logfile.log', '220.195.35.40')
  
    for port_num, count in port_traffic.items():
        if count >= 100:
            generate_port_traffic_report(log_file, port_num)
   

    

# TODO: Step 8
def tally_port_traffic(log_file):
    data = filter_log_by_regex(log_file, r'DPT=(.+?) ')[1]
    port_traffic = {}
    for d in data:
        port = d[0]
        port_traffic[port] = port_traffic.get(port, 0) + 1
    return port_traffic

# TODO: Step 9
def generate_port_traffic_report(log_file, port_number):
    regex = r'(.{6}) (.{8}) .*SRC=(.+) DST(.+?) .+SPT=(.+)' + f'DPT=({port_number}) '
    data = filter_log_by_regex(log_file, regex)[1]

    report_df = pd.DataFrame(data)
    header_row = ('Date', 'Time', 'Source IP Address', 'Destination IP Address', 'Source Port', 'Destination Port')
    report_df.to_csv(f'destination_port_{port_number}_report.csv', index=False, header=header_row)
    

# TODO: Step 11
def generate_invalid_user_report(log_file):
    regex = r'(.{6}) (.{8}) .*Failed password for invalid user (\w+) from (.+)'
    data = filter_log_by_regex(log_file, regex)[1]

    report_df = pd.DataFrame(data, columns=('Date', 'Time', 'Username', 'IP Address'))
    report_df.to_csv('invalid_users.csv', index=False)
# TODO: Step 12
def generate_source_ip_log(log_file, ip_address):
  regex = r'(.{6}) (.{8}) .*SRC=(.+) .*' + f'SRC={ip_address} '
  data = filter_log_by_regex(log_file, regex)
  with open(f'source_ip_{ip_address.replace(".", "_")}.log', 'w') as file:
        for line in data[0]:
            file.write(line)

if __name__ == '__main__':
    main()
    
