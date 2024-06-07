# LogSnap

LogSnap is a simple command-line tool for analyzing log files. It provides a clear, colored summary of log levels and allows users to search for specific keywords within the logs, highlighting the results for easy troubleshooting.

## Features

- **Log Summary**: Get a quick overview of log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL, FATAL) with colored output.
- **Keyword Search**: Search for specific keywords in the log file and see the results highlighted in color.
- **Cross-Platform**: Works seamlessly on Windows, Mac, and Linux.

## Installation

Install LogSnap using pip:

```sh
pip install logsnap
```

## Usage

**To get a summary of the log file, run:**

```sh
logsnap path/to/logfile.log
```

**To search for a specific keyword in the log file, use:**

```sh
logsnap path/to/logfile.log --search keyword
```

Or using the short option for search:

```sh
logsnap path/to/logfile.log -s keyword
```

## License

This project is licensed under the MIT License.