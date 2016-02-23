Drop to a shell on gbp buildpackage failure
===========================================

:date: 2015-12-21 15:43
:tags: debian, config
:category: debian-dev
:slug: pbuilder-hooks
:author: Kevin Murray
:summary: You can use pbuilder hooks to drop to a shell on build failure.


This was taken from the `ubuntu wiki <https://wiki.ubuntu.com/PbuilderHowto#Running_a_Shell_When_Build_Fails_.28Intro_to_Hook_Scripts.29>`_


This is done using a hook script. First we need to create a directory to home
your pbuilder hooks. This can be anywhere but we'll use a directory in
/var/cache/pbuilder for this example: ::

    sudo mkdir /var/cache/pbuilder/hook.d

Now we need to tell pbuilder to use this directory as its hook directory.
Edit ~/.pbuilderrc and add the following line: ::

    HOOKDIR="/var/cache/pbuilder/hook.d"

Then we need to add a hook script to be called by pbuilder when the
build fails. The script needs to be placed in the HOOKDIR and made
executable. The name of the hook script is also important. See the
pbuilder man page for details. As you can see, for this example, we
need to name the script C<digit><digit><whatever-else-you-want> so
let's call it C10shell. Edit the new file
/var/cache/pbuilder/hook.d/C10shell and add the following: ::

    #!/bin/sh
    # invoke shell if build fails.

    apt-get install -y --force-yes vim less bash
    cd /tmp/buildd/*/debian/..
    /bin/bash < /dev/tty > /dev/tty 2> /dev/tty

This script must be made world executable for pbuilder to execute it,
so now we run: ::

    sudo chmod a+x /var/cache/pbuilder/hook.d/C10shell

And you're all set.

END OF UBUNTU WIKI TEXT.


While you're at it, the whole Ubuntu wiki `pbuilder page
<https://wiki.ubuntu.com/PbuilderHowto>`_ is pretty awesome, and worth a read.


