.. GIDEON API Wrapper - Python documentation master file, created by
   sphinx-quickstart on Tue Jun 29 17:32:44 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to GIDEON API Wrapper - Python's documentation!
=======================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   outbreaks
   disease_filter
   gideon_id_codes
   api_query_wrapper

Authentication
==============
All calls to the GIDEON API require an API key to work.
This library Provide your GIDEON API key as an environment variable.
The exact steps will depend on your operating system.

- macOS / Linux - Add the following line to your .bashrc file: export GIDEON_API_KEY='<YOUR API KEY>'
- Windows - Search for "Edit environment variables for your your account" in the Start Menu and add a GIDEON_API_KEY variable

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
