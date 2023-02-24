#!/usr/bin/python

import subprocess
from datetime import datetime
# import resource


# def memory_limit():
#     soft, hard = resource.getrlimit(resource.RLIMIT_AS)
#     resource.setrlimit(resource.RLIMIT_AS, (2 * 1024 *
#                        1024 * 1024, hard))
#     soft, hard = resource.getrlimit(resource.RLIMIT_AS)
#     print(soft/(1024*1024*1024))


def grabUserInput():
    def filterInput(message, default):
        user_input = input(message)

        if user_input == "":
            user_input = default
        return user_input

    user_input_dict = {}

    user_input_dict["input_file"] = filterInput(
        "Input File: ", "./video/video.mp4")

    return user_input_dict


def buildFFmpegCommand():
    final_user_input = grabUserInput()

    commands_list = [
        'ffmpeg',
        '-i',
        final_user_input['input_file'],
        '-vf',
        'fps=1,scale=160:90,tile=10x4',
        './output/output%0003d.png'
    ]
    return commands_list


def runFFmpeg(commands):
    starttime = datetime.now()
    if subprocess.run(commands).returncode == 0:
        print("FFmpeg Script Ran Successfully")
        print(f'Total Time -> {(datetime.now() - starttime).total_seconds()}')
    else:
        print("There was an error running your FFmpeg script")


# memory_limit()
runFFmpeg(buildFFmpegCommand())
