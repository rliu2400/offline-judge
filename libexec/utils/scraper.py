import requests
from bs4 import BeautifulSoup


def scrape_usaco_contest(contest_id):
    url = f"https://usaco.org/index.php?page=viewcontest&contestid={contest_id}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    problems = {}
    for problem_link in soup.find_all("a", href=True):
        if "index.php?page=viewproblem" in problem_link["href"]:
            problem_id = problem_link["href"].split("problemid=")[-1]
            problems[problem_id] = scrape_usaco_problem(problem_id)

    return problems


def scrape_usaco_problem(problem_id):
    url = f"https://usaco.org/index.php?page=viewproblem2&problemid={problem_id}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    input_data = soup.find("pre", class_="input").text
    output_data = soup.find("pre", class_="output").text

    return {"input": input_data.splitlines(), "output": output_data.splitlines()}
