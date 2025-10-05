# 🤖 HelpDesk Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**Intelligent IT support assistant powered by AI for automated troubleshooting and system diagnostics**

</div>

---

## 📋 Overview

HelpDesk Assistant is a local Python-based IT support tool that combines system diagnostics with AI-powered troubleshooting guidance. Designed for both technical and non-technical users, it automatically detects system information and provides step-by-step solutions to common computer problems.

Perfect for:
- **Help Desk Teams** providing remote support
- **IT Departments** automating tier-1 support
- **End Users** troubleshooting their own issues
- **System Administrators** diagnosing system problems

## ✨ Features

### 🔍 Automatic System Detection
- **Hardware Information**: CPU, RAM, disk usage
- **Operating System**: Version, architecture, platform details
- **Network Configuration**: IP address, connectivity status
- **Running Processes**: Active applications and services

### 💬 Intelligent Troubleshooting
- **AI-Powered Guidance**: Clear, step-by-step instructions
- **Context-Aware Solutions**: Tailored to your specific system
- **Interactive Diagnosis**: Asks relevant follow-up questions
- **Multi-Issue Support**: Handles various IT problems

### 🔒 Privacy & Security
- **100% Local Execution**: No data sent to external servers (except OpenAI API)
- **Secure API Key Handling**: Keys stored locally, never uploaded
- **No Telemetry**: No tracking or usage data collection
- **Open Source**: Fully transparent and auditable code

### 🎯 User-Friendly
- **Simple Interface**: No technical knowledge required
- **Clear Instructions**: Easy-to-follow troubleshooting steps
- **Cross-Platform**: Works on Windows, Linux, and macOS
- **Standalone Executable**: Optional .exe for non-Python users

## 🚀 Quick Start

### Installation

**Method 1: Python Script (Recommended)**
```bash
# Clone the repository
git clone https://github.com/x0VIER/HelpDeskAssistant.git
cd HelpDeskAssistant

# Install dependencies
pip install -r requirements.txt

# Run the assistant
python "HELP DESK AI.py"
```

**Method 2: Standalone Executable**
```bash
# Download the .exe file (Windows only)
# Double-click to run - no Python installation needed
```

### First-Time Setup

1. **Obtain OpenAI API Key**
   - Visit [OpenAI Platform](https://platform.openai.com/)
   - Create an account or sign in
   - Navigate to API Keys section
   - Generate a new API key

2. **Configure the Assistant**
   - Run the application
   - Enter your API key when prompted
   - Key is stored locally for future use

3. **Start Troubleshooting**
   - Describe your computer problem
   - Answer follow-up questions
   - Follow the provided step-by-step instructions

## 📖 Usage Examples

### Example 1: Slow Computer Performance
```
User: My computer is running very slow
