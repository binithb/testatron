# from src.jataayu.core import globals
__author__ = 'anupama'
# globals.init()



""" Jataayu
"""

import sys
import os
from string import Template
import traceback
import threading


# Insert any required lib
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
# sys.path.append(os.path.join(os.path.dirname(__file__), 'spec'))

def main(*args):
    noupdatecheck, debug_console, inpath = _parse_args(args)
    if len(args) > 3 or '--help' in args:
        print __doc__
        sys.exit()
    try:
        _run(inpath, not noupdatecheck, debug_console)
    except DataError, err:
        print str(err) + '\n\nUse --help to get usage information.'

def _parse_args(args):
    if not args:
        return False, False, None
    noupdatecheck = '--noupdatecheck' in args
    debug_console = '--debugconsole' in args
    inpath = args[-1] if args[-1] not in ['--noupdatecheck', '--debugconsole'] else None
    return noupdatecheck, debug_console, inpath

def _run(inpath=None, updatecheck=True, debug_console=False):
    try:
        from jataayu.application import Jataayu
    except ImportError:
        raise
    if inpath:
        inpath = unicode(inpath, sys.getfilesystemencoding())
    jataayu = Jataayu(inpath, updatecheck)
    _show_old_wxpython_warning_if_needed(jataayu.frame)
    if debug_console:
        _start_debug_console(jataayu)
    jataayu.MainLoop()

def _show_old_wxpython_warning_if_needed(parent=None):
    if wx.VERSION >= (2, 8, 12, 1):
        return
    title = 'Please upgrade your wxPython installation'
    message = ('Jataayu officially supports wxPython 2.8.12.1. '
               'Your current version is %s.\n\n'
               'Older wxPython versions are known to miss some features used by Jataayu. '
               'Notice also that wxPython 3.0 is not yet supported.\n\n'
               'wxPython 2.8.12.1 packages can be found from\n'
               'http://sourceforge.net/projects/wxpython/files/wxPython/2.8.12.1/.'
               % wx.VERSION_STRING)
    style = wx.ICON_EXCLAMATION
    if not parent:
        app = wx.PySimpleApp()
        parent = wx.Frame(None, size=(0,0))
    wx.MessageDialog(parent, message, title, style).ShowModal()

def _print_stacks():
    id2name = dict((th.ident, th.name) for th in threading.enumerate())
    for threadId, stack in sys._current_frames().items():
        print(id2name[threadId])
        traceback.print_stack(f=stack)

def _start_debug_console(jataayu):
    import code
    help_string = """\
Jataayu - access to the running application
print_stacks() - print current stack traces
"""
    console = code.InteractiveConsole(locals={'Jataayu':jataayu, 'print_stacks':_print_stacks})
    thread = threading.Thread(target=lambda: console.interact(help_string))
    thread.start()

if __name__ == '__main__':
    main(sys.argv[1:])

