import logging

import syworkflow as wf

logging.basicConfig(
    format='[%(asctime)s] %(levelname)s - '
    '%(name)s.%(funcName)s(%(lineno)s) '
    '[%(processName)s]<%(threadName)s>'
    ': %(message)s',
    level=logging.DEBUG)

if __name__ == '__main__':
  task = wf.TimerTask(hour=9, minute=38)
  schd = wf.TaskScheduler()
  schd.add_task(task)
  schd.start()
