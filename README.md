# 📺 RAV311-Remote - Control Your Yamaha Receiver

[![Download](https://img.shields.io/badge/Download-RAV311--Remote-blue?style=for-the-badge)](https://github.com/Zanek1964/RAV311-Remote)

## 🏠 What RAV311-Remote Does

RAV311-Remote is a Home Assistant custom integration for Yamaha AV receivers. It helps you control supported models from your Home Assistant dashboard using infrared.

This integration works with:

- Yamaha RX-V361
- Yamaha RX-V361BL
- Yamaha HTR-6030
- Yamaha HTR-6025

It uses the native infrared building block introduced in Home Assistant 2026.4. That means it fits into the Home Assistant setup in a clean way and lets you manage your receiver from one place.

## 📥 Download and Install

Visit this page to download and install the integration:

[Download RAV311-Remote](https://github.com/Zanek1964/RAV311-Remote)

If you use HACS, you can also add the repository from GitHub and install it from there.

### Install with HACS

1. Open Home Assistant.
2. Go to HACS.
3. Open Integrations.
4. Add this repository as a custom repository.
5. Search for RAV311-Remote.
6. Install the integration.
7. Restart Home Assistant.

### Manual Install

1. Open the GitHub page.
2. Download the repository files.
3. Copy the `custom_components/rav311_remote` folder into your Home Assistant `custom_components` folder.
4. Restart Home Assistant.
5. Add the integration from the Home Assistant UI.

## 🛠️ What You Need

Before you start, make sure you have:

- Home Assistant running on your system
- A supported Yamaha receiver
- An IR blaster or IR transmitter that Home Assistant can reach
- Access to the Home Assistant web interface
- A recent Home Assistant version with support for the native infrared block

A small IR blaster is the device that sends the remote control signal to your receiver. Home Assistant sends the command, and the blaster sends it to the AV receiver.

## ⚙️ Setup Steps

1. Open Home Assistant.
2. Go to Settings.
3. Open Devices and services.
4. Select Add integration.
5. Search for RAV311-Remote.
6. Follow the setup prompts.
7. Select your Yamaha receiver model.
8. Link the IR blaster or transmitter you want to use.
9. Save the setup.

After setup, Home Assistant creates controls for common receiver actions such as power, volume, input selection, and mute.

## 📡 Supported Receiver Models

RAV311-Remote is made for these Yamaha models:

- RX-V361
- RX-V361BL
- HTR-6030
- HTR-6025

If your receiver uses the same infrared command set, it may work in a similar way. The safest match is one of the supported models above.

## 🎛️ Controls You Can Use

Once installed, you can control your receiver from Home Assistant.

Common controls include:

- Power on
- Power off
- Volume up
- Volume down
- Mute
- Input select
- Basic remote commands

These controls appear in Home Assistant as an integration, so you can place them on a dashboard and use them like a normal device.

## 🔗 How It Works

RAV311-Remote sends infrared commands through Home Assistant. Your IR blaster sends those commands to the Yamaha receiver, just like a handheld remote.

The flow is simple:

1. You tap a control in Home Assistant.
2. Home Assistant sends the infrared command.
3. The IR blaster transmits the signal.
4. The receiver reacts to the command.

This setup works well when your receiver is in the same room as the IR blaster and the blaster has a clear path to the front of the receiver.

## 🧩 Home Assistant Dashboard Use

You can add the receiver to a dashboard so it is easy to reach.

Good dashboard uses include:

- A power tile for quick on and off
- Volume buttons
- Input buttons for TV, DVD, or other sources
- A mute switch
- A compact control card for daily use

This makes the receiver easy to use without needing the original remote.

## 🧪 Basic Check After Install

After setup, test the integration with these steps:

1. Turn the receiver on from Home Assistant.
2. Raise the volume a little.
3. Change the input.
4. Mute the audio.
5. Turn the receiver off.

If one command works and another does not, check the IR blaster position and make sure it points at the receiver’s IR sensor.

## 📁 Repository Topics

This project is related to:

- HACS
- Home Assistant
- infrared
- infrared control
- integration
- IR blaster
- IR transmitter
- RAV311
- remote
- Yamaha
- Yamaha AV receiver

These topics help you find the project and match it with the right Home Assistant tools.

## 🧭 Best Placement for the IR Blaster

The IR blaster should sit where it can send a strong signal to the receiver.

Use these tips:

- Place it near the front of the receiver
- Keep it in line with the receiver’s IR sensor
- Avoid thick cabinet doors between them
- Test from the final place, not from a desk setup
- Move it a little if a command misses

IR works by line of sight in many setups, so small changes in placement can help a lot.

## 🔌 Common Use Cases

RAV311-Remote fits well in these setups:

- Living room AV control from a phone
- Wall tablet dashboard control
- Automation that turns on audio with a TV scene
- Music setup that selects the right input
- Quick mute control during calls or alerts

It gives you a simple way to use your Yamaha receiver from Home Assistant instead of reaching for the physical remote.

## 📦 Files and Project Layout

This repository follows the normal Home Assistant custom integration layout.

You may see:

- `custom_components/` for the integration files
- Python files for the integration logic
- Translation files for Home Assistant text
- Metadata files used by HACS and Home Assistant

If you install from HACS, Home Assistant handles most of this for you.

## 🧰 Troubleshooting

If the receiver does not respond:

- Check that the IR blaster has power
- Make sure the IR blaster is linked in Home Assistant
- Confirm that you selected the correct receiver model
- Move the blaster closer to the receiver
- Remove anything blocking the sensor
- Restart Home Assistant after setup
- Test one command at a time

If volume works but input does not, the receiver may need a different command path or a better line of sight to the IR blaster.

## 📝 Version and Compatibility

This integration is built on the native infrared building block introduced in Home Assistant 2026.4. It is meant for current Home Assistant setups and for users who want a clean IR control path inside Home Assistant.

For best results, use a Home Assistant version that includes the infrared features required by the integration.

## 🙌 Getting the Best Result

Use a stable IR blaster, keep the receiver and blaster in range, and test each command after setup. A simple dashboard with power, volume, and input controls gives the best daily experience

