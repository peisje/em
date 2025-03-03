import log_passer as logs
import report_generator as generateReport

log_file = "logs.txt"

result = logs.analyze_log(log_file)

generateReport.generate_report(result)