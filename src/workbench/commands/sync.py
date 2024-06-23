import click
import subprocess
import os

@click.command()
@click.option('--remote', required=True, help='Remote server (user@hostname)')
@click.option('--remote-dir', required=True, help='Directory path on remote server')
@click.option('--local-dir', required=True, help='Local directory path')
def sync(remote, remote_dir, local_dir):
    """Perform a two-way sync between a local and a remote directory using rsync over SSH."""
    try:
        # Ensure directories end with a slash
        remote_dir = os.path.join(remote_dir, '')
        local_dir = os.path.join(local_dir, '')

        # Sync from remote to local
        click.echo("Syncing from remote to local...")
        subprocess.check_call([
            "rsync", "-avz", "-e", "ssh", 
            f"{remote}:{remote_dir}", local_dir
        ])

        # Sync from local to remote
        click.echo("Syncing from local to remote...")
        subprocess.check_call([
            "rsync", "-avz", "-e", "ssh", 
            local_dir, f"{remote}:{remote_dir}"
        ])

        click.echo("Two-way sync completed successfully.")
    except subprocess.CalledProcessError as e:
        click.echo(f"An error occurred during the sync process: {e}")

if __name__ == '__main__':
    sync()
