#!/usr/bin/env python3
# -*- coding: utf-8 -*-

TITLE_TEX_FILE_NAME = "title"
HEADERS_FILE_NAME = "head.tex"
LOG_FILE_NAME = "log.txt"
TEMP_FILENAME = "temp.pdf"
REQUIRED_EXECS = ("pandoc", "xelatex", "pdftk")
FILES_TO_RM = (".log", ".aux")

CLEAR_LOG_CMD = f": > {LOG_FILE_NAME}"
GENERATE_TITLE_CMD = f"xelatex {TITLE_TEX_FILE_NAME}.tex >> {LOG_FILE_NAME}"
REMOVE_LAST_LINE_CMD = f"sed -i '$ d' {HEADERS_FILE_NAME}"
SET_STARTPAGE_TO_2_CMD = f'echo "\setcounter{{page}}{{2}}" >> {HEADERS_FILE_NAME}'
CMD_EXEC_ERROR_MSG = f"Error! Check {LOG_FILE_NAME}"


import argparse
from shutil import which
from os import rename, remove, system
from os.path import exists


def check_executables():
    result = True
    for exec in REQUIRED_EXECS:
        if not which(exec):
            print(f"Error: {exec} not installed!")
            result = False
    return result


def check_files(md_filename):
    required_files = (
        f"{md_filename}.md",
        f"{TITLE_TEX_FILE_NAME}.tex",
        HEADERS_FILE_NAME,
    )
    result = True
    for filename in required_files:
        if not exists(f"./{filename}"):
            print(f"Error: {filename} not exists!")
            result = False
    return result


def parse_args():
    parser = argparse.ArgumentParser(description="Report generator")
    parser.add_argument("filename", type=str, help=".md file name without extension")
    parser.add_argument("--title", help="Include title sheet", action="store_true")
    parser.add_argument("--toc", help="Include table of contents", action="store_true")
    args = parser.parse_args()
    return args.filename, args.title, args.toc


def generate_title_sheet():
    print("Generating title...", end=" ")
    result = True
    if system(GENERATE_TITLE_CMD):
        print(CMD_EXEC_ERROR_MSG)
        result = False
    else:
        print("Done!")
        system(SET_STARTPAGE_TO_2_CMD)

    for extension in FILES_TO_RM:
        filename = TITLE_TEX_FILE_NAME + extension
        if exists(filename):
            remove(filename)
    return result


def main():
    if not check_executables():
        return

    report_filename, title, toc = parse_args()
    if not check_files(report_filename):
        return

    system(CLEAR_LOG_CMD)

    if title:
        if not generate_title_sheet():
            return

    print("Generating report...", end=" ")
    generate_report_cmd = f"pandoc --pdf-engine=xelatex -H {HEADERS_FILE_NAME} \
        {report_filename}.md -o {TEMP_FILENAME}{' --toc' if toc else ''} 2>> {LOG_FILE_NAME}"
    if system(generate_report_cmd):
        print(CMD_EXEC_ERROR_MSG)
        return
    else:
        print("Done!")

    output_filename = f"{report_filename}.pdf"

    if title:
        print("Concatenatig title with report...", end=" ")
        system(REMOVE_LAST_LINE_CMD)
        concat_cmd = f"pdftk {TITLE_TEX_FILE_NAME}.pdf {TEMP_FILENAME} cat output {output_filename} >> {LOG_FILE_NAME}"
        if system(concat_cmd):
            print(CMD_EXEC_ERROR_MSG)
            return
        else:
            remove(f"{TITLE_TEX_FILE_NAME}.pdf")
            remove(TEMP_FILENAME)
            print("Done!")
    else:
        rename(TEMP_FILENAME, output_filename)

    if exists(LOG_FILE_NAME):
        remove(LOG_FILE_NAME)

    print("All done, have a nice day!")


if __name__ == "__main__":
    main()
