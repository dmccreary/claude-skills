# Installing Claude on Windows Systems for Linux (WSL)

It is often difficult to get the Windows Systems for Linux (WSL) working.
You much make sure your computer support the Hyper-V options.
On older systems this could only be set in the BIOS during boot.
You can install Claude on the PowerShell and then have Claude
walk you through the steps of installing WSL.

[Claude Code Documentation](https://code.claude.com/docs/en/setup#platform-specific-setup)

## PowerShell

```shell
irm https://claude.ai/install.ps1 | iex
```

!!! warning
    Anthropic has deprecated the node installation.  Only
    use the native installer.

Make sure the Hypervisor is turned on
You will find this in the Windows Control Panel

```powershell
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
```

### Pros of the Powershell

It can talk directly to your desktop and install icons on your desktop that will start the mkdocs server.

### Cons of the Powershell

Claude Code on the Powershell is very under-tested.  99% of Claude Code users
use Linux, so, that is always the preferred method.

### Launching the Browser

Our skill use a screen capture shell script to get screen images.
These tools will not work on the PowerShell.
