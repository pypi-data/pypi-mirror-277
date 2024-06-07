import argparse
import os
import json
from app.reports.report import Report
from app.reports.report_engine import ReportEngine
from app.reports.report_lib import ReportInput

parser = argparse.ArgumentParser(description="Generate reports.")
parser.add_argument(
    "--spec", type=str, help="Path to the report specification JSON file"
)
parser.add_argument(
    "--api_key", type=str, help="API key", default=os.getenv("PROD_API_KEY")
)
parser.add_argument(
    "--api_url", type=str, help="API URL", default="https://api.spyderbat.com"
)
parser.add_argument("--org", type=str, help="Organization")
parser.add_argument(
    "-o", "--output_name", type=str, default="sample", help="Output name"
)

args = parser.parse_args()

with open(args.spec, "r") as f:
    report_input = json.load(f)
    report_input["org_uid"] = args.org
    ri = ReportInput.model_validate(report_input)
    rep = Report(input=ri, formats=["json", "yaml", "md", "html", "pdf"])

    engine = ReportEngine(
        {"backend": {"kind": "simple_file", "dir": "/tmp/reports"}}
    )

    reports = engine.make_reports(rep, args.api_key, args.api_url)
    for fmt, path in reports.items():
        # move the file path to the output name + format
        if "sample" in args.output_name:
            path.rename(f"{args.output_name}-{ri.report_id}.{fmt}")
        else:
            path.rename(f"{args.output_name}.{fmt}")
