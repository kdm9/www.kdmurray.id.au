=============================
DIY numpy and scipy on raijin
=============================

:date: 2016-06-08
:tags: python
:category: notes-to-self
:slug: raijin-scipy
:author: Kevin Murray


In short, use OpenBLAS not any of the other BLAS libs. Also, use gfortran, as it 
seems to play a bit nicer with GCC-compiled python


.. code-block:: shell

    git clone git://github.com/xianyi/OpenBLAS
    cd OpenBLAS
    make FC=gfortran
    make PREFIX=$PREFIX/ install

    NPY_NUM_BUILD_JOBS=4 pip3 install numpy scipy
