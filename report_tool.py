#!/usr/bin/env python3
# -*- coding: utf-8 -*-

TITLE_TEX_FILE_NAME = "title"
FILES_TO_RM = (".log", ".aux")

HEADERS_FILE_NAME = "head.tex"

GENERATE_TITLE_CMD = f"xelatex {TITLE_TEX_FILE_NAME}.tex"

REQUIRED_EXECS = ("pandoc", "xelatex", "pdftk")

TEMP_FILENAME = "temp.pdf"

from shutil import which
import argparse
from os import rename, remove, system
from os.path import exists


def check_executables():
    result = True
    for exec in REQUIRED_EXECS:
        if not which(exec):
            print("Error: {exec} not installed!")
            result = False
    return result


def check_files(md_filename):
    required_files = (f"{md_filename}.md", f"{TITLE_TEX_FILE_NAME}.tex", HEADERS_FILE_NAME)
    result = True
    for filename in required_files:
        if not exists(f"./{filename}"):
            print(f"Error: {filename} not exists!")
            result = False
    return result


def generate_title_sheet():
    result = system(GENERATE_TITLE_CMD)
    for extension in FILES_TO_RM:
        remove(TITLE_TEX_FILE_NAME + extension)
    return result



if __name__ == "__main__":
    
    if check_executables():

        parser = argparse.ArgumentParser(description='Report generator')
        parser.add_argument('filename', type=str, help='.md file name without extension')
        parser.add_argument('--title', help='Include title sheet', action='store_true')
        parser.add_argument('--toc', help='Include table of contents', action='store_true')
        args = parser.parse_args()

        report_filename = args.filename

        if check_files(report_filename):

            if args.title:
                print("Generating title...", end=" ")
                if (generate_title_sheet() == 0):
                    print("Done!")
                else:
                    print("Error!")
                system(f'echo "\setcounter{{page}}{{2}}" >> {HEADERS_FILE_NAME}')
                    

            print("Generating report...", end=" ")
            generate_report_cmd = f"pandoc --pdf-engine=xelatex -H {HEADERS_FILE_NAME} {report_filename}.md -o {TEMP_FILENAME}{' --toc' if args.toc else ''}"
            system(generate_report_cmd)
            

            output_filename = f"{report_filename}.pdf"

            if args.title:
                print("Concatenatig files...", end=" ")
                system(f"sed -i '$ d' {HEADERS_FILE_NAME}")
                system(f"pdftk {TITLE_TEX_FILE_NAME}.pdf {TEMP_FILENAME} cat output {output_filename}")
                remove(f"{TITLE_TEX_FILE_NAME}.pdf")
                remove(TEMP_FILENAME)
                print("Done!")
            else:
                rename(TEMP_FILENAME, output_filename)
            print("Done!")
