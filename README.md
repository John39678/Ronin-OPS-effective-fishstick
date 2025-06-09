# Ronin-OPS-effective-fishstick
Voice Activated Local private coder and more
mkdir ronin-ops
cd ronin-ops
touch main.py requirements.txt README.md
mkdir static
touch static/index.html

# requirements.txt
fastapi==0.110.0
uvicorn==0.29.0
httpx==0.27.0
python-multipart==0.0.9

{ pkgs }: {
    deps = [
        pkgs.python310
        pkgs.python310Packages.fastapi
        pkgs.python310Packages.uvicorn
        pkgs.python310Packages.httpx
    ];
}


🛠️ Setup

### Prerequisites
1. [LM Studio](https://lmstudio.ai/) installed
2. Python 3.10+
3. Modern browser (Chrome recommended)

### Installation
```bash
# Clone repository
git clone https://github.com/your-username/ronin-ops.git
cd ronin-ops

# Install dependencies
pip install -r requirements.txt

