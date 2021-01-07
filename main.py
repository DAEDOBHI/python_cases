from .utils.get_traceback import get_traceback

def test_traceback():

  try: 
    raise Exception('Example error traceback')
  except Exception as err:
    message = get_traceback(str(err))  
    print(message)
test_traceback()    