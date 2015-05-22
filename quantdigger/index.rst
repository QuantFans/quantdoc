.. quantdigger documentation master file, created by
   sphinx-quickstart on Sun May 17 16:47:03 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to quantdigger's documentation!
=======================================

Contents:

.. toctree::
   :numbered:

   内核 <quantdigger.kernel>
   #quantdigger.plugin
   #:maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. py:function:: filterwarnings(action, message='', category=Warning, \
                                module='', lineno=0, append=False)
   :noindex:

   :param str sender: The person sending the message
   :param str recipient: The recipient of the message
   :param str message_body: The body of the message
   :param priority: The priority of the message, can be a number 1-5
   :type priority: integer or None
   :return: the message id
   :rtype: int
   :raises ValueError: if the message_body exceeds 160 characters
   :raises TypeError: if the message_body is not a basestring

.. cpp:class:: NameSpace::ClassName : public MyBase, MyOtherBase

.. cpp:function:: bool namespaced::theclass::method(int arg1, std::string arg2)

   :param str arg1: The person sending the message

   :param str recipient: The recipient of the message

   :py:func:`.filterwarnings`
   ok :class:`.NameSpace::ClassName` hell

.. code-block:: python
   :linenos:
   :emphasize-lines: 1, 2-3

   def some_function():
       interesting = False
       print 'This line is highlighted.'
       print 'This one is not...'
       print '...but this one is.'
