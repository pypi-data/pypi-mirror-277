import os
import subprocess
import platform
import shutil
import psutil

class DrivePy:
    @staticmethod
    def list_usb_drives():
        system = platform.system()
        if system == 'Linux':
            try:
                import pyudev
                context = pyudev.Context()
                drives = []
                for device in context.list_devices(subsystem='block', DEVTYPE='disk'):
                    if 'ID_BUS' in device and device['ID_BUS'] == 'usb':
                        drives.append(device.device_node)
                return drives
            except ImportError:
                return []
        elif system == 'Windows':
            drives = []
            partitions = psutil.disk_partitions()
            for partition in partitions:
                if 'removable' in partition.opts:
                    drives.append(partition.device)
            return drives
        elif system == 'Darwin':  # macOS
            try:
                drives = []
                disks = subprocess.check_output(['diskutil', 'list']).decode('utf-8').split('\n')
                for disk in disks:
                    if '/dev/disk' in disk and 'external' in disk.lower():
                        drives.append(disk.strip())
                return drives
            except subprocess.CalledProcessError:
                return []
        else:
            raise NotImplementedError(f"Unsupported platform: {system}")

    @staticmethod
    def unmount_drive(drive):
        system = platform.system()
        if system == 'Linux':
            try:
                subprocess.run(['umount', drive], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError:
                pass
        elif system == 'Windows':
            try:
                diskpart_script = f"""
                select volume {drive.strip(':')}
                remove
                """
                subprocess.run(['diskpart', '/s', diskpart_script.strip()], shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError:
                pass
        elif system == 'Darwin':  # macOS
            try:
                subprocess.run(['diskutil', 'unmountDisk', drive], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError:
                pass

    @staticmethod
    def flash_iso_to_usb(iso_path, usb_drive):
        system = platform.system()
        if system == 'Linux':
            try:
                with open(iso_path, 'rb') as iso_file:
                    with open(usb_drive, 'wb') as usb:
                        usb.write(iso_file.read())
            except IOError:
                pass
        elif system == 'Windows':
            try:
                subprocess.run(['cmd', '/c', f'xcopy /s {iso_path} {usb_drive}'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError:
                pass
        elif system == 'Darwin':  # macOS
            try:
                subprocess.run(['dd', f'if={iso_path}', f'of={usb_drive}', 'bs=1m'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError:
                pass

    @staticmethod
    def flash_iso(iso_path, usb_drive):
        DrivePy.unmount_drive(usb_drive)
        DrivePy.flash_iso_to_usb(iso_path, usb_drive)

    @staticmethod
    def make_bootable(usb_drive):
        system = platform.system()
        if system == 'Linux':
            try:
                subprocess.run(['sudo', 'syslinux', '-i', usb_drive], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError:
                pass
        elif system == 'Windows':
            try:
                shutil.copy('path/to/bootloader_files/*', usb_drive)  # Copy bootloader files to USB drive
            except FileNotFoundError:
                pass
        elif system == 'Darwin':  # macOS
            try:
                subprocess.run(['sudo', 'bless', '--folder', f'{usb_drive}/', '--bootinfo', '--bootefi'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError:
                pass

    @staticmethod
    def is_bootable(usb_drive):
        system = platform.system()
        if system == 'Linux':
            # Check if the USB drive has a bootable MBR (Master Boot Record)
            try:
                output = subprocess.check_output(['file', '-sL', usb_drive]).decode('utf-8')
                return 'boot sector' in output.lower()
            except subprocess.CalledProcessError:
                return False
        elif system == 'Windows':
            # Check if the USB drive has boot files
            boot_files = ['bootmgr', 'boot.ini', 'boot', 'ntldr']
            return all(os.path.exists(os.path.join(usb_drive, file)) for file in boot_files)
        elif system == 'Darwin':  # macOS
                        # Check if the USB drive is bootable on macOS by looking for EFI boot files
            efi_boot_files = ['EFI', 'boot']
            return all(os.path.exists(os.path.join(usb_drive, file)) for file in efi_boot_files)
        else:
            return False  # Unsupported platform

    @staticmethod
    def verify_bootability(usb_drive):
        if DrivePy.is_bootable(usb_drive):
            print(f"The USB drive ({usb_drive}) is bootable.")
        else:
            print(f"The USB drive ({usb_drive}) is not bootable.")

    @staticmethod
    def main():
        usb_drives = DrivePy.list_usb_drives()
        if not usb_drives:
            print("No USB drives detected.")
        else:
            print("Available USB drives:")
            for idx, drive in enumerate(usb_drives, 1):
                print(f"{idx}: {drive}")

if __name__ == "__main__":
    DrivePy.main()
