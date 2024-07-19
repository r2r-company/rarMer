import win32serviceutil
import win32service
import win32event
import subprocess

class TaskNotifierService(win32serviceutil.ServiceFramework):
    _svc_name_ = "TaskNotifierService"
    _svc_display_name_ = "Служба для сповіщення про нові завдання"
    _svc_description_ = "Ця служба надсилає сповіщення про нові завдання на сервер Django."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.process = None

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        if self.process:
            self.process.terminate()
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        self.process = subprocess.Popen(["python", "task_notifier.py"])
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(TaskNotifierService)
