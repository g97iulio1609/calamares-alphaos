#!/usr/bin/env python3
# encoding: utf-8
# === This file is part of Calamares - <http://github.com/calamares> ===
#
#   Copyright 2014 - 2015, Philip Müller <philm@manjaro.org>
#
#   Calamares is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Calamares is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Calamares. If not, see <http://www.gnu.org/licenses/>.

import os

import libcalamares

import shutil

def run():
    """ Misc postinstall configurations """

    install_path = libcalamares.globalstorage.value( "rootMountPoint" )


    # Add BROWSER var
     os.system("sed -i "s/pam-autologin-service=lightdm-autologin/#pam-autologin-service=lightdm-autologin/" /etc/lightdm/lightdm.conf".format(install_path))
     os.system("sed -i "s/autologin-user=alpha/#autologin-user=/" /etc/lightdm/lightdm.conf".format(install_path))
     os.system("sed -i "s/autologin-user-timeout=0/#autologin-user-timeout=0/" /etc/lightdm/lightdm.conf".format(install_path))
     os.system("sed -i "sed -i "s/%sudo	ALL=(ALL) ALL/#%sudo	ALL=(ALL) ALL/" /etc/sudoers".format(install_path))
     os.system("sed -i "s/%wheel ALL=(ALL) NOPASSWD: ALL/#%wheel ALL=(ALL) NOPASSWD: ALL/" /etc/sudoers".format(install_path))
     os.system("sed -i "s/alpha ALL=(ALL) NOPASSWD: ALL//" /etc/sudoers" /etc/sudoers".format(install_path))



    # Remove calamares
    if os.path.exists("{!s}/usr/bin/calamares".format(install_path)):
        libcalamares.utils.chroot_call(['pacman', '-R', '--noconfirm', 'calamares'])

    # Copy mirror list
    shutil.copy2('/etc/pacman.d/mirrorlist',
             os.path.join(install_path, 'etc/pacman.d/mirrorlist'))

    # Copy random generated keys by pacman-init to target
    if os.path.exists("{!s}/etc/pacman.d/gnupg".format(install_path)):
        os.system("rm -rf {!s}/etc/pacman.d/gnupg".format(install_path))
    os.system("cp -a /etc/pacman.d/gnupg {!s}/etc/pacman.d/".format(install_path))
    libcalamares.utils.chroot_call(['pacman-key', '--populate', 'archlinux', 'manjaro'])

    return None
