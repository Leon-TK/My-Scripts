#SPDX-FileCopyrightText: � 2022 Leonid Tkachenko leon24rus@gmail.com
#SPDX-License-Identifier: MIT License

#WIP
#Script for fast launch of Zomboid server through ssh

from SshWithShell.sshWithShell import SshWithShell

sshSession = SshWithShell()
sshSession.Init()
sshSession.Connect("leonserver.loc")
sshSession.SendMsg("$path = $Env:ZOMBOIDSERVER")
sshSession.ChangeDir("$path")
sshSession.Exec("StartServer64.bat", '', ".\\")
