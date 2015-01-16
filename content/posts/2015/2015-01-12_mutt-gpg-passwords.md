Title: Avoiding plain-text passwords in muttrc
Tags: config-snippets, gotchas
Category: notes-to-self
Author: Kevin Murray
Summary: Pipe it from gpg!

I'm not a fan of plain-text passwords just sitting on disk. However to avoid
typing my password every time I sent an email in [mutt](http://www.mutt.org/)
(which is a brilliant MUA by the way), I stored it on disk in my `muttrc`.

That was, until I saw a config file somewhere on the internet that contained
this magic:

    echo 'set my_password="password123"' | gpg -er MY_KEY_ID > ~/.mutt/pass.gpg

Then, at the start of your `muttrc`:

    source "gpg2 -dq ${HOME}/.mutt/pass.gpg |"

*noting the space and pipe at the end of that line*

This imports (securely) your password into RAM, which you can use via the
variable name you set in the echo statement above, like so:

    set smtp_url="smtp://me:$my_password@mydomain.com"
    set imap_url="imaps://me:$my_password@mydomain.com:993"

This "just worked" for me, hope it helps you.

Only problem, I can't find the place I originally saw this to give them credit.
If it was you and you want some credit, [contact me](/contact.html).
