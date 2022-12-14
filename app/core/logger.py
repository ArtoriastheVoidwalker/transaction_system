from datetime import datetime
from termcolor import colored


class Logger:

    @property
    def current_time(self):
        return datetime.strftime(datetime.now(), '%d.%m.%y %H:%M:%S')

    def info(self, message):
        print(colored('{0} [INFO] {1}'.format(self.current_time, message), 'cyan'))

    def warning(self, message):
        print(colored('{0} [WARN] {1}'.format(self.current_time, message), 'yellow'))

    def success(self, message):
        print(colored('{0} [OK] {1}'.format(self.current_time, message), 'green'))


    def error(self, message):
        print(colored('{0} [ERR] {1}'.format(self.current_time, message), 'red'))


logger = Logger()
