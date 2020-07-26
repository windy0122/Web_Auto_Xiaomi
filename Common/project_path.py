import os

file = os.path.realpath(__file__)
file_name = os.path.split(os.path.split(file)[0])[0]
# 截图路径
image_path = os.path.join(file_name, 'Outputs', 'screenshots')

# 测试报告路径
test_report_path = os.path.join(file_name, 'Outputs', 'report', 'test_report.html')

# print(test_report_path)