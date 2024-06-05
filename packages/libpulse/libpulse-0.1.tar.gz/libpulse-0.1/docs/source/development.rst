.. _Development:

Development
===========

Requirements
------------

Development:
    * GNU ``gcc`` and `pyclibrary`_ are used to parse the libpulse headers and
      create the ``pulse_types``, ``pulse_enums``, ``pulse_structs``
      and ``pulse_functions`` modules of the libpulse package.

      To re-create those modules using the current libpulse headers run [#]_::

        $ python -m tools.libpulse_parser libpulse

    * `coverage`_ is used to get the test suite coverage.
    * `flit`_ is used to publish libpulse to PyPi and may be used to install
      libpulse locally.

      At the root of the libpulse git repository, use the following command to
      install libpulse locally::

        $ flit install --symlink [--python path/to/python]

      This symlinks libpulse into site-packages rather than copying it, so that
      you can test changes.

Documentation:
    * `Sphinx`_ [#]_.
    * `Read the Docs theme`_.

Documentation
-------------

To build locally the documentation follow these steps:

  - Fetch the GitLab test coverage badge::

      $ curl -o docs/source/_static/coverage.svg "https://gitlab.com/xdegaye/libpulse/badges/master/coverage.svg?min_medium=85&min_acceptable=90&min_good=90"

  - Build the html documentation and the man pages::

      $ make -C docs clean html

Updating the development version
--------------------------------

In order to update the version at the `latest documentation`_ during
development, after a change in the functionality or in the features, run the
following commands::

    $ python -m tools.set_devpt_version_name
    $ make -C docs clean html
    $ git commit -m "Update version"
    $ git push

Releasing
---------

* Run the test suite from the root of the project [#]_::

    $ python -m unittest --verbose --catch --failfast

* Get the test suite coverage::

    $ coverage run -m unittest
    $ coverage report -m

* Update ``__version__`` in libpulse/__init__.py.
* Update docs/source/history.rst if needed.
* Build locally the documentation, see the previous section.
* Commit the changes::

    $ git commit -m 'Version 0.n'
    $ git push

* Tag the release and push::

    $ git tag -a v0.n -m 'Version 0.n'
    $ git push --tags

* Publish the new version to PyPi::

    $ flit publish

.. _Read the Docs theme:
    https://docs.readthedocs.io/en/stable/faq.html#i-want-to-use-the-read-the-docs-theme-locally
.. _Sphinx: https://www.sphinx-doc.org/
.. _`coverage`: https://pypi.org/project/coverage/
.. _flit: https://pypi.org/project/flit/
.. _unittest command line options:
    https://docs.python.org/3/library/unittest.html#command-line-options
.. _latest documentation:
    https://libpulse.readthedocs.io/en/latest/
.. _pyclibrary:
    https://pypi.org/project/pyclibrary/

.. rubric:: Footnotes

.. [#] The shell commands in this section are all run from the root of the
       repository.
.. [#] Required versions at ``docs/requirements.txt``.
.. [#] See `unittest command line options`_.
