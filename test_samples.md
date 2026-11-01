Phishing URL Awareness Checker – Test Results

Test Environment

- Language: Python 3.10+
- Project: Phishing URL Awareness Checker
- Testing Type: Sample URL testing

Test Cases

Test No.| Sample URL| Expected Result| Status
1| "https://www.example.com/login"| No listed warning signs detected| PASS
2| "http://192.0.2.10/account"| IP address hostname and HTTP warning| PASS
3| "http://example.com@sample.invalid/login"| @ symbol and HTTP warning| PASS
4| "https://a.b.c.d.e.example.invalid/path"| Hostname contains 5 or more segments| PASS
5| "https://xn--example.invalid/"| Punycode marker detected| PASS

Test Result Summary

- Total test cases: 5
- Passed: 5
- Failed: 0
- Overall Result: PASS

Conclusion

All five test cases were executed successfully. The Phishing URL Awareness Checker detected the expected warning signs in the sample URLs.
