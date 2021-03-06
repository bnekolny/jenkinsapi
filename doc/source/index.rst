JenkinsAPI
==========

Jenkins is the market leading continuous integration system, originally created by Kohsuke Kawaguchi. This API makes Jenkins even easier to use by providing an easy to use conventional python interface.

Jenkins (and It's predecessor Hudson) are fantastic projects - but they are somewhat Java-centric. Thankfully the designers have provided an excellent and complete REST interface. This library wraps up that interface as more conventional python objects in order to make most Jenkins oriented tasks simpler.

This library can help you:

 * Query the test-results of a completed build
 * Get a objects representing the latest builds of a job
 * Search for artifacts by simple criteria
 * Block until jobs are complete
 * Install artifacts to custom-specified directory structures
 * Username/password auth support for jenkins instances with auth turned on
 * Search for builds by subversion revision
 * Add, remove and query jenkins slaves

Important links
===============

Project source code: github: https://github.com/salimfadhley/jenkinsapi

Releases: http://pypi.python.org/pypi/jenkinsapi

This documentation: http://packages.python.org/jenkinsapi/

Installation
============

Egg-files for this project are hosted on PyPi. Most Python users should be able to use pip or distribute to automatically install this project.

Most users can do the following:

    easy_install jenkinsapi

If you'd like to install in multi-version mode:

    easy_install -m jenkinsapi

Project Authors
===============

 * Salim Fadhley (sal@stodge.org) 
 * Ramon van Alteren (ramon@vanalteren.nl) 
 * Ruslan Lutsenko (ruslan.lutcenko@gmail.com) 



Package Contents
================

.. toctree::
   jenkinsapi
   jenkinsapi.command_line
   jenkinsapi.utils
   modules
	
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

