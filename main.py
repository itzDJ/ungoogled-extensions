#!/usr/bin/env python3

"""
Script to update ungoogled-chromium extensions through the manual install method

Subprocess notes: https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output
Extension notes: https://avoidthehack.com/manually-install-extensions-ungoogled-chromium
"""

import subprocess

# assumes homebrew is installed and eloston-chromium is installed via homebrew
# updates homebrew and upgrades eloston-chromium
subprocess.run("brew upgrade eloston-chromium", shell=True)

# gets the version of eloston-chromium needed for the install URL
VERSION = (
    subprocess.run(
        "brew list --versions --casks eloston-chromium",
        shell=True,
        stdout=subprocess.PIPE,
    )
    .stdout.decode("utf-8")
    .split(" ")[1]
    .split("-")[0]
)


def install():
    EXTENSION_ID = input("Enter the extension ID from the Chrome Web Store URL: ")
    URL = f"https://clients2.google.com/service/update2/crx?response=redirect&acceptformat=crx2,crx3&prodversion={VERSION}&x=id%3D{EXTENSION_ID}%26installsource%3Dondemand%26uc"
    print(f"Install URL: {URL}")


def update():
    UBLOCK_ORIGIN_EXTENSION_ID = "cjpalhdlnbpafiamejdnhcphjbkeiagm"
    # BITWARDEN_EXTENSION_ID = "nngceckbapebfimnlniiiahkandclblb"

    UBLOCK_ORIGIN_URL = f"https://clients2.google.com/service/update2/crx?response=redirect&acceptformat=crx2,crx3&prodversion={VERSION}&x=id%3D{UBLOCK_ORIGIN_EXTENSION_ID}%26installsource%3Dondemand%26uc"
    # BITWARDEN_URL = f"https://clients2.google.com/service/update2/crx?response=redirect&acceptformat=crx2,crx3&prodversion={VERSION}&x=id%3D{BITWARDEN_EXTENSION_ID}%26installsource%3Dondemand%26uc"

    print(f"uBlock Origin: {UBLOCK_ORIGIN_URL}")
    # print(f"Bitwarden: {BITWARDEN_URL}")

    # subprocess.run(
    #     f"open -a Chromium {UBLOCK_ORIGIN_URL}", shell=True
    # )  # TODO: Get this to work


if __name__ == "__main__":
    if input("Install or update extension(s)? (i/U): ").lower() == "i":
        install()
    else:
        update()
