$THEMES_PATH = (Join-Path $env:GITHUB pelican-themes)

Get-ChildItem -Directory $THEMES_PATH | ForEach-Object {
    Write-Output $_.Name
    pelican content -o output -e SITENAME="`"$($_.Name)`"" -t $_.FullName
    $wshell = New-Object -ComObject wscript.shell
    if ($wshell.AppActivate('Firefox')) {
        # Start-Sleep 1
        $wshell.SendKeys('{F5}')
    }
    # $wshell.AppActivate('Visual Studio Code')
    # $wshell = New-Object -ComObject Wscript.Shell
    # $wshell.Popup("Press a button for file: $($_.Name)", 0, 'Done', 0x1)
    # Add-Type -AssemblyName PresentationFramework
    # [System.Windows.MessageBox]::Show("$($_.Name): Press OK to continue")
    Read-Host 'Press Enter to continue'

}