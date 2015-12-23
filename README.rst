======
pyomni
======
Python library to manipulate Omnifocus tasks.

Available function
------------------
* Add task to inbox

How to use
----------

Install via pip
^^^^^^^^^^^^^^^
.. code:: shell

 $ pip install pyomni


Sample code
^^^^^^^^^^^
.. code:: python

    from pyomni import PyOmni
    from pyomni import OmniTask

    if __name__ == "__main__":

        # Create PyOmni Instance
        po = PyOmni("username", "password")

        # Create task to add
        task = OmniTask("Sample task to add")

        # Call add_task method
        po.add_task(task)

.. image:: https://rawgit.com/taxpon/pyomni/master/resources/inbox.jpg

Reference
---------
* `Omnifocus .ofocus file format <https://github.com/tomzx/ofocus-format/tree/2.0>`_
* `Is editing the XML files to handle completes an option? <http://forums.omnigroup.com/showthread.php?p=105247#post105247>`_


License
-------
* MIT