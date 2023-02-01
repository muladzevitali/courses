import time
from ddtrace.runtime import RuntimeMetrics

RuntimeMetrics.enable()

while True:
    time.sleep(1)
