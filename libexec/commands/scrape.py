import os
from utils.scraper import scrape_usaco_contest

def scrape_contest(contest_id):
    print(f"Scraping contest {contest_id}...")

    problems = scrape_usaco_contest(contest_id)
    contest_dir = f"problems/{contest_id}"
    os.makedirs(contest_dir, exist_ok=True)

    for problem_id, test_cases in problems.items():
        problem_dir = f"{contest_dir}/{problem_id}"
        os.makedirs(problem_dir, exist_ok=True)

        # Save test cases
        with open(f"{problem_dir}/input.txt", "w") as fin:
            fin.writelines(test_cases["input"])
        with open(f"{problem_dir}/output.txt", "w") as fout:
            fout.writelines(test_cases["output"])

    print(f"Scraped {len(problems)} problems from {contest_id}.")

