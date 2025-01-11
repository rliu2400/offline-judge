#!/usr/bin/env python3
import argparse
from commands import scrape, submit

def main():
    parser = argparse.ArgumentParser(prog="oj", description="Offline Judge CLI")
    subparsers = parser.add_subparsers(dest="command")

    # `oj scrape`
    scrape_parser = subparsers.add_parser("scrape", help="Scrape a contest")
    scrape_parser.add_argument("contest_id", type=str, help="Contest ID to scrape")

    # `oj submit`
    submit_parser = subparsers.add_parser("submit", help="Submit a solution")
    submit_parser.add_argument("problem_id", type=str, help="Problem ID")
    submit_parser.add_argument("file", type=str, help="Path to C++ solution file")

    args = parser.parse_args()

    if args.command == "scrape":
        scrape.scrape_contest(args.contest_id)
    elif args.command == "submit":
        submit.submit_solution(args.problem_id, args.file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

