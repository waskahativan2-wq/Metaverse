# Persistent USB Binding for VM Hotplug (udev + systemd + libvirt)

Use fixed USB identifiers so a specific host USB device is automatically attached to (and detached from) a VM when plugged in or removed.

## 1) Find the USB vendor/product IDs

Connect the drive and run:

```bash
lsusb
```

Look for the target device line:

```text
ID 1234:5678
```

- `1234` = `idVendor`
- `5678` = `idProduct`

## 2) Create a persistent udev rule

Create a custom rules file:

```bash
sudo nano /etc/udev/rules.d/99-retro-usb.rules
```

Add:

```udev
ACTION=="add|remove", SUBSYSTEM=="usb", ATTR{idVendor}=="1234", ATTR{idProduct}=="5678", TAG+="systemd", ENV{SYSTEMD_WANTS}+="vm-usb-bind@%E{ACTION}.service"
```

Replace `1234` and `5678` with your real IDs.

Reload and trigger rules:

```bash
sudo udevadm control --reload
sudo udevadm trigger
```

## 3) Create the hotplug script

Create:

```bash
sudo nano /usr/local/sbin/vm-usb-bind.sh
```

Script:

```bash
#!/usr/bin/env bash
set -euo pipefail

ACTION="${1:-}"
VM_NAME="your-vm-name" # replace with your libvirt domain name

if [[ "${ACTION}" == "add" ]]; then
  CMD="attach-device"
else
  CMD="detach-device"
fi

virsh "${CMD}" "${VM_NAME}" /dev/stdin <<'EOF'
<hostdev mode='subsystem' type='usb' managed='yes'>
  <source>
    <vendor id='0x1234'/>
    <product id='0x5678'/>
  </source>
</hostdev>
EOF
```

Set executable:

```bash
sudo chmod +x /usr/local/sbin/vm-usb-bind.sh
```

## 4) Create the systemd unit template

Create:

```bash
sudo nano /etc/systemd/system/vm-usb-bind@.service
```

Content:

```ini
[Unit]
Description=Attach/detach USB device to VM on udev event (%i)
After=libvirtd.service

[Service]
Type=oneshot
ExecStart=/usr/local/sbin/vm-usb-bind.sh %i
```

Reload systemd:

```bash
sudo systemctl daemon-reload
```

## Notes

- Update `VM_NAME` and the USB IDs in both the udev rule and XML snippet.
- Verify the VM is running before attach events.
- If using a non-root libvirt URI/session, adjust `virsh` context accordingly.
