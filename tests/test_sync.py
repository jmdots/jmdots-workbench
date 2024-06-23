import pytest
from click.testing import CliRunner
from workbench.commands.sync import sync
import subprocess
import os

def test_sync_command(mocker):
    runner = CliRunner()
    
    # Mock subprocess.check_call to prevent actual command execution
    mock_subprocess = mocker.patch('subprocess.check_call')
    
    # Test input parameters
    test_remote = "user@hostname.example.com"
    test_remote_dir = "/path/to/remote/dir"
    test_local_dir = "/path/to/local/dir"
    
    # Invoke the sync command with test parameters
    result = runner.invoke(sync, [
        '--remote', test_remote,
        '--remote-dir', test_remote_dir,
        '--local-dir', test_local_dir
    ])
    
    # Check if the command executed successfully
    assert result.exit_code == 0
    assert "Two-way sync completed successfully." in result.output
    
    # Verify the sequence of subprocess calls
    expected_calls = [
        mocker.call([
            "rsync", "-avz", "-e", "ssh", 
            f"{test_remote}:{os.path.join(test_remote_dir, '')}", os.path.join(test_local_dir, '')
        ]),
        mocker.call([
            "rsync", "-avz", "-e", "ssh", 
            os.path.join(test_local_dir, ''), f"{test_remote}:{os.path.join(test_remote_dir, '')}"
        ])
    ]
    mock_subprocess.assert_has_calls(expected_calls)
    
    # Verify the number of calls
    assert mock_subprocess.call_count == 2

def test_sync_command_error(mocker):
    runner = CliRunner()
    
    # Mock subprocess.check_call to simulate an error
    mocker.patch('subprocess.check_call', side_effect=subprocess.CalledProcessError(1, 'rsync'))
    
    # Test input parameters
    test_remote = "user@hostname.example.com"
    test_remote_dir = "/path/to/remote/dir"
    test_local_dir = "/path/to/local/dir"
    
    # Invoke the sync command with test parameters
    result = runner.invoke(sync, [
        '--remote', test_remote,
        '--remote-dir', test_remote_dir,
        '--local-dir', test_local_dir
    ])
    
    # Check if the command caught the error
    assert result.exit_code == 0
    assert "An error occurred during the sync process" in result.output

# Note: These tests focus on the logic of our sync function.
# They verify that:
# 1. The function constructs the correct rsync commands based on input parameters.
# 2. The function handles both successful execution and errors appropriately.
# 3. No actual network calls or rsync operations are performed during testing.
