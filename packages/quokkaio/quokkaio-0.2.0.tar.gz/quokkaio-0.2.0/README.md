# Quokka.io

This project provides a Python client for interacting with the Quokka API. The client allows users to perform various operations such as uploading files for scanning, retrieving scan results, downloading reports, and managing subgroups.

https://www.quokka.io/

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Initialization](#initialization)
  - [Push Scan](#push-scan)
  - [Get Subgroups](#get-subgroups)
  - [Wait for Scan Completion](#wait-for-scan-completion)
  - [Download PDF Report](#download-pdf-report)
  - [Get App Issues](#get-app-issues)
  - [Get Results](#get-results)
  - [Get Submitted Apps](#get-submitted-apps)
- [Logging](#logging)
- [Contributing](#contributing)
- [License](#license)


## Installing

To install the Quokka API Client, use pip:

```
pip install quokkaio
```

## Usage

### Initialization

First, import the `Quokka` class and create an instance with your API key:

```python
from quokka import Quokka

api_key = "YOUR_API_KEY"
quokka = Quokka(api_key)
```

### Push Scan

Upload an APK or IPA file for scanning:

```python
the_file = "path/to/your/app.apk"
subgroup_ids = ["subgroup1", "subgroup2"]
response_data, platform = quokka.push_scan(the_file, subgroup_ids)
print(response_data, platform)
```

### Get Subgroups

Retrieve a list of subgroups:

```python
quokka.get_sub_groups()
```

Retrieve a specific subgroup ID by name:

```python
subgroup_id = quokka.get_sub_groups(the_group="specific_group_name")
print(subgroup_id)
```

### Wait for Scan Completion

Wait for a scan to complete:

```python
uuid = "scan_uuid"
quokka.wait_for_scan_complete(uuid, maxWaitTime=30)  # maxWaitTime in minutes
```

### Download PDF Report

Download the scan results as a PDF file:

```python
uuid = "scan_uuid"
quokka.download_pdf(uuid)
```

### Get App Issues

Retrieve app issues in JSON format:

```python
uuid = "scan_uuid"
issues = quokka.get_app_issue(uuid)
print(issues)
```

### Get Results

Retrieve specified results in JSON format from a start date:

```python
from datetime import datetime

start_date = datetime(2023, 1, 1)
results = quokka.get_results(start_date)
print(results)
```

### Get Submitted Apps

Retrieve submitted apps within a date range:

```python
from datetime import datetime

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 6, 1)
apps = quokka.get_apps(start_date, end_date)
print(apps)
```

## Logging

This client uses Python's built-in logging module to provide debug information. By default, logging is set to the DEBUG level. You can configure the logging level and format as needed.

## Contributing

If you want to contribute to this project, please fork the repository and create a pull request with your changes. Make sure to write tests and documentation for new features or modifications.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
