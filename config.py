from logging import getLogger
from sys import exit

from yaml import safe_load


class Config():
    def __init__(self, config):
        self.log = getLogger('Config')
        self.config = self._load_config(config)
        self.log.debug('Config loaded')

    def _load_config(self, config):
        try:
            return safe_load(file(config))
        except Exception, e:
            self.log.critical(e)
            print ''
            print '-' * 79
            print ' Malformed configuration file, common reasons:'
            print '-' * 79
            print ''
            print ' o Indentation error'
            print ' o Missing : from end of the line'
            print ' o Non ASCII characters (use UTF8)'
            print " o If text contains any of :[]{}% characters it must be single-quoted ('')"
            lines = 0
            if e.problem is not None:
                print ' Reason: %s' % e.problem
                if e.problem == 'mapping values are not allowed here':
                    print ' ----> MOST LIKELY REASON: Missing : from end of the line!'
            if e.context_mark is not None:
                print ' Check configuration near line %s, column %s' % (e.context_mark.line, e.context_mark.column)
                lines += 1
            if e.problem_mark is not None:
                print ' Check configuration near line %s, column %s' % (e.problem_mark.line, e.problem_mark.column)
                lines += 1
            if lines:
                print ''
            if lines == 1:
                print ' Fault is almost always in this or previous line'
            if lines == 2:
                print 'Fault is almost always in one of these lines or previous ones'
            exit(1)

