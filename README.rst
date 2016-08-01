Introduction
------------
This structure contains the mini-project for the course
"Scientific Computing using Python, part 1", held at Aalborg University,
May 2016. The structure is stored and sent as a ``.zip`` file, but also
available at: https://bitbucket.org/nestorjhernandezm/phd-python-1/

You can get access to this repository by cloning it, by doing
in a terminal::

  git clone git@bitbucket.org:nestorjhernandezm/phd-python-1.git

Or, if you don't have SSH, by doing::

  git clone https://github.com/libgit2/libgit2

The mini-project is based in the Lorenz attractor equations. These
are a set of 3D, non-linear ordinary differential equations. Each
of the variables x, y, z is a state of the attractor. A good introductory
description can be found in [1_].

.. _1: https://en.wikipedia.org/wiki/Lorenz_system

Normally, for these equations, we are given a set initial conditions
and parameters to compute the states all times. We achieve this in
the mini-project by computing the states of the discretized version
of [1_] by the Euler method [2_].

.. _2: https://en.wikipedia.org/wiki/Euler_method

In what follows, we provide a short description of the mini-project.

Getting Started
---------------
.. As a first step, you can run the repository by generating::

..   sudo apt-get install g++ python mercurial git-core

.. In the following, we will clone ns-3 to the ``~/ns-3-dev`` folder and we
.. will clone the kodo-ns3-examples to the ``~/kodo-ns3-examples`` folder.
.. You may use different folders, but the two folders **must be separate**,
.. i.e. one cannot be the subfolder of the other.

.. Here you can put a bit of information/documentation of the program
.. you develop, including:

.. - Author
.. - What does the program?
.. - Files and dir structure
.. - How to run the program

.. you might need to put something like

.. import sys
.. sys.path.append('../')
.. import lorenz

.. in e.g. cases/case1.py or test/test.py to be access the functions etc.
.. you make in lorenz/solver.py, lorenz/run.py etc.
