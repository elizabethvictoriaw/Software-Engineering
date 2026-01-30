import sys, traceback
try:
    import nltk
    print('OK', getattr(nltk, '__file__', None))
    print('has internals?', hasattr(nltk, 'internals'))
except Exception as e:
    print('ERR', repr(e))
    m = sys.modules.get('nltk')
    print("sys.modules['nltk']:", m)
    if m is not None:
        print('module file:', getattr(m, '__file__', None))
    traceback.print_exc()
