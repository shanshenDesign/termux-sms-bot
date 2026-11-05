# 📱 Termux SMS Command Bot

A lightweight, offline-capable Python automation script that turns your Android phone into an **SMS Command Center and Relay**. By listening to incoming text messages through **Termux:API**, this bot parses authorized trigger words (`#ping`, `#battery`, `#ring`) and executes native device actions or sends automated SMS replies remotely.

---

## 🚀 What It Does
* **Remote Device Audit:** Send `#battery` from an authorized phone number to instantly receive your device's current battery percentage and charging state via SMS.
* **Emergency Alarm Trigger:** Send `#ring` to override silent modes, max out your phone's alarm volume, and trigger text-to-speech emergency announcements.
* **System Health Monitoring:** Send `#ping` to verify that your mobile node is online, responsive, and operational.
* **One-Tap Widget Execution:** Easily run or toggle background monitoring directly from your Android home screen using **Termux:Widget**.

---

## 💡 How It Helps
* **Zero Internet / Cloud Dependency:** Operates purely over cellular text messaging, allowing you to manage or query your phone even when Wi-Fi or mobile data is disabled.
* **Automation & Portability:** Leverages Android's hardware APIs locally on your mobile device without needing heavy external servers or third-party paid SMS gateway subscriptions.
* **Security-First Design:** Implements rigid sender verification via a local whitelist configuration file (`config.json`) to block unauthorized users from interacting with your device.

---

## 🛠️ Prerequisites & Tools Needed
Make sure you have the following installed on your Android device:
1. **Termux** (Installed from F-Droid)
2. **Termux:API** (App + package bridge)
3. **Termux:Widget** (For home screen shortcuts)
4. **Python 3 & JQ** (`pkg install python jq -y`)

---

## ⚙️ Installation & Setup Guide

### 1. Clone the Repository
```bash
git clone [https://github.com/shanshenDesign/termux-sms-bot.git](https://github.com/shanshenDesign/termux-sms-bot.git) ~/sms_bot
cd ~/sms_bot
