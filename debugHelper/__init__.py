import builtins as __builtin__

from time import monotonic



import sys


advanced_enable = "3.7" < sys.version 



class DebugPrinter():
    enabled = False
    indentDepth = 0 
    indentChar = ""
    def __init__(self, leftCol):
        super(DebugPrinter, self).__init__()
        self.leftCol = leftCol
        
    def indention(self):
        if self.enabled:
            return self.indentChar * self.indentDepth
        return ''
        
    def indent(self):
        self.indentDepth += 1
    
    def dedent(self):
        self.indentDepth += -1
        if self.indentDepth < 0:
            self.indentDepth = 0
        
    def message(self, *args, **kwargs):
        leftColumnStr = ''
        if self.enabled:
            leftColumnStr = self.leftCol
            if callable(self.leftCol):
                leftColumnStr = self.leftCol()
        return leftColumnStr + " ".join(args)
        
    def print(self, *args, **kwargs):
        return __builtin__.print(self.message(*args, **kwargs))

    def debugAnounce(self, fn):
        def inner(*args, **kwargs):
            if self.enabled:
                fn_name = ''
                try:
                    fn_name = "=> "+fn.__name__
                except:
                    fn_name = "-> "+ re.sub( r".*function (.*) at.*" , r"\1", str(fn) )
                
                self.print(">", str(fn_name))
                self.indent()
                self.print(f"{args=}, {kwargs=}")
            r = fn(*args, **kwargs)
            if self.enabled:
                self.dedent()
                self.print("<", str(fn))
            return r
        return inner

def now():
    return monotonic()

thisDebugPrinter = DebugPrinter(lambda: '[ ' + str(now()) + ' ]' )
print = thisDebugPrinter.print
debugAnounce = thisDebugPrinter.debugAnounce

