import traceback

def get_traceback(err:str):
  trace_back = traceback.format_exc()
  return f"{err} {trace_back}"
