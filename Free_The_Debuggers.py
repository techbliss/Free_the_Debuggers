import sys
import idaapi
import idc


class Freesome(idaapi.plugin_t):
    flags = idaapi.PLUGIN_PROC
    comment = ""

    help = ""
    wanted_name = "Free the Debugger"
    wanted_hotkey = "Alt-F6"

    def init(self):
        idaapi.msg("Free the Debugger is found. \n")
        return idaapi.PLUGIN_OK

    def run(self, arg):
        idaapi.msg("run() called with %d!\n" % arg)

    def term(self):
        idaapi.msg("")


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
    idaapi.load_and_run_plugin("epoc_user", 0)
    idc.LoadDebugger("gdb", 1)

	
def PLUGIN_ENTRY():
	return Freesome()

print "Finally We Are Free At Last"
