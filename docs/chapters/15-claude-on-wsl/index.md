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

## Overview: Why Use WSL Instead of PowerShell

This section is a complete, step-by-step guide to running Claude Code inside
the Windows Subsystem for Linux (WSL). It assumes you already have **Claude
Desktop** installed on Windows — Claude Desktop stays exactly where it is.
WSL only adds a real Linux environment on the same machine so that
**Claude Code** (the command-line agent) can run in the shell that almost
all of our skills, scripts, and screen-capture tools were written and tested
against.

!!! tip
    Claude Desktop and Claude Code are two different products. Claude
    Desktop is the chat application. Claude Code is the terminal-based
    coding agent. You will keep using Claude Desktop on Windows for chat,
    and you will open a WSL terminal whenever you want to run Claude Code
    against this repository.

## Step 1: Confirm Your System Can Run WSL2

Before installing anything, confirm three things on the Windows side:

1. **Windows version** — Windows 10 version 2004 (Build 19041) or later, or
   any version of Windows 11. Check with:

    ```powershell
    winver
    ```

2. **Virtualization is enabled in the BIOS/UEFI** — WSL2 runs a real
   lightweight VM (via Hyper-V/Virtual Machine Platform), so hardware
   virtualization must be turned on. Check in Task Manager:

    - Open Task Manager → **Performance** tab → **CPU**
    - Look for **Virtualization: Enabled**

    If it says **Disabled**, reboot into your BIOS/UEFI setup screen (often
    `F2`, `F10`, `Del`, or `Esc` at boot) and enable **Intel VT-x**,
    **AMD-V**, or **SVM Mode**, depending on your CPU vendor.

3. **Total system RAM is at least 8GB** — WSL2's default memory limit is
   half of your host RAM (or 8GB, whichever is smaller), so an 8GB host will
   only give the VM about 4GB unless you raise the limit explicitly (see
   Step 4). Check your installed RAM in **Settings → System → About**, under
   *Installed RAM*.

!!! warning
    If your machine has less than 8GB of physical RAM, you can still run
    WSL, but you will not be able to give the VM a full 8GB (Step 4).
    Claude Code itself is lightweight, but builds, `mkdocs serve`, and
    browser-based screenshot tools are memory-hungry — 8GB dedicated to the
    VM is the practical minimum for this repository.

## Step 2: Install WSL2

Open **PowerShell as Administrator** (right-click the Start menu →
*Terminal (Admin)* or *Windows PowerShell (Admin)*) and run:

```powershell
wsl --install
```

This single command enables the required Windows features (`Virtual
Machine Platform` and `Windows Subsystem for Linux`), downloads the WSL2
Linux kernel, sets WSL2 as the default version, and installs **Ubuntu** as
the default distribution.

Restart the computer when prompted:

```powershell
Restart-Computer
```

After the restart, an Ubuntu terminal window will open automatically the
first time and ask you to create a UNIX username and password. This is a
**Linux** account, separate from your Windows login — pick anything you
like and remember the password, since it is required for `sudo` commands.

!!! note "Already have WSL1 installed?"
    If `wsl --install` reports that WSL is already installed, instead run:

    ```powershell
    wsl --install -d Ubuntu
    wsl --set-default-version 2
    wsl --set-version Ubuntu 2
    ```

## Step 3: Verify the Installation

Back in PowerShell, list your installed distributions and confirm the
**VERSION** column reads `2`:

```powershell
wsl -l -v
```

Expected output:

```
  NAME      STATE           VERSION
* Ubuntu    Running         2
```

If it shows `1` instead of `2`, upgrade it:

```powershell
wsl --set-version Ubuntu 2
```

You can also confirm the kernel and distro details from inside the Linux
shell:

```bash
uname -a
lsb_release -a
```

## Step 4: Guarantee the WSL2 VM Has at Least 8GB of RAM

WSL2's memory limit is controlled by a `.wslconfig` file that lives in your
**Windows** user profile (not inside the Linux filesystem).

1. In PowerShell, open (or create) the file:

    ```powershell
    notepad "$env:USERPROFILE\.wslconfig"
    ```

2. Add the following, adjusting `memory` to no less than `8GB` (leave some
   RAM for Windows itself — e.g. on a 16GB machine, 8–10GB for WSL is
   reasonable):

    ```ini
    [wsl2]
    memory=8GB
    processors=4
    swap=4GB
    localhostForwarding=true
    ```

3. Save the file and restart WSL so the new limit takes effect:

    ```powershell
    wsl --shutdown
    ```

4. Reopen your Ubuntu terminal and verify the VM actually sees 8GB:

    ```bash
    free -h
    ```

    The `total` column on the `Mem:` row should read `8.0Gi` or higher. If
    it doesn't, double check the `.wslconfig` path and that you ran
    `wsl --shutdown` (a plain terminal close is not enough — the whole VM
    must stop and restart).

## Step 5: Update Ubuntu and Install Prerequisites

Inside the WSL Ubuntu shell:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl git build-essential
```

## Step 6: Install Claude Code Inside WSL

From inside the Ubuntu shell (not PowerShell), run the native Linux
installer:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

!!! warning
    As noted above, Anthropic has deprecated the `npm`/Node-based
    installation method. Always use the native installer script shown
    above, and always run it **inside the Linux shell**, not PowerShell —
    a Windows-side install will not be visible to WSL, and vice versa.

Restart your terminal, then confirm it installed correctly:

```bash
claude --version
```

Navigate to this repository (Windows drives are mounted under `/mnt/`) and
launch Claude Code:

```bash
cd /mnt/c/Users/<your-windows-username>/Documents/ws/claude-skills
claude
```

!!! tip "Keep the repo inside the Linux filesystem for speed"
    File I/O across the `/mnt/c/...` boundary is noticeably slower than
    native Linux disk access. If you do heavy work in this repo, consider
    cloning it directly into your Linux home directory instead
    (`~/ws/claude-skills`) and accessing it from Windows tools (like VS
    Code's Remote-WSL extension) rather than the other way around.

### Pros of WSL

- This is the environment almost every Claude Code user runs, so it is the
  best-tested path.
- The screen-capture and browser-automation shell scripts used by our
  skills work correctly here, unlike on PowerShell.
- Standard Unix tooling (`bash`, `grep`, `sed`, `curl`, Python virtualenvs)
  behaves exactly like it does in our documentation and skills.

### Cons of WSL

- It cannot place icons directly on the Windows desktop or launch Windows
  GUI apps as easily as a native PowerShell install can.
- Requires an extra one-time setup step (this guide) that PowerShell users
  skip.

## Useful Prompts for Claude Code Running Inside WSL

Once `claude` is running inside your WSL Ubuntu shell, it can sometimes
default to habits that make more sense on native Linux/macOS than on a
Windows host, or vice versa. The prompts below help keep it oriented.
Give the first one early in any new session:

- "Claude, remember that you are running on a WSL system and that Unix
  shell commands are preferred over PowerShell commands."
- "Confirm you are running inside WSL2 and not native Windows before making
  any environment assumptions."
- "This project's files live at `/mnt/c/Users/<username>/Documents/ws/claude-skills` — always use that Linux-style path, not a Windows path like `C:\Users\...`."
- "When you need to open a URL or screenshot a local MicroSim, use the WSL
  browser/screen-capture tooling described in this repo's skills, not a
  Windows-only tool."
- "Check `free -h` and `df -h` before starting a memory- or disk-heavy task
  like `mkdocs build` or a screenshot batch job, and warn me if resources
  look low."
- "If a command fails with something like `xdg-open: command not found` or
  a display error, that usually means it's trying to open a GUI window —
  ask me how I want to view the result instead of guessing."
- "Never call a PowerShell-only command (like `Enable-WindowsOptionalFeature`
  or anything with a `.ps1` extension) from inside this WSL session."

!!! note
    These prompts are especially useful the first time you open a new
    WSL terminal in a session, since Claude Code has no memory of earlier
    sessions unless you have saved these preferences to a project or
    global `CLAUDE.md` file.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `wsl --install` does nothing or errors | Virtualization disabled in BIOS | Re-check Step 1, enable VT-x/AMD-V, reboot |
| `wsl -l -v` shows VERSION `1` | Distro was installed before WSL2 was set as default | `wsl --set-version Ubuntu 2` |
| `free -h` shows less than 8GB after editing `.wslconfig` | VM wasn't fully restarted | Run `wsl --shutdown` in PowerShell, then reopen Ubuntu |
| `claude: command not found` | Installer was run in PowerShell instead of the Linux shell, or shell wasn't restarted | Re-run the installer inside WSL, then open a new terminal |
| Screenshots or browser tools silently fail | Session is actually a PowerShell tab, not WSL | Check the terminal prompt/title bar; open a fresh WSL tab |
| Very slow `mkdocs serve` or `git status` | Repo is stored under `/mnt/c/...` and accessed across the Windows/Linux boundary | Clone the repo into the Linux filesystem (e.g. `~/ws/claude-skills`) instead |
