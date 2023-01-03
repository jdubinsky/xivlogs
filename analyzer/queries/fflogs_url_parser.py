from urllib.parse import urlparse

def get_report_code_from_url(report_url: str) -> str:
    parsed_url = urlparse(report_url)
    if parsed_url.netloc != "www.fflogs.com":
        raise Exception("Expected fflogs URL")

    url_path = parsed_url.path
    if not url_path.startswith('/reports/'):
        raise Exception("URL must be a reports URL")

    report_code = url_path.split('/')[2]

    return report_code
