import os
import subprocess

class ShellContext:
    def run(script: 'AddEnvSystemScript'):
        pass
class PowershellContext:
    def run(script):
        args = ['powershell'] + script.get().split
        subprocess.call(args)
class BashContext:
    def run(script):
        pass

class AddEnvSystemScript:
    def get() -> str:
        pass
class AddEnvPowershellScript(AddEnvSystemScript):
    def get() -> str:
        pass
class AddEnvBashScript(AddEnvSystemScript):
    def get() -> str:
        pass

shellContext: ShellContext = PowershellContext()
shellContext.run(AddEnvPowershellScript())