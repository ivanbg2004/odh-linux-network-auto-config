# OD&H Linux Network Auto Config

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.6+-blue.svg)]()
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)]()

> _"Because if you're still wrestling with Windows for networking... well, there's a better way."_

**A comprehensive and automated network diagnostic and utility suite for Linux systems, brought to you by Oblivion Development & Hosting (OD&H).**

* * *

## 🧠 About

**OD&H Linux Network Auto Config** is an advanced, no-nonsense Python-based utility developed by **Oblivion Development & Hosting (OD&H)** to empower Linux users with streamlined, automated network troubleshooting and optimization.  Tired of endless manual debugging and cryptic error messages? This suite handles detection, diagnostics, and utility setup so you can spend less time troubleshooting and more time actually using your network.

* * *

## 🚀 Features at a Glance

✅ **Smart Distribution Detection** — Supports Ubuntu, Arch, Fedora, Gentoo, and everything in between.  If it's Linux, we probably support it.

✅ **Connectivity Verification** — Instantly checks if your internet connection is alive or dying.  No more wondering if it's *you* or *the network*.

✅ **DNS Cache Management** — Clears the DNS cache using distribution-specific methods.  Because sometimes, DNS just needs a little kick.

✅ **Automatic Dependency Installer** — Ensures key network tools are present (requires root). Say goodbye to dependency hell.

✅ **OD&H Branding** — Built with consistency and professionalism in mind. It’s so professional, it practically wears a suit.

⚠️ **IP Changing Placeholder** — Not implemented. Use a VPN or Tor, not amateur hacks that'll break everything.

* * *

## 🖥️ For Those Emerging From the Windows Wastes:

>  This tool is built for Linux, where **updates don't randomly decide to reboot your system in the middle of a critical task.**

>  If you're still on Windows, and your network problem *isn't* Windows, congratulations, you're a statistical anomaly! But seriously, consider:

*   **A Fresh Start:** Linux offers a stable and robust environment for networking.
*   **More Control:** Fine-tune your network settings without fighting cryptic GUIs.
*   **A Community of Support:** Countless resources and helpful users ready to assist.

> _Consider switching to Linux. We're not saying it's a miracle cure, but it might be the closest thing you get._

* * *

## 🛠️ Installation

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/ivanbg2004/odh-linux-network-auto-config
    cd odh-linux-network-auto-config
    ```

2.  **Execute Permissions:**

    ```bash
    chmod +x linux_internet_checker.py
    ```

3.  **Run (Root Required):**

    ```bash
    sudo ./linux_internet_checker.py
    ```

* * *

## 🧑‍💻 Usage

After running, the toolkit will:

1.  Detect your Linux distribution automatically.
2.  Identify the relevant package manager.
3.  Perform an initial internet connectivity check.
4.  Provide the following options:

    *   `dns`: Flush the DNS cache.
    *   `ip`: Attempt to change IP address (⚠️ **PLACEHOLDER - NOT RECOMMENDED** ⚠️).
    *   `Enter`: Skip and exit.

* * *

## ⚙️ Configuration

Currently, configuration is managed within the script. Future releases may offer a separate `config.py` for customizable settings:

*   **Ping Target:** Customize the hostname/IP used for connectivity testing.
*   **Timeout Values:** Adjust ping timeout duration.
*   **Package List:** Specify packages for automated installation.

## ⚠️ Important Considerations

*   **Root Access:** This script *requires* root privileges. Always exercise caution.
*   **IP Address Handling:** Direct IP address modification is a placeholder and **NOT functional**. A VPN/Tor is highly recommended.
*   **Distribution Scope:** Compatibility is not guaranteed across all Linux distributions.
*   **Limited Guarantees:** The script is provided AS-IS with no guarantees. Review the code before execution.
*   **OD&H Disclaimer:** Oblivion Development & Hosting is not liable for any issues caused by using this tool.

## 🐧 Supported Distributions

Tested on:

*   Ubuntu
*   Debian
*   Pop!\_OS
*   Linux Mint
*   Fedora
*   Red Hat Enterprise Linux (RHEL)
*   CentOS
*   Rocky Linux
*   AlmaLinux
*   Arch Linux
*   Manjaro
*   EndeavourOS
*   openSUSE
*   SUSE Linux Enterprise (SLE)
*   Gentoo
*   Slackware

* * *

## 🤝 Contributing

Contributions are welcome!

1.  Fork it!
2.  Create your feature branch: `git checkout -b my-new-feature`
3.  Commit your changes: `git commit -am 'Add some feature'`
4.  Push to the branch: `git push origin my-new-feature`
5.  Submit a pull request.

* * *

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

* * *

## 📞 Contact

For questions, bug reports, or general inquiries, reach out to Oblivion Development & Hosting via our website: [https://odh.ivan-vcard.xyz](https://odh.ivan-vcard.xyz)

---

**Oblivion Development & Hosting (OD&H) - Delivering Secure, Reliable, and Innovative Tech Solutions.**
