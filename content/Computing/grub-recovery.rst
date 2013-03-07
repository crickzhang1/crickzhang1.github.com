Recover GRUB to MBR/EBR using a Linux install-cd
################################################

:date: 2013-03-07 18:46
:tags: Linux, GRUB
:category: Computing
:slug: recover-grub-to-mbr-using-a-linux-install-cd
:author: Crick Zhang
:summary: Recover GRUB to MBR/EBR using a bootable (Gentoo) Linux install-cd.

Occasionally GRUB in MBR (Main Boot Record) or EBR (Extended Boot Record) get
corrupted in our Linux box, and will boot correctly. So come the following
few steps for recovering GRUB installation just as a note for convenience.
A bootable Linux install-cd is sufficient for this purpose, and I prefer a 
`Gentoo minimal installation ISO`_ (as a bootable CD or bootable USB pen).

The following assumption is made:

* The first partation (`/dev/sda1`) of the harddisk holds the main Linux system
  (`/bin`, `/usr/bin`, `/boot`, etc.) and in which GRUB related files should
  be OK.

Boot the computer with the installing medium into the Gentoo shell.
Here are the recovery steps:

.. code-block:: bash

  $ # Necessary mounts
  $ mkdir -p /mnt/gentoo
  $ mount /dev/sda1 /mnt/gentoo
  $ mount -t proc none /mnt/gentoo
  $ mount -o bind /dev /mnt/gentoo/dev
  $ # Chroot in the Linux system in our harddisk
  $ chroot /mnt/gentoo /bin/bash
  $ source /etc/profile
  $ # Find the rootfs
  $ grep -v rootfs /proc/mounts > /etc/mtab
  $ # Install GRUB to MBR
  $ grub-install /dev/sda
  $ umount /mnt/gentoo/proc
  $ umount /mnt/gentoo/bind
  $ umount /gentoo
  $ # Reboot the system and GRUB will be OK.

.. _Gentoo minimal installation ISO: http://distfiles.gentoo.org/releases/amd64/autobuilds/current-iso/
