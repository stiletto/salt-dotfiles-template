from __future__ import print_function
import os, pwd
from os import path

def main():
    grains = {}

    pw = pwd.getpwuid(os.getuid())
    grains['home_cwd'] = os.getcwd()
    grains['home_user'] = pw.pw_name
    grains['home_uid'] = pw.pw_uid
    grains['home_gid'] = pw.pw_gid
    grains['home_shell'] = pw.pw_shell
    grains['home'] = pw.pw_dir
    return grains

if __name__ == "__main__":
    import yaml
    print(yaml.dump(main()))
