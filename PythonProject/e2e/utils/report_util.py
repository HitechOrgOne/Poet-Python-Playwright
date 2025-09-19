import subprocess
import os

def generate_allure_report(results_dir="reports/allure-results", report_dir="reports/allure-report"):
    try:
        os.makedirs(report_dir, exist_ok=True)
        subprocess.run(
            ["allure", "generate", results_dir, "-o", report_dir, "--clean"],
            check=True
        )
        print(f"\n✅ Allure report generated: {report_dir}/index.html")
    except Exception as e:
        print(f"\n❌ Failed to generate Allure report: {e}")
