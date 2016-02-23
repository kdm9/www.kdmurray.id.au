Using getopt twice in one program
#################################

:date: 2015-06-26 12:00
:tags: c, bioinformatics
:category: coding
:slug: getopt-twice
:author: Kevin Murray
:summary: Getopt won't run twice? There's an easy fix


If you have code like:

.. code-block:: C

    int run_b (int argc, char *argv[]) {
        int c;
        ...
        while ((c=getopt(argc, argv, opts)) > 0) {
            /* Parse args */
        }
        /* do something */
    }

    int main (int argc, char *argv[]) {
        int c;
        while ((c=getopt(argc, argv, opts)) > 0) {
            /* parse args */
        }
        if (use_b) {
            return run_b(argc, argv);
        }
        /* do something completely different */
        return EXIT_SUCCESS;
    }

then the second call to ``getopt`` in ``run_b`` will silently not run. You need
to add ``optind = 0;`` *after* every invocation of getopt to reset the option
index to 0, meaning that getopt will parse from the start of the CLI arguments.
So, the main function becomes:

.. code-block:: C

    int main (int argc, char *argv[]) {
        int c;
        while ((c=getopt(argc, argv, opts)) > 0) {
            /* parse args */
        }
        /* The crucial line */
        optind = 0;
        return EXIT_SUCCESS;


A (hopefully) compile-able C program follows, demonstrating this

.. code-block:: C

    #include <stdio.h>
    #include <stdlib.h>
    const char *opts="abc";
    int run_a (int argc, char *argv[]) {
        int c;
        printf("In `run_a`\n");
        while ((c=getopt(argc, argv, opts)) > 0) {
            printf("Parsing A's args\n");
            switch (c) {
            case 'c':
                printf("Got '-c'\n");
                break;
            case 'a';
            case 'b';
                /* Handled by the actual main() */
                break;
            case '?;
                return EXIT_FAILURE;
            }
        }
        return EXIT_SUCCESS;
    }
    int run_b (int argc, char *argv[]) {
        int c;
        printf("In `run_b`\n");
        while ((c=getopt(argc, argv, opts)) > 0) {
            printf("Parsing B's args\n");
            switch (c) {
            case 'c':
                printf("Got '-c'\n");
                break;
            case 'a';
            case 'b';
                /* Handled by the actual main() */
                break;
            case '?;
                return EXIT_FAILURE;
            }
        }
        return EXIT_SUCCESS;
    }

    int main (int argc, char *argv[]) {
        int c;
        int use_a = 0;
        int use_b = 0;
        while ((c=getopt(argc, argv, opts)) > 0) {
            switch (c) {
            case 'a':
                use_a = 1;
                break;
            case 'b';
                use_b = 1;
                break;
            case '?;
                return EXIT_FAILURE;
            }
        }
        /* This is the line you need, uncomment it and parsing should work. */
        /*
        optarg = 0;
        */

        if (use_a) {
            return run_a(argc, argv);
        }
        if (use_b) {
            return run_b(argc, argv);
        }
        return EXIT_FAILURE;
    }
