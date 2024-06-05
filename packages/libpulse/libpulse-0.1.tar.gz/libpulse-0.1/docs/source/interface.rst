Interface
=========

Overview
--------

The libpulse ctypes foreign functions, the subclasses of the ctypes Structure
and the constants are built by the ``libpulse_ctypes`` module using the
``pulse_types``, ``pulse_enums``, ``pulse_structs`` and ``pulse_functions``
modules of the libpulse package. These modules are generated from the headers of
the ``pulse`` library. They represent the ABI of the library which is pretty
much stable. Using recent versions of Pulseaudio and Pipewire generates exactly
the same modules. These modules can be re-generated using ``gcc`` and
``pyclibrary`` as explained in the :ref:`Development` section although this is
not necessary.

The following sections describe the ``libpulse`` module of the libpulse package
that provides the ctypes interface to the library.

Variables
---------

The ``pulse`` enums constants are defined as variables of the module as well as
the ``PA_INVALID_INDEX`` variable.

``struct_ctypes`` is a dictionary of all the ``pulse`` structures defined as
subclasses of the ctypes Structure class.

Functions
---------

The ``pulse`` functions that are not async functions [#]_ have their
corresponding ctypes foreign functions defined. They may be called directly once
the LibPulse class has been instantiated.

PulseStructure class
--------------------

When a callback sets a pointer to a ``pulse`` structure as one of its arguments,
the memory referenced by this pointer is very short-lived. A PulseStructure is
then instantiated to make a deep copy of the structure. It includes the nested
structures and  the structures that are referenced by a member of the  structure
as a pointer to another structure (recursively). The attributes of the
PulseStructure instance are the members of the structure.

The PulseStructure instance is returned by the asyncio coroutine that handles
this callback. See below how to call a ``pulse`` async function.

PropList class
--------------

When the member of a ``pulse`` structure is a pointer to a ``proplist``, the
corresponding PulseStructure attribute is set to an instance of PropList
class. The PropList class is a subclass of ``dict`` and the elements of the
proplist can be
accessed as the elements of a dictionary.

PulseEvent class
----------------

An instance of PulseEvent is returned by the async iterator returned by the
get_events() method of a LibPulse instance. See below
:ref:`pa_context_subscribe()`.

Its attributes are::

  facility:   str - name of the facility, for example 'sink'.
  index:      int - index of the facility.
  type:       str - type of event, 'new', 'change' or 'remove'.

LibPulse class
--------------

The LibPulse class is an asyncio context manager. To instantiate the LibPulse
instance run::

  async with LibPulse('some name') as lib_pulse:
    statements using the 'lib_pulse' LibPulse instance
    ...

A LibPulse instance manages the connection to the ``pulse`` library. There is
only one instance of this class per asyncio event loop, and therefore only one
instance per thread.

The ``c_context`` attribute of the instance is required by all functions
prefixed with ``pa_context_`` as the first argument (but this first argument is
excluded from the LibPulse asyncio coroutine methods, see below).

LibPulse methods
""""""""""""""""

The ``pulse`` async functions [1]_ are implemented as LibPulse methods that are
asyncio coroutines except for five :ref:`Not implemented` methods.

These methods are sorted in four lists according to their signature and the
signature of their callbacks. The lists are the LibPulse class attributes:

  - context_methods
  - context_success_methods
  - context_list_methods
  - stream_success_methods

For all the methods, the first argument, the last one and the callback argument
in the corresponding libpulse signature are omitted upon invocation. For example
pa_context_get_server_info() is invoked as:

.. code-block:: python

    server_info = await lib_pulse.pa_context_get_server_info()

The ``context_methods`` return an empty list if the callback has no other
argument than ``pa_context *c`` and ``void *userdata``, they return a list if
the callback has set more than one of its arguments, otherwise they return the
unique argument set by the callback.

The ``context_success_methods`` and ``stream_success_methods`` return an ``int``, either
PA_OPERATION_DONE or PA_OPERATION_CANCELLED. Check the ``pa_operation_state``
enum in the ``pulse_enums`` module to get those values.

The ``context_list_methods`` return a list after the ``pulse`` library has
invoked repeatedly the callback, or just once as is the case for some of those
methods whose name ends with ``_by_name`` or ``_by_index``.

.. _pa_context_subscribe():

pa_context_subscribe()
""""""""""""""""""""""

``pa_context_subscribe()`` is one of the LibPulse asyncio coroutine method. This
method may be invoked at any time to change the subscription masks currently
set, even from within the ``async for`` loop that iterates over the reception of
libpulse events. After this method has been invoked for the first time, call the
``get_events()`` method to get an async iterator that returns the successive
libpulse events.

For example:

.. code-block:: python

    # Start the iteration on sink-input events.
    await lib_pulse.pa_context_subscribe(PA_SUBSCRIPTION_MASK_SINK_INPUT)
    iterator = lib_pulse.get_events()
    async for event in iterator:
        await handle_the_event(event)

``event`` is an instance of PulseEvent.

.. _Not implemented:

Not implemented
"""""""""""""""

The following ``pulse`` async functions are not implemented as a method of a
LibPulse instance:

    pa_signal_new() and pa_signal_set_destroy():
        Signals are handled by asyncio and the hook signal support built into
        pulse abstract main loop is not needed.

In the following functions the callback has to be handled by the libpulse module
user:

  - pa_context_rttime_new()
  - pa_stream_write()
  - pa_stream_write_ext_free()

An example on how to implement those coroutines can be found in the LibPulse
class implementation of context state monitoring:

    - ``__init__()`` sets the function pointer (and keeps a refence to it to
      prevent Python garbage collection) to a LibPulse staticmethod named
      ``context_state_callback()`` that will be called as the ``pulse``
      callback. The staticmethod gets the LibPulse instance through a call to
      the get_instance() method.

    - Upon entering the LibPulse context manager, the ``_pa_context_connect()``
      method sets this fonction pointer as the callback in the call to
      ``pa_context_set_state_callback()``.

.. rubric:: Footnotes

.. [#] ``pulse`` async functions are those functions that have a callback as
       one of their arguments and that do not set the callback.
