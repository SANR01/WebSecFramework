import argparse

from modules.headers import security_headers
from modules.auth import auth_assessment
from modules.xss import xss_test
from modules.sqli import sqli_test
from modules.disclosure import information_disclosure

from utils.report import generate_html_report
from utils.logger import setup_logger

logger = setup_logger()
logger.info("Web Security Framework Started")

parser = argparse.ArgumentParser(
    prog="WebSecurityFramework",
    description="A Python-based Web Security Testing Framework",
    epilog="""
Examples:

python framework.py --target https://example.com --module headers

python framework.py --target https://example.com --module auth

python framework.py --target https://example.com --module xss

python framework.py --target "http://testphp.vulnweb.com/listproducts.php?cat=1" --module sqli

python framework.py --target https://example.com --module disclosure

python framework.py --target https://example.com --module all
""",
    formatter_class=argparse.RawDescriptionHelpFormatter
)


parser.add_argument(
    "--target",
    required=True,
    help="Target URL"
)

parser.add_argument(
    "--module",
    required=True,
    choices=[
        "headers",
        "auth",
        "xss",
        "sqli",
        "disclosure",
        "all"
    ],
    help="Select security testing module"
)

executed_modules = []

args = parser.parse_args()


print("=" * 50)
print(" Web Security Testing Framework ")
print("=" * 50)

print(f"Target : {args.target}")
print(f"Module : {args.module}")


if args.module == "headers":
    logger.info("Security Headers Module Started")
    security_headers(args.target)
    logger.info("Security Headers Module Completed")
    executed_modules.append("Security Headers")

elif args.module == "auth":
    logger.info("Authentication Module Started")
    auth_assessment(args.target)
    logger.info("Authentication Module Completed")
    executed_modules.append("Authentication Assessment")

elif args.module == "xss":
    logger.info("XSS Module Started")
    xss_test(args.target)
    logger.info("XSS Module Completed")
    executed_modules.append("XSS Testing")

elif args.module == "sqli":
    logger.info("SQLI Module Started")
    sqli_test(args.target)
    logger.info("SQLI Module Completed")
    executed_modules.append("SQL Injection")

elif args.module == "disclosure":
    logger.info("Information Discloure Module Started")
    information_disclosure(args.target)
    logger.info("Information Discloure Module Completed")
    executed_modules.append("Information Disclosure")

elif args.module == "all":

    logger.info("Running All Modules")

    security_headers(args.target)
    executed_modules.append("Security Headers")

    auth_assessment(args.target)
    executed_modules.append("Authentication Assessment")

    sqli_test(args.target)
    executed_modules.append("SQL Injection Assessment")

    xss_test(args.target)
    executed_modules.append("XSS Testing")

    information_disclosure(args.target)
    executed_modules.append("Information Disclosure")



generate_html_report(
    args.target,
    executed_modules
)

logger.info("Web Security Framework Finished")