

.. image:: assets/img/diagrams.png
   :target: assets/img/diagrams.png
   :alt: diagrams logo


Diagrams
========


.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: /LICENSE
   :alt: license


.. image:: https://badge.fury.io/py/diagrams.svg
   :target: https://badge.fury.io/py/diagrams
   :alt: pypi version


.. image:: https://img.shields.io/badge/python-3.6%2C3.7%2C3.8-blue?logo=python
   :target: https://img.shields.io/badge/python-3.6%2C3.7%2C3.8-blue?logo=python
   :alt: python version


.. image:: https://badgen.net/https/api.tickgit.com/badgen/github.com/mingrammer/diagrams?label=todos
   :target: https://www.tickgit.com/browse?repo=github.com/mingrammer/diagrams
   :alt: todos


.. image:: https://img.shields.io/badge/provider-OnPremise-orange?color=5f87bf
   :target: https://img.shields.io/badge/provider-OnPremise-orange?color=5f87bf
   :alt: on premise provider


.. image:: https://img.shields.io/badge/provider-AWS-orange?logo=amazon-aws&color=ff9900
   :target: https://img.shields.io/badge/provider-AWS-orange?logo=amazon-aws&color=ff9900
   :alt: aws provider


.. image:: https://img.shields.io/badge/provider-Azure-orange?logo=microsoft-azure&color=0089d6
   :target: https://img.shields.io/badge/provider-Azure-orange?logo=microsoft-azure&color=0089d6
   :alt: azure provider


.. image:: https://img.shields.io/badge/provider-GCP-orange?logo=google-cloud&color=4285f4
   :target: https://img.shields.io/badge/provider-GCP-orange?logo=google-cloud&color=4285f4
   :alt: gcp provider


.. image:: https://img.shields.io/badge/provider-Kubernetes-orange?logo=kubernetes&color=326ce5
   :target: https://img.shields.io/badge/provider-Kubernetes-orange?logo=kubernetes&color=326ce5
   :alt: kubernetes provider


.. image:: https://img.shields.io/badge/provider-AlibabaCloud-orange
   :target: https://img.shields.io/badge/provider-AlibabaCloud-orange
   :alt: alibaba cloud provider


.. image:: https://img.shields.io/badge/provider-OracleCloud-orange?logo=oracle&color=f80000
   :target: https://img.shields.io/badge/provider-OracleCloud-orange?logo=oracle&color=f80000
   :alt: oracle cloud provider


.. image:: https://img.shields.io/badge/provider-Programming-orange?color=5f87bf
   :target: https://img.shields.io/badge/provider-Programming-orange?color=5f87bf
   :alt: programming provider


**Diagram as Code**.

Diagrams lets you draw the cloud system architecture **in Python code**. It was born for **prototyping** a new system architecture design without any design tools. You can also describe or visualize the existing system architecture as well. Diagrams currently supports six major providers: ``AWS``\ , ``Azure``\ , ``GCP``\ , ``Kubernetes``\ , ``Alibaba Cloud`` and ``Oracle Cloud``.  It now also supports ``On-Premise`` nodes.

**Diagram as Code** also allows you to **track** the architecture diagram changes in any **version control** system.

..

    NOTE: It does not control any actual cloud resources nor does it generate cloud formation or terraform code. It is just for drawing the cloud system architecture diagrams.


Getting Started
---------------

It requires **Python 3.6** or higher, check your Python version first.

It uses `Graphviz <https://www.graphviz.org/>`_ to render the diagram, so you need to `install Graphviz <https://graphviz.gitlab.io/download/>`_ to use **diagrams**. After installing graphviz (or already have it), install the **diagrams**.

..

   macOS users can download the Graphviz via ``brew install graphviz`` if you're using `Homebrew <https://brew.sh>`_.


.. code-block:: shell

   # using pip (pip3)
   $ pip install diagrams

   # using pipenv
   $ pipenv install diagrams

   # using poetry
   $ poetry add diagrams

You can start with `quick start <https://diagrams.mingrammer.com/docs/getting-started/installation#quick-start>`_. Check out `guides <https://diagrams.mingrammer.com/docs/guides/diagram>`_ for more details, and you can find all available nodes list in `here <https://diagrams.mingrammer.com/docs/nodes/aws>`_.

Examples
--------

.. list-table::
   :header-rows: 1

   * - Event Processing
     - Stateful Architecture
     - Advanced Web Service
   * - 
     .. image:: https://diagrams.mingrammer.com/img/event_processing_diagram.png
        :target: https://diagrams.mingrammer.com/img/event_processing_diagram.png
        :alt: event processing
     
     - 
     .. image:: https://diagrams.mingrammer.com/img/stateful_architecture_diagram.png
        :target: https://diagrams.mingrammer.com/img/stateful_architecture_diagram.png
        :alt: stateful architecture
     
     - 
     .. image:: https://diagrams.mingrammer.com/img/advanced_web_service_with_on-premise.png
        :target: https://diagrams.mingrammer.com/img/advanced_web_service_with_on-premise.png
        :alt: advanced web service with on-premise
     


You can find all the examples on the `examples <https://diagrams.mingrammer.com/docs/getting-started/examples>`_ page.

Contributing
------------

To contribute to diagram, check out `contribution guidelines <CONTRIBUTING.md>`_.

..

   Let me know if you are using diagrams! I'll add you in showcase page. (I'm working on it!) :)


Who use it?
-----------


.. image:: https://gitpitch.com/gpimg/logo.png
   :target: https://gitpitch.com/
   :alt: GitPitch


`GitPitch <https://gitpitch.com/>`_ is a markdown presentation service for developers. Diagrams is now integrated as `Cloud Diagram Widget <https://gitpitch.com/docs/diagram-features/cloud-diagrams/>`_ of GitPitch, so you can use the Diagrams when to create slide decks for Tech Conferences, Meetups, and Training with GitPitch.

License
-------

`MIT <LICENSE>`_
