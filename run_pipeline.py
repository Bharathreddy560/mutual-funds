"""
Mutual Fund Analytics - Master Pipeline

Runs all major project stages in sequence.
Author: Bandi Bharath
"""

import subprocess
import sys


def run_script(script_name):
    """Run a Python script and stop if it fails."""

    print(f"\nRunning {script_name}...")

    result = subprocess.run(
        [sys.executable, script_name],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"Completed: {script_name}")
    else:
        print(f"Error in {script_name}")
        print(result.stderr)
        sys.exit(1)


def main():
    print("Mutual Fund Analytics Pipeline Started")

    scripts = [
        "data_ingestion.py",
        "live_nav_fetch.py",
        "dataclean+sql database.py",
        "recommender.py"
    ]

    for script in scripts:
        run_script(script)

    print("\nPipeline completed successfully!")


if __name__ == "__main__":
    main()