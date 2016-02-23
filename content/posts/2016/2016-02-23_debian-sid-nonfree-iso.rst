==============================================
Getting a Debian testing/sid ISO with firmware
==============================================

:date: 2016-02-23 16:23
:tags: installer
:category: debian
:slug: debian-sid-iso-nonfree
:author: Kevin Murray
:summary: There's an annoyingly long path to the ISOs

To obtain a Debian installer CD ISO with non-free firmware available (which is
often requred for NICs or WiFi recievers), the following will work.

.. code-block:: shell

   baseurl='http://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/daily-builds/sid_d-i/current/amd64/iso-cd/'

   for file in firmware-testing-amd64-netinst.iso SHA512SUMS SHA512SUMS.sign
   do
        wget -O $file ${baseurl}${file}
   done

   gpg --recv-keys 'F41D 3034 2F35 4669 5F65  C669 4246 8F40 09EA 8AC3'
   gpg --verify SHA512SUMS.sign
   sha512sums -c SHA512SUMS

This will get you an ISO of the latest netinst testing CD, and verify its
integrity. Note that the key used to sign Debian images changes periodically,
so you may need to update the call to ``gpg --recv-keys`` above to reflect any
newer keys (you'll be told about a missing key when you do ``gpg --verify``).

To flash this to a USB stick, do:

.. code-block:: shell

    sudo cp firmware-testing-amd64-netinst.iso /dev/sdX

where ``/dev/sdX`` is the block device of your USB stick. Find this with ``sudo
fdisk -l /dev/sd?`` and/or ``dmesg``.
