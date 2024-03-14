$t = "$env:USERPROFILE\.local\bin\poetry"
& $t install
& $t run build_windows_cli

Copy-Item -Path "toolbox\*.bat" -Destination "dist\toolbox" -Recurse -Force
