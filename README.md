# NameCraft

## Overview
**NameCraft** is a tool designed to help Minecraft players discover available 3-letter usernames. Given the scarcity of such short usernames, this tool automates the process of checking their availability. While getting a 3-letter username might seem nearly impossible without resorting to sniping methods, MineTag offers a simple and user-friendly way to explore what's still available.

## Features
- **Automated Username Checking:** Automatically generate and check the availability of all possible 3-letter Minecraft usernames.
- **Specific Username Checker:** Check the availability of any Minecraft username by manually entering it.
- **Real-time Feedback:** The program provides real-time feedback on whether a username is taken or available.
- **Logging:** All taken usernames are logged and saved to a file named `namesthatwork.txt`.

## Important Note
While the tool is generally accurate, there is a chance that the program might occasionally indicate a taken username as available. This could happen due to caching or slight delays in Mojang's API updates. It's not too common, but it’s possible and may occur in roughly 50% of cases. This issue is rare enough that it shouldn't affect most checks, but it's something to be aware of when using the tool.

## Usage
1. **Check a specific username:** Use this option to manually enter a username and check its availability.
2. **Generate and check 3-letter usernames:** This option will automatically generate all possible 3-letter combinations and check them one by one.
3. **Exit:** Exit the program gracefully.

## Notes
- This tool is probably the easiest way to get a 3-letter Minecraft username, short of sniping methods, although there is no guarantee of success due to the limited availability.
- The username availability check uses Mojang's official API, ensuring accurate results, though the aforementioned issue may occasionally occur.

## Installation
Simply clone this repository and run the Python script. Ensure you have Python installed on your system. No additional libraries are required beyond the standard library.

```bash
git clone https://github.com/YourUsername/MineTag.git
cd MineTag
python namecraft.py
