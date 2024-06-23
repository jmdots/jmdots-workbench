import pytest
from click.testing import CliRunner
from workbench.commands.rebase import rebase
import subprocess

def test_rebase_command(mocker):
    runner = CliRunner()

    # Mock subprocess calls
    mocker.patch('subprocess.check_output', return_value=b'feature-branch')
    mocker.patch('subprocess.check_call')

    result = runner.invoke(rebase)
    assert result.exit_code == 0
    assert "Rebase completed successfully." in result.output

    # Verify the sequence of subprocess calls
    subprocess.check_output.assert_called_once_with(["git", "branch", "--show-current"])
    subprocess.check_call.assert_any_call(["git", "checkout", "main"])
    subprocess.check_call.assert_any_call(["git", "fetch", "origin"])
    subprocess.check_call.assert_any_call(["git", "pull", "origin", "main"])
    subprocess.check_call.assert_any_call(["git", "checkout", "feature-branch"])
    subprocess.check_call.assert_any_call(["git", "rebase", "main"])
    subprocess.check_call.assert_any_call(["git", "push", "--force-with-lease"])
    subprocess.check_call.assert_any_call(["git", "log", "--oneline", "--graph", "--decorate", "--all"])
