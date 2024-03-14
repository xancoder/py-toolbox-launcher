# py-toolbox-launcher

tool box collection execution wrapper

## Builds

the app is located in the `dist` folder later

### Windows

tested in an unattended virtualbox Windows 10 virtual machine installation

in a powershell at project folder use the following commands

```PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\scripts\setup_python.ps1
.\scripts\build_windows.ps1
```

### Linux

tested in an unattended virtualbox debian 12 virtual machine installation

in a shell at project folder use the following commands

```bash
chmod +x ./scripts/build_linux.sh 
./scripts/build_linux.sh
```
