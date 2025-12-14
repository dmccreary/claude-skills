# Setting up Claude on a Raspberry Pi

## Installing node



```sh
# Remove any old Node.js installations (optional)
sudo apt remove nodejs npm

# Install Node.js 20.x (LTS as of 2025)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# Verify installation
node --version  # Should show v20.x.x
npm --version   # Should show 10.x.x or higher
```

## Sample Node Installation Transcript

```
Reading state information... Done
4 packages can be upgraded. Run 'apt list --upgradable' to see them.
2025-12-11 13:17:19 - Repository configured successfully.
2025-12-11 13:17:19 - To install Node.js, run: apt install nodejs -y
2025-12-11 13:17:19 - You can use N|solid Runtime as a node.js alternative
2025-12-11 13:17:19 - To install N|solid Runtime, run: apt install nsolid -y 

Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  libbasicusageenvironment1 libc++1-16 libc++abi1-16 libcamera0.3
  libgroupsock8 liblivemedia77 libunwind-16 libwlroots12
  linux-headers-6.6.51+rpt-common-rpi linux-headers-6.6.51+rpt-rpi-2712
  linux-headers-6.6.51+rpt-rpi-v8 linux-image-6.6.51+rpt-rpi-2712
  linux-image-6.6.51+rpt-rpi-v8 linux-kbuild-6.6.51+rpt python3-v4l2
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed:
  nodejs
0 upgraded, 1 newly installed, 0 to remove and 4 not upgraded.
Need to get 31.0 MB of archives.
After this operation, 197 MB of additional disk space will be used.
Get:1 https://deb.nodesource.com/node_20.x nodistro/main arm64 nodejs arm64 20.19.6-1nodesource1 [31.0 MB]
Fetched 31.0 MB in 11s (2,839 kB/s)                                            
Selecting previously unselected package nodejs.
(Reading database ... 171276 files and directories currently installed.)
Preparing to unpack .../nodejs_20.19.6-1nodesource1_arm64.deb ...
Unpacking nodejs (20.19.6-1nodesource1) ...
Setting up nodejs (20.19.6-1nodesource1) ...
Processing triggers for man-db (2.11.2-2) ...
v20.19.6
10.8.2
```

## Installing Conda

```

```

## Installing mkdocs

```
pip install mkdocs mkdocs-material[imaging] pymdown-extensions
```

## Customizing Terminals

```sh
sudo apt install wmctrl
```

We can then create a command that starts up our three development terminals:

1. One for Claude Code

```sh
#!/bin/bash

sleep 2

# Startup Terminal 1 with Claude Code at (0,50)
lxterminal -t "Claude Code" --loginshell -e /usr/bin/claude --dangeriously-skip-permissions --geometry=80x24 &
# The -e option format is gravity,x,y,width,height (in pixels). Use 0 for gravity (default).
sleep 0.5
wmctrl -r "Claude Code" -e 0,0,0,800,400

# Terminal starting in a specific directory
lxterminal --working-directory=/home/pi/projects &

# Terminal that runs a command
lxterminal -e "htop" &
```
## GitHub Settings

```sh
git config --global user.email "suejohnson@example.com"
git config --global user.name "Sue Johnson"
```

## Screen Capture Tool

```sh
sudo apt install grim slurp
```

```sh
grim -g "$(slurp)" screenshot.png
```

## Open

```sh
which open
/usr/bin/open
(base) dan@raspberrypi:~ $ ls -l /usr/bin/open
lrwxrwxrwx 1 root root 22 Apr 25  2021 /usr/bin/open -> /etc/alternatives/open
(base) dan@raspberrypi:~ $ ls -l /etc/alternatives/open
lrwxrwxrwx 1 root root 17 Apr 25  2021 /etc/alternatives/open -> /usr/bin/xdg-open
```