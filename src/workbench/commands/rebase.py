import click
import subprocess

@click.command()
def rebase():
    """Rebase the current branch on top of the main branch."""
    try:
        # Get the current branch name
        current_branch = subprocess.check_output(["git", "branch", "--show-current"]).strip().decode('utf-8')

        # Checkout to main branch
        subprocess.check_call(["git", "checkout", "main"])

        # Fetch and pull the latest changes from the main branch
        subprocess.check_call(["git", "fetch", "origin"])
        subprocess.check_call(["git", "pull", "origin", "main"])

        # Checkout back to the original branch
        subprocess.check_call(["git", "checkout", current_branch])

        # Rebase the current branch on top of the main branch
        subprocess.check_call(["git", "rebase", "main"])

        # Push the changes
        subprocess.check_call(["git", "push", "--force-with-lease"])

        # Show the commit log
        subprocess.check_call(["git", "log", "--oneline", "--graph", "--decorate", "--all"])

        click.echo("Rebase completed successfully.")
    except subprocess.CalledProcessError as e:
        click.echo(f"An error occurred during the rebase process: {e}")
