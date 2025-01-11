import requests
from bs4 import BeautifulSoup
import os
import time

USACO_PROBLEM_URL = "https://usaco.org/index.php?page=viewproblem2&cpid="


def scrape_usaco_problem(cpid):
    """
    Scrapes a single USACO problem using its cpid.

    :param cpid: The problem ID (cpid).
    :return: A dictionary containing input and output test cases.
    """
    url = f"{USACO_PROBLEM_URL}{cpid}"
    response = requests.get(url)

    if response.status_code != 200:
        print(
            f"Error: Unable to fetch problem {cpid} (Status Code: {response.status_code})"
        )
        return {"input": [], "output": []}

    soup = BeautifulSoup(response.text, "html.parser")
    input_data, output_data = [], []

    try:
        # Locate the input and output sample test cases
        pre_tags = soup.find_all("pre")
        if len(pre_tags) >= 2:
            input_data = pre_tags[0].text.strip().split("\n")
            output_data = pre_tags[1].text.strip().split("\n")

    except Exception as e:
        print(f"Parsing error for problem {cpid}: {e}")

    return {"input": input_data, "output": output_data}


def save_test_case(cpid, test_cases):
    """
    Saves the test cases into files.

    :param cpid: The problem ID (cpid).
    :param test_cases: Dictionary containing input and output test cases.
    """
    problem_dir = f"problems/{cpid}"
    os.makedirs(problem_dir, exist_ok=True)

    input_file = os.path.join(problem_dir, "input.txt")
    output_file = os.path.join(problem_dir, "output.txt")

    with open(input_file, "w") as fin:
        fin.write("\n".join(test_cases["input"]) + "\n")

    with open(output_file, "w") as fout:
        fout.write("\n".join(test_cases["output"]) + "\n")

    print(f"✅ Saved test cases for problem {cpid}")


def scrape_and_save_problem(cpid):
    """
    Scrapes a single USACO problem and saves its test cases.

    :param cpid: The problem ID (cpid).
    """
    print(f"🔍 Scraping problem {cpid} from USACO...")
    test_cases = scrape_usaco_problem(cpid)

    if test_cases["input"] and test_cases["output"]:
        save_test_case(cpid, test_cases)
        print(f"🎉 Successfully saved test cases for problem {cpid}")
    else:
        print(f"⚠️ No valid test cases found for problem {cpid}")
