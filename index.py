import subprocess
import logging
import sys


astc_command = 'LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/lib64 ./astcenc/astcenc-sse2 -cl %s %s 6x6 -medium'

# 控制log输出级别
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger()
logger.setLevel(level=logging.INFO)


def main_handler(event, context):
    logger.info("start main handler")

    command_to_run = astc_command % ("input.png", "/tmp/input.astc")
    print("Command to run: " + command_to_run)

    child = subprocess.run(command_to_run, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           close_fds=True, shell=True)
    if child.returncode == 0:
        print("success:", child)
        return "Success"
    else:
        return "Transcode failed." + str(child.stderr)
