from packages.includes import scan
def reader(input,output):
    try:
        with open(input,'r') as file:
            for line in file:
                scan.open_redirect_scan(line.strip(),output)
    except FileNotFoundError:
        print("File not found. check the file paath and name.")
