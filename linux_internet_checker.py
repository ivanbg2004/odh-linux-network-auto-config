import platform
import subprocess
import os
import random
import argparse
import logging

# Define constants
ODH_BRAND = "Oblivion Development & Hosting (ODH)"
ODH_DISCLAIMER = "[ODH: Direct IP change is a placeholder - use VPN/Tor for privacy!]"

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_linux_distro():
    """Detects the Linux distribution."""
    try:
        return platform.linux_distribution()[0].lower()
    except:
        try:
            with open('/etc/os-release', 'r') as f:
                os_info = {}
                for line in f:
                    if '=' in line:
                        key, value = line.strip().split('=', 1)
                        key = key.strip()
                        value = value.strip().strip('"')
                        os_info[key] = value
                return os_info.get('ID', '').lower()
        except FileNotFoundError:
            return "unknown"

def get_package_manager(distro):
    """Identifies the package manager based on the distribution."""
    if "ubuntu" in distro or "debian" in distro or "popos" in distro or "linuxmint" in distro:
        return "apt-get"
    elif "fedora" in distro or "red hat" in distro or "centos" in distro or "rocky" in distro or "almalinux" in distro:
        return "dnf"
    elif "arch" in distro or "manjaro" in distro or "endeavouros" in distro:
        if subprocess.call(["which", "yay"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
            return "yay"
        else:
            return "pacman"
    elif "opensuse" in distro or "suse" in distro:
        return "zypper"
    elif "gentoo" in distro:
        return "emerge"
    elif "slackware" in distro:
        return "pkgtool"
    else:
        return None

def check_internet_connectivity(host="8.8.8.8", timeout=3):
    """Checks internet connectivity by pinging a host."""
    try:
        subprocess.check_call(["ping", "-c", "1", "-W", str(timeout), host],
                              stdout=subprocess.DEVNULL,
                              stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def install_package(package_manager, package):
    """Installs a package using the identified package manager."""
    try:
        if package_manager == "apt-get":
            subprocess.check_call(["sudo", "apt-get", "install", "-y", package])
        elif package_manager == "dnf":
            subprocess.check_call(["sudo", "dnf", "install", "-y", package])
        elif package_manager == "pacman":
            subprocess.check_call(["sudo", "pacman", "-S", "--noconfirm", package])
        elif package_manager == "yay":
            subprocess.check_call(["yay", "-S", "--noconfirm", package])
        elif package_manager == "zypper":
            subprocess.check_call(["sudo", "zypper", "--non-interactive", "install", package])
        elif package_manager == "emerge":
            subprocess.check_call(["sudo", "emerge", "--ask", package])
        elif package_manager == "pkgtool":
            subprocess.check_call(["sudo", "pkgtool", package])
        else:
            logging.error(f"Unsupported package manager: {package_manager}")
            return False
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Error installing package: {e}")
        return False

def flush_dns():
    """Flushes the DNS cache."""
    distro = get_linux_distro()
    try:
        if "ubuntu" in distro or "debian" in distro or "popos" in distro or "linuxmint" in distro:
            subprocess.check_call(["sudo", "systemd-resolve", "--flush-caches"])
            subprocess.check_call(["sudo", "resolvectl", "flush-caches"])
        elif "fedora" in distro or "red hat" in distro or "centos" in distro or "rocky" in distro or "almalinux" in distro:
            subprocess.check_call(["sudo", "systemd-resolve", "--flush-caches"])
        elif "arch" in distro or "manjaro" in distro or "endeavouros" in distro:
            subprocess.check_call(["sudo", "systemd-resolve", "--flush-caches"])
        elif "opensuse" in distro or "suse" in distro:
            subprocess.check_call(["sudo", "systemd-resolve", "--flush-caches"])
        elif "gentoo" in distro:
            logging.warning("DNS Flushing on Gentoo requires manual configuration. Consider restarting the network service.")
            return False
        elif "slackware" in distro:
            logging.warning("DNS Flushing on Slackware requires manual configuration. Consider restarting the network service.")
            return False
        else:
            logging.error("Unsupported distribution for DNS flushing. Please flush manually.")
            return False
        logging.info("DNS cache flushed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Error flushing DNS cache: {e}")
        return False

def change_ip_address():
    """
    WARNING: This function is highly dependent on the network configuration and distribution.
    It's generally NOT recommended to change the IP address directly.
    Using a VPN or Tor is a safer and more reliable way to protect your privacy.
    This is a placeholder - it needs significant customization.
    """
    logging.warning("Changing IP address directly is risky and not recommended.")
    logging.warning("Consider using a VPN or Tor for privacy.")
    logging.info("This functionality is not yet implemented. You'll need to research the appropriate commands for your distribution and network setup.")

def main():
    parser = argparse.ArgumentParser(description='ODH Linux Network Tool')
    parser.add_argument('--flush-dns', action='store_true', help='Flush DNS cache')
    parser.add_argument('--change-ip', action='store_true', help='Change IP address (NOT RECOMMENDED)')
    parser.add_argument('--install-curl', action='store_true', help='Install curl')
    args = parser.parse_args()

    print(f"\n--- {ODH_BRAND} Linux Network Tool ---")
    distro = get_linux_distro()
    logging.info(f"Detected Linux distribution: {distro}")
    package_manager = get_package_manager(distro)
    if not package_manager:
        logging.error("Unsupported distribution. Please install packages manually.")
        return

    logging.info(f"Detected package manager: {package_manager}")

    if check_internet_connectivity():
        logging.info("Internet connection is working.")
    else:
        logging.error("No internet connection detected.")

    if args.install_curl:
        if install_package(package_manager, "curl"):
            logging.info("Successfully installed curl. Please try connecting to the internet.")
        else:
            logging.error("Failed to install curl. Please check your internet connection and package manager configuration.")

    if args.flush_dns:
        flush_dns()

    if args.change_ip:
        change_ip_address()

    print(f"\n--- {ODH_BRAND} - All Done! ---")
    print(ODH_DISCLAIMER)

if __name__ == "__main__":
    main()
