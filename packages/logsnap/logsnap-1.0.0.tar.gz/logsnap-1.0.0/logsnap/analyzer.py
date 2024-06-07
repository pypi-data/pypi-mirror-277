import argparse
from colorama import init, Fore, Style

init(autoreset=True)

def summarize(logs):

    counts = {
        'DEBUG': 0,
        'INFO': 0,
        'WARNING': 0,
        'ERROR': 0,
        'CRITICAL': 0,
        'FATAL': 0
    }

    for line in logs:
        for level in counts:
            if level in line:
                counts[level] += 1
    
    print(f'{Fore.CYAN}Log Summary:{Style.RESET_ALL}')

    for level, count in counts.items():
        if level == 'DEBUG':
            print(f'{Fore.BLUE}{level}: {count}{Style.RESET_ALL}')
        elif level == 'INFO':
            print(f'{Fore.GREEN}{level}: {count}{Style.RESET_ALL}')
        elif level == 'WARNING':
            print(f'{Fore.YELLOW}{level}: {count}{Style.RESET_ALL}')
        elif level == 'ERROR':
            print(f'{Fore.RED}{level}: {count}{Style.RESET_ALL}')
        elif level in ['CRITICAL', 'FATAL']:
            print(f'{Fore.MAGENTA}{level}: {count}{Style.RESET_ALL}')

def search_logs(logs, keyword):

    found = False

    print(f'{Fore.CYAN}Search Results for "{keyword}":{Style.RESET_ALL}')

    for line in logs:
        if keyword in line:
            found = True
            if 'DEBUG' in line:
                print(f'{Fore.BLUE}{line.strip()}{Style.RESET_ALL}')
            elif 'INFO' in line:
                print(f'{Fore.GREEN}{line.strip()}{Style.RESET_ALL}')
            elif 'WARNING' in line:
                print(f'{Fore.YELLOW}{line.strip()}{Style.RESET_ALL}')
            elif 'ERROR' in line:
                print(f'{Fore.RED}{line.strip()}{Style.RESET_ALL}')
            elif 'CRITICAL' in line or 'FATAL' in line:
                print(f'{Fore.MAGENTA}{line.strip()}{Style.RESET_ALL}')
            else:
                print(line.strip())
    
    if not found:
        print(f'{Fore.YELLOW}No results found for "{keyword}".{Style.RESET_ALL}')

def main():
    parser = argparse.ArgumentParser(description='Analyze log file.')
    parser.add_argument('file', type=str, help='Path to the log file.')
    parser.add_argument('--search', '-s', type=str, help='Keyword to search in the log file.')

    args = parser.parse_args()

    try:
        with open(args.file, 'r') as file:
            logs = file.readlines()
    except FileNotFoundError:
        print(f'{Fore.RED}Error: The file {args.file} was not found.{Style.RESET_ALL}')
        return
    
    if args.search:
        search_logs(logs, args.search)
    else:
        summarize(logs)
    
if __name__ == '__main__':
    main()