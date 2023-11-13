# URL Vulnerability Checker

This is a simple Python script for checking directory traversal vulnerabilities in URLs. The script attempts to access the "/etc/passwd" file by using a specified number of "../" iterations.

## Usage

# 1. Checking a single URL:
 
`python3 etc-passwd-finder.py --single http://example.com`

# 2. Checking a urls file :

`python3 etc-passwd-finder.py --file urls.txt`



## Generate URLs using `waybackurls` and check for etc/passwd file in Urls:
 
 ##  [waybackurls](https://github.com/tomnomnom/waybackurls) Downloads


### Prerequisites
- Python 3.x
- Requests library (`pip install requests`)
- argparse library (`pip install argparse`)

### Command-line Arguments

- `--file`: Specifies a file containing multiple URLs to check.
- `--single`: Specifies a single URL to check.
- `--iterations`: Number of "../" iterations for the directory traversal payload (default is 5).
- `--hide`: If provided, it hides non-200 responses.
- `--help`: If provided, it prints all available options.


   

