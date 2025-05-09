import click
from .scraper import scrape_problem, scrape_contest
from .benchmark import run_benchmarks


@click.group()
def cli():
    """oj: Offline Judge CLI"""
    pass


@cli.group()
def scrape():
    """🖌  Scrape problem statements or data."""
    pass


@scrape.command("problem")
@click.argument("cpid", type=int)
def scrape_problem_cmd(cpid):
    """Scrape USACO problem samples by CPID."""
    scrape_problem(cpid)
    click.echo(f"✓ problem {cpid} done ➜ problem-{cpid}")


@scrape.command("contest")
@click.argument("code", type=str)
@click.option("-o", "--out", default=".", help="Output directory")
def scrape_contest_cmd(code, out):
    """Download USACO contest data zip (e.g. dec20)."""
    scrape_contest(code, out)
    click.echo(f"✓ contest {code} done ➜ {out}/contests/{code}")


@cli.command("bench")
@click.option(
    "-a", "--algorithm", multiple=True, help="Name(s) of your algorithms to benchmark"
)
@click.option(
    "-i",
    "--input",
    type=click.Path(exists=True),
    help="Input file or directory for benchmarks",
)
def bench_cmd(algorithm, input):
    """⚡ Run benchmarks on your implementations."""
    run_benchmarks(algorithm, input)
