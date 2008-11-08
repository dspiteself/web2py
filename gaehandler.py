import time,os,sys,logging
import google
import cPickle,pickle
sys.modules['cPickle'] = sys.modules['pickle']
import wsgiref.handlers
import gluon.main
import logging

debug = os.environ.get('SERVER_SOFTWARE','').startswith('Devel')

def log_stats(fun):
   if debug:
       def newfun(e,r):
           t0 = time.time()
           c0 = time.clock()
           out = fun(e,r)
           c1 = time.clock()
           t1 = time.time()
           s = """**** Request: %5.0fms/%.0fms (real time/cpu time)""" % \
             ( (t1-t0) * 1000, (c1-c0) * 1000 )
           logging.info(s)
           return out
       return newfun
   else:
       return fun

### comment logging and uncomment @log_stats to enable logging of stats on GAE
logging.basicConfig(level=35) 
#@log_stats
def wsgiapp(env,res):
  return gluon.main.wsgibase(env,res)

def main():
  wsgiref.handlers.CGIHandler().run(wsgiapp)

if __name__ == '__main__':
    main() 