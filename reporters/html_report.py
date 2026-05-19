def generate_html_report(results):
    html = "<html><body><h2>Test Report</h2><table border='1'>"

    for r in results:
        html += f"<tr><td>{r['test']}</td><td>{r['status']}</td></tr>"

    html += "</table></body></html>"

    with open("report.html", "w") as f:
        f.write(html)
