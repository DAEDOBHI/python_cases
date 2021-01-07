import traceback
try:
  raise Exception('error')
except Exception as err:
    trace_back = traceback.format_exc()
    message = str(err) + " " + str(trace_back)
    print(message)  