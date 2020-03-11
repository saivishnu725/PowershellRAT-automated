import os, sys
import subprocess

def cmd_takeScreenshot():
	process=subprocess.Popen(["powershell","C:\Python36\Shoot.ps1"], shell=False);

def cmd_sendMail():
	process=subprocess.Popen(["powershell","C:\Python36\Mail.ps1"], shell=False);

def cmd_deleteScreenShot():
	process=subprocess.Popen(["powershell","Remove-Item $env:USERPROFILE\Documents\ScreenShot\*.*"], shell=False);

cmds = {
	"1" : cmd_takeScreenshot,
	"2" : cmd_sendMail,
	"3" : cmd_deleteScreenShot,
	"4" : lambda: sys.exit(0)
}

def main():
	try:
		cmds.get("1")()
		cmds.get("2")()
		cmds.get("3")()
		cmds.get("4")()
	except KeyboardInterrupt:
		print ('[!] Ctrl + C detected\n[!] Exiting')
		sys.exit(0)
	except EOFError:
		print ('[!] Ctrl + D detected\n[!] Exiting')
		sys.exit(0)

if __name__ == "__main__":
	main()
