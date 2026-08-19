"""
Mutual Fund Analytics - Master Pipeline

Runs all major project stages in sequence.
Author: Bandi Bharath
"""

import subprocess
import sys


def run_script(script_name, input_text=None):
    """Run a Python script and stop if it fails."""

    print(f"\nRunning {script_name}...")

    result = subprocess.run(
        [sys.executable, script_name],
        input=input_text,
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    if result.returncode == 0:
        print(f"Completed: {script_name}")

        if result.stdout.strip():
            print(result.stdout)

    else:
        print(f"Error in {script_name}")

        if result.stdout.strip():
            print(result.stdout)

        if result.stderr.strip():
            print(result.stderr)

        sys.exit(1)


def main():
    print("Mutual Fund Analytics Pipeline Started")

    run_script("data_ingestion.py")
    run_script("live_nav_fetch.py")
    run_script("dataclean+sql database.py")

    run_script("recommender.py", input_text="Moderate\n")

    print("\nPipeline completed successfully!")


if __name__ == "__main__":
    main()