==============
Website CRM Notify
==============

This module provides the following functions:

* When someone sends question or inquiry from `Contact us` page on website, <br>
Sends an Email to both the company and sender for the purpose of nofitication and remainder.

This module depends on `wbsite_crm` module.


Installation
============

To install this module, 

* Place this module on a directory included in addons_path, updates Apps list on Odoo, and install this module.


Configration
============

To configure this module,

* Go to `Settings > Technical > Email > Templates` and select `Contact Form Notify`,
* Edit the template of Email to be sent.

By default, Email is sent to the following addresses

* of the company (for the purpose of notification)
* the sender inputs (for the purpose of remainder)

and the body of Email includes all the information the sender inputs (Name, Phone, Company and so on).


Usage
============

To use this module,

* Go to `Contact us` page of website, input the contents of your question or inquiry and submit them
