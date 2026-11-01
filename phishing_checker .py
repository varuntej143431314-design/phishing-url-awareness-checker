from urllib.parse import urlparse
from ipaddress import ip_address


def inspect_url(raw_url):
    warnings = []
    parsed = urlparse(raw_url)
    hostname = parsed.hostname or ""

    if "@" in raw_url:
        warnings.append("URL contains @ symbol")

    if len(raw_url) > 100:
        warnings.append("URL is longer than 100 characters")

    try:
        ip_address(hostname)
        warnings.append("URL uses an IP address instead of a domain")
    except ValueError:
        pass

    if len(hostname.split(".")) >= 5:
        warnings.append("Hostname has 5 or more segments")

    if "xn--" in hostname:
        warnings.append("Hostname contains punycode marker")

    if parsed.scheme.lower() == "http":
        warnings.append("URL uses HTTP instead of HTTPS")

    return warnings


def main():
    print("=== Phishing URL Awareness Checker ===")

    while True:
        raw_url = input(
            "\nEnter a URL (or type 'quit' to exit): "
        ).strip()

        if raw_url.lower() == "quit":
            print("Thank you for using the checker!")
            break

        if not raw_url:
            print("Please enter a URL.")
            continue

        warnings = inspect_url(raw_url)

        if warnings:
            print("\nWarnings found:")

            for warning in warnings:
                print("- " + warning)

            print("\nResult: REVIEW CAREFULLY")

        else:
            print("\nNo listed warning signs found.")
            print("Result: No warning signs detected.")

        print("\nNote: This tool does not guarantee that a URL is safe.")


if __name__ == "__main__":
    main()