#!/usr/bin/env python3
import json
import subprocess
import os

CONFIG_PATH = os.path.expanduser("~/sms_bot/config.json")
STATE_PATH = os.path.expanduser("~/sms_bot/last_processed.txt")

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def run_cmd(command):
    try:
        res = subprocess.run(command, capture_output=True, text=True, check=True)
        return res.stdout.strip()
    except Exception as e:
        return None

def send_sms(number, message):
    run_cmd(["termux-sms-send", "-n", number, message])

def process_command(sender, body):
    body_clean = body.strip().lower()

    if body_clean.startswith("#ping"):
        send_sms(sender, "Bot Status: Online & operational.")

    elif body_clean.startswith("#battery"):
        batt_data = run_cmd(["termux-battery-status"])
        if batt_data:
            info = json.loads(batt_data)
            perc = info.get("percentage", "Unknown")
            status = info.get("status", "Unknown")
            send_sms(sender, f"Battery: {perc}% | Status: {status}")
        else:
            send_sms(sender, "Error retrieving battery stats.")

    elif body_clean.startswith("#ring"):
        run_cmd(["termux-volume", "stream", "alarm", "volume", "15"])
        run_cmd(["termux-tts-speak", "Emergency alert received from trusted contact."])
        send_sms(sender, "Triggered loud emergency sound on device.")

def main():
    config = load_config()
    allowed = config.get("allowed_numbers", [])
    
    # Read latest inbox (limit to recent 5 messages)
    raw_inbox = run_cmd(["termux-sms-inbox", "-l", "5"])
    if not raw_inbox:
        return

    try:
        messages = json.loads(raw_inbox)
    except Exception:
        return

    # Get last processed message ID to avoid duplicates
    last_id = ""
    if os.path.exists(STATE_PATH):
        with open(STATE_PATH, "r") as f:
            last_id = f.read().strip()

    for msg in messages:
        msg_id = str(msg.get("_id", ""))
        sender = msg.get("number", "")
        body = msg.get("body", "")

        if msg_id == last_id:
            break  # Reached already processed messages

        # Verify sender & trigger prefix
        if sender in allowed and body.startswith(config.get("trigger_prefix", "#")):
            process_command(sender, body)

    # Save newest ID
    if messages:
        with open(STATE_PATH, "w") as f:
            f.write(str(messages[0].get("_id", "")))

if __name__ == "__main__":
    main()

