import logging

import syworkflow as wf

logging.basicConfig(
    format='[%(asctime)s] %(levelname)s - '
    '%(name)s.%(funcName)s(%(lineno)s) '
    '[%(processName)s]<%(threadName)s>'
    ': %(message)s',
    level=logging.DEBUG)

if __name__ == '__main__':
  task1 = wf.TimerTask(hour=0, minute=2)
  task2 = wf.TimerTask(hour=0, minute=0, dep_tasks=[task1])
  schd = wf.TaskScheduler()
  schd.add_task(task2)
  schd.start()
