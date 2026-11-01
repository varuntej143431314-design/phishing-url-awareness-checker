Phishing URL Awareness Checker

1. Project Overview

The Phishing URL Awareness Checker is a beginner-friendly Python cybersecurity project that identifies common warning signs in URL text.

The main purpose of this project is to help users understand potential phishing risks by checking visible URL characteristics.

This program only analyzes URL text. It does not open websites or send data over the internet.

2. Objectives

- Understand phishing attacks and URL structures.
- Identify common phishing warning signs.
- Learn Python programming fundamentals.
- Develop basic cybersecurity awareness.
- Practice testing and documenting a project.
- Publish the project using GitHub.

3. Features

This project checks six URL warning signs:

1. @ Symbol Detection – Identifies URLs containing an @ symbol.
2. Long URL Detection – Identifies URLs longer than 100 characters.
3. IP Address Detection – Identifies URLs using an IP address as the hostname.
4. Hostname Segment Detection – Identifies hostnames containing five or more segments.
5. Punycode Detection – Identifies hostnames containing the "xn--" marker.
6. HTTP Detection – Identifies URLs using HTTP instead of HTTPS.

Additional Improvements

- Loop with Quit: Allows users to check multiple URLs without restarting the program.
- Review Carefully Summary: Displays a warning summary when warning signs are detected.

4. Technologies Used

- Python 3
- VS Code
- GitHub
- Python Standard Library ("re", "urllib.parse")

5. Requirements

- Python 3.10 or later.
- Visual Studio Code (recommended).
- Windows, Linux, or macOS.

No additional Python packages are required.

6. Project Structure

phishing-url-awareness/
│
├── phishing_checker.py
├── README.md
├── requirements.txt
│
├── tests/
│   └── test_samples.md
│
└── screenshots/
    ├── sample_run.png
    └── test_results.png

7. How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

python phishing_checker.py

5. Enter a sample URL.
6. Check the displayed results.
7. Type "q" to exit the program.

8. Sample Testing

No.| Sample URL| Expected Result
1| https://www.example.com/login| No listed warning signs
2| http://192.0.2.10/account| IP address and HTTP warnings
3| http://example.com@sample.invalid/login| @ symbol and HTTP warnings
4| https://a.b.c.d.e.example.invalid/path| Many hostname segments
5| https://xn--example.invalid/| Punycode warning

All tests should be run using the sample URLs provided in the project workbook. Record the actual results in "tests/test_samples.md".

9. Screenshots

Sample Program Output

"Sample Run" (screenshots/sample_run.png)

Test Results

"Test Results" (screenshots/test_results.png)

10. Limitations

- This project only checks visible URL text.
- It does not visit or open websites.
- It does not scan for malware.
- It does not use online reputation services.
- It cannot guarantee that a URL is safe.

Important: No warning signs found does NOT mean a URL is safe.

11. Ethical Use

This project is developed for educational and cybersecurity awareness purposes.

- Use only the provided sample URLs.
- Never enter passwords or sensitive information.
- Do not use this tool to deceive anyone.
- Do not scan or test websites without permission.

12. Author

Name: CHODISETTI Vinay
Course: B.Tech – Electronics and Communication Engineering
Project: Cybersecurity Mini Project
Language: Python

---

Project Title: Phishing URL Awareness Checker
Purpose: Educational Cybersecurity Project
