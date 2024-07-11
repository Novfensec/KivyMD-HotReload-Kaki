# KivyMD Hot Reload with Kaki
A simple app demonstrating KivyMD hotreload using Kaki tool.

# Overview
This repository contains a basic KivyMD app that showcases hot reload functionality. With Kaki, you can make code changes and instantly see the updates without restarting the application.

# Prerequisites
Make sure you have the following installed:

  + **Kivy** : A Python framework for creating cross-platform applications.
  + **KivyMD** : A library providing Material Design components for Kivy.
  + **Kaki** : A tool enabling hot reload functionality.

# Installation
1. Install `Kaki`, `Kivy=2.3.0(specific)`, `KivyMD=1.1.1(specific)`

   <pre><code>pip install kivy==2.3.0 kivymd==1.1.1 kaki</code></pre>

# Project Structure
1. The root directory contains:
   + `main.py` : Main Python file.
   + `kv_files/` : Directory for Kivy language files.
   + `.vscode/launch.json` : Launch configuration file for VS Code users.`(specific)`

# Usage
1. Run the Kivy app using terminal:
   
   <pre><code>python main.py</code></pre>

2. Simply execute the `main.py` file from your editor.
3. VS Code users can create a `launch.json` file with the below python configuration settings in the `.vscode/` directory:
   ```javascript
    {
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "./main.py",
            "console": "internalConsole",
            "justMyCode": true
        }
      ]
    }
   ```
   
You should see the app window open with some basic app design. Make changes to the `app.kv` file  and save it, and see the updates in real-time without restarting the application.
Now you can develop your Kivy and KivyMD app with real-time updates using hot reload.

Happy Coding!

# Additional Resources:
+ [KivyMD Hot Reload: Mastering Kaki Tool for Seamless App Development (Youtube)](https://youtu.be/GdrwjSVSo2E?si=t-JlITVBwPxiA_wJ)
