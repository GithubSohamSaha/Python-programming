# 5. Log File Analyzer
# •Problem: Write a program to analyze a log file and extract useful information such as error counts and timestamps.
# •Example: Given a server log file, count the number of error occurrences and list the corresponding timestamps.
# •Objective: Parse and process log files to extract patterns like error messages, IP addresses, or other critical information.

import re
from collections import Counter

def analyze_log_file(log_file):
    try:
        # Open the log file in read mode
        with open(log_file, 'r') as file:
            lines = file.readlines()

        # Initialize variables
        error_count = Counter()  # To count occurrences of each error
        error_details = []  # To store timestamps and error messages

        # Regex patterns for timestamp and error messages
        timestamp_pattern = r'\[(.*?)\]'  # Matches timestamps like [2025-01-25 10:00:00]
        error_pattern = r'(ERROR|WARNING|CRITICAL): (.+)'  # Matches error messages with their severity

        # Process each line in the log file
        for line in lines:
            timestamp_match = re.search(timestamp_pattern, line)
            error_match = re.search(error_pattern, line)

            if error_match:
                # Extract timestamp and error message
                timestamp = timestamp_match.group(1) if timestamp_match else "No timestamp"
                error_message = error_match.group(2)
                severity = error_match.group(1)

                # Increment error count and store details
                error_count[error_message] += 1
                error_details.append((timestamp, severity, error_message))

        # Display results
        print("Error Counts:")
        for error, count in error_count.items():
            print(f"{error}: {count} occurrences")

        print("\nError Details:")
        for timestamp, severity, message in error_details:
            print(f"[{timestamp}] {severity}: {message}")

    except FileNotFoundError:
        print(f"Error: File '{log_file}' not found.")

# Specify the log file name
log_file = 'server.log'

# Analyze the log file
analyze_log_file(log_file)
