import click
from rich.console import Console

from cli.plan_executor import PlanExecutor
from cli.constants import CHEAP_MODEL, DEFAULT_MODEL
from cli.status_indicator import StatusIndicator
from cli.task_runner import TaskRunner


@click.command()
@click.option('--wait/--no-wait', is_flag=True, default=True, help='Wait for PR Pilot to finish the task.')
@click.option('--repo', help='Github repository in the format owner/repo.', required=False)
@click.option('--snap', is_flag=True, help='Select a portion of your screen to add as an image to the task.')
@click.option('--plan', '-p', type=click.Path(exists=True), help='Path to YAML file containing step-by-step plan for PR Pilot.')
@click.option('--edit', '-e', type=click.Path(exists=True), help='Let PR Pilot edit a file for you.')
@click.option('--spinner/--no-spinner', is_flag=True, default=True, help='Display a loading indicator.')
@click.option('--quiet', is_flag=True, default=False, help='Disable all output on the terminal.')
@click.option('--cheap', is_flag=True, default=False, help=f'Use the cheapest GPT model ({CHEAP_MODEL})')
@click.option('--code', is_flag=True, default=False, help='Optimize prompt and settings for generating code')
@click.option('--file', '-f', type=click.Path(exists=True), help='Generate prompt from a template file.')
@click.option('--direct', is_flag=True, default=False,
              help='Do not feed the rendered template as a prompt into PR Pilot, but render it directly as output.')
@click.option('--output', '-o', type=click.Path(exists=False), help='Output file for the result.')
@click.option('--model', '-m', help='GPT model to use.', default=DEFAULT_MODEL)
@click.option('--debug', is_flag=True, default=False, help='Display debug information.')
@click.argument('prompt', nargs=-1)
def main(wait, repo, snap, plan, edit, spinner, quiet, cheap, code, file, direct, output, model, debug, prompt):
    """Create a new task for PR Pilot - https://docs.pr-pilot.ai"""

    console = Console()
    show_spinner = spinner and not quiet
    status_indicator = StatusIndicator(spinner=show_spinner, messages=not quiet, console=console)

    try:
        if plan is not None:
            runner = PlanExecutor(plan, status_indicator)
            runner.run(wait, repo, edit, quiet, model, debug, prompt)
            return

        runner = TaskRunner(status_indicator)
        runner.run_task(wait, repo, snap, edit, quiet, cheap, code, file, direct, output, model, debug, prompt)
        status_indicator.stop()
    except Exception as e:
        status_indicator.fail()
        console.print(f"[bold red]An error occurred:[/bold red] {type(e)} {str(e)}")


if __name__ == '__main__':
    main()