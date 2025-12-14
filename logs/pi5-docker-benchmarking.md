# Raspberry Pi 5 Docker Benchmarking

**Date:** December 13, 2025
**Purpose:** Baseline benchmarks for comparison with Pi 500 (16GB RAM, 256GB NVMe)

## System Information

| Spec | Value |
|------|-------|
| Model | Raspberry Pi 5 Model B Rev 1.0 |
| RAM | 4GB |
| Storage | 119.3GB SD Card (mmcblk0) |
| Kernel | 6.12.47+rpt-rpi-2712 (aarch64) |
| OS | Debian Bookworm |

## Storage Layout

```
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
mmcblk0     179:0    0 119.3G  0 disk
├─mmcblk0p1 179:1    0   512M  0 part /boot/firmware
└─mmcblk0p2 179:2    0 118.7G  0 part /
```

## Benchmark Results

### Docker Alpine Startup Time

Running `docker run alpine echo "Hello World!"`:

| Run | Time |
|-----|------|
| 1 | 2.021s |
| 2 | 1.726s |
| 3 | ~1.7s (estimated) |
| **Average** | **~1.8s** |

### SD Card Read Speed

```
dd if=/dev/mmcblk0 of=/dev/null bs=4M count=50
209715200 bytes (210 MB, 200 MiB) copied, 5.54416 s, 37.8 MB/s
```

**Sequential read speed: ~37.8 MB/s**

### Memory

```
               total        used        free      shared  buff/cache   available
Mem:           4.0Gi       2.2Gi       323Mi       222Mi       1.8Gi       1.7Gi
Swap:          511Mi       424Mi        87Mi
```

### WebGL Aquarium (GPU Benchmark)

**URL:** https://webglsamples.org/aquarium/aquarium.html

| Fish Count | Browser | FPS | Notes |
|------------|---------|-----|-------|
| 100 | Chromium | 60 | Steady, no dropouts |
| 500 (default) | Chromium | 60 | Some dropouts |
| 1000 | Chromium | 40-60 | Variable depending on other activity |
| 5000 | Chromium | ~20 | Average |

## Expected Pi 500 Improvements

| Metric | Pi 5 (SD) | Pi 500 (NVMe) | Expected Improvement |
|--------|-----------|---------------|---------------------|
| Docker startup | ~1.8s | ~0.5s | 3-4x faster |
| Storage read | ~38 MB/s | ~400+ MB/s | 10x+ faster |
| RAM | 4GB | 16GB | 4x more |

---

## Session Log

### Installing Docker on Raspberry Pi

The easiest method is using the official convenience script:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

After installation, add your user to the docker group to run without sudo:

```bash
sudo usermod -aG docker $USER
```

Log out and back in for the group change to take effect, then verify:

```bash
docker --version
docker run hello-world
```

### Running Alpine in Docker

**Interactive shell (most common):**
```bash
docker run -it alpine
```

**Run a specific command:**
```bash
docker run alpine echo "Hello from Alpine"
```

**Run in background (detached):**
```bash
docker run -d --name my-alpine alpine sleep infinity
```

Then attach to it later:
```bash
docker exec -it my-alpine sh
```

### Timing Docker Commands

```bash
time docker run alpine echo "Hello World!"
```

For accurate timing (excluding image download):
```bash
docker pull alpine
time docker run alpine echo "Hello World!"
```

### Fixing Docker Permission Denied

Add your user to the `docker` group:

```bash
sudo usermod -aG docker $USER
```

Then log out and back in, or apply immediately:

```bash
newgrp docker
```

---

## Notes

- Pi 5 with SD card shows typical ~1.7-2s Docker container startup time
- This is expected for SD card storage
- NVMe upgrade would significantly improve I/O-bound operations
- Pi 500 comparison to be done after Christmas setup
