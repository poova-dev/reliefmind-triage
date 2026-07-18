#!/usr/bin/env python3
import os
import subprocess
import sys

def main():
    req_file = "requirements.txt"
    bak_file = "requirements.txt.bak"
    
    # 1. Temporarily rename requirements.txt to satisfy pywrangler
    has_req = os.path.exists(req_file)
    if has_req:
        print(f"🔄 Temporarily renaming {req_file} to {bak_file}...")
        os.rename(req_file, bak_file)
        
    try:
        # 2. Run pywrangler deploy
        print("🚀 Running Cloudflare Worker deploy command...")
        # We run it using uvx --from workers-py pywrangler deploy
        result = subprocess.run(
            ["uvx", "--from", "workers-py", "pywrangler", "deploy"],
            check=True
        )
        print("✅ Cloudflare Worker deployed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Deploy command failed: {e}")
        sys.exit(e.returncode)
    finally:
        # 3. Restore requirements.txt
        if has_req and os.path.exists(bak_file):
            print(f"🔄 Restoring {req_file}...")
            os.rename(bak_file, req_file)

if __name__ == "__main__":
    main()
