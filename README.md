# ⚡ Vortex Pulse // Cyberpunk System Telemetry HUD

> **Ultra-Lightweight, Real-Time Hardware & System Monitor with Zero External Dependencies!**

Built directly with Python's standard library and native Win32 `kernel32.dll` system calls (`GetSystemTimes`, `GlobalMemoryStatusEx`, `GetSystemInfo`), rendering smooth 60 FPS oscilloscope graphs using Tkinter Canvas.

---

## 🌟 Key Features
- **Zero Third-Party Dependencies**: No `psutil`, no heavy libraries. Uses direct Win32 C-struct bindings.
- **Microsecond Latency**: Reads kernel user/idle slice ticks with zero lag.
- **Cyberpunk HUD Visuals**:
  - Live animated dual-channel oscilloscope (CPU Trace in Cyan, RAM Load in Sky Blue).
  - High-contrast telemetry cards with warning thresholds.
  - One-click Discord community access to claim the **`💎 First 100 Badge`**.
- **Instant Launcher**: Just double-click `START_PULSE.bat`.

---

## 🚀 Quick Start
```bash
# Double-click launcher:
START_PULSE.bat

# Or run via terminal:
python pulse.py
```

---

## 💬 Community
Join the Vortex Discord server:
👉 **[discord.gg/QtyBucygQ6](https://discord.gg/QtyBucygQ6)**
