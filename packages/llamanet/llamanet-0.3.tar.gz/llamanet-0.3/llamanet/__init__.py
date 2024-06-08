# import llamanet
# llamanet.run()
# llamanet.run("start", HUGGINGFACE_URL, "-c", 128000, "--verbose")
# ...
import atexit
import subprocess
import time
import requests
import sys
import os
import signal
def run(*args):
  a = ['npx', '-y', 'llamanet@latest'] + list(args)
  process = subprocess.Popen(a, stdout=sys.stdout, stderr=sys.stderr)
  while True:
    try:
      response = requests.get('http://localhost:42424')
      if response.status_code == 200:
        break
    except requests.ConnectionError:
      pass
    time.sleep(1)

  # set environment variables
  os.environ['OPENAI_BASE_URL'] = "http://localhost:42424/v1"
  os.environ['OPENAI_API_KEY'] = "llamanet"

  # Register cleanup function to be called when the script exits
  def cleanup():
    os.killpg(os.getpgid(process.pid), signal.SIGTERM)
  atexit.register(cleanup)
