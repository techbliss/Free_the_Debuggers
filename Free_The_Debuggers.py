import sys
import idaapi
from idaapi import *
import idc
from idc import  *

class plugin_t():

##'lets give this baby some debuggers'''
    idaapi.load_and_run_plugin("windbg_user.plw", 0)
    idaapi.load_and_run_plugin("armlinux_stub.plw", 0)
    idaapi.load_and_run_plugin("gdb_user.plw", 0)
    idaapi.load_and_run_plugin("linux_stub.plw", 0)
    idaapi.load_and_run_plugin("mac_stub.plw", 0)
    idaapi.load_and_run_plugin("win32_stub.plw", 0)
    idaapi.load_and_run_plugin("win32_user.plw", 0)
    idaapi.load_and_run_plugin("wince_stub.plw", 0)
    idaapi.load_and_run_plugin("bdescr.plw", 0)
    idaapi.load_and_run_plugin("fentanyl.py", 0)
    idaapi.load_and_run_plugin("epoc_user", 0)
    idaapi.load_and_run_plugin("deci3dbg.plw", 0)
    idaapi.load_and_run_plugin("deci3dbg.p64", 0)
    idc.LoadDebugger("gdb", 1)



# ----------------------------------------------------------------------
def Plugin_ENTRY():
  return plugin_t()

print "Finally We Are Free At Last"
