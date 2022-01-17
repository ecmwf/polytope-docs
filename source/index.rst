Welcome to Polytope's documentation!
====================================

`Polytope <https://github.com/ecmwf-projects/polytope-server>`_ is an open-source web service designed to provide efficient access to hypercubes of data in scientific analysis workflows, and is able to federate access between hypercubes in distributed computing resources. It is designed to couple data-centric workflows operating across multiple platforms (HPC, cloud) and across multiple distributed sites.

Users can access the Polytope service via the REST API exposed by Polytope, or via the `polytope-client <https://github.com/ecmwf-projects/polytope-client>`_ Python package. The client includes a Python API and a command line tool (CLI) for accessing Polytope services.


Features
--------

* Efficient web-based access to a variety of datacube datasources under a common API
* Robust role-based and attribute-based access control, including quality-of-service limits
* Micro-service design, able to be deployed and scaled on Kubernetes and Docker Swarm
* Compatible and extendable to a variety of authentication providers (e.g. Keycloak, LDAP, SSO)
* Federation of multiple Polytope instances, connecting distributed storage infrastructure
* [WIP] Server-side polytope-based subsetting and feature extraction

Packages
--------

* `polytope-server <https://github.com/ecmwf-projects/polytope-server>`_
* `polytope-client <https://github.com/ecmwf-projects/polytope-client>`_
* `polytope-deployment <https://github.com/ecmwf-projects/polytope-deployment>`_
* `polytope-docs <https://github.com/ecmwf-projects/polytope-docs>`_


License 
-------

*Polytope* is available under the open source `Apache License`__. In applying this licence, ECMWF does not waive the privileges and immunities granted to it by virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

__ http://www.apache.org/licenses/LICENSE-2.0.html

----

.. toctree::
   :maxdepth: 1
   :caption: Overview

   overview/quick_start
   overview/collections
   overview/authentication

.. toctree::
   :maxdepth: 1
   :caption: Client

   client/rest_api
   client/python_api

.. toctree::
   :maxdepth: 1
   :caption: Server

   server/design
   deployment/deployment
   deployment/https
   server/telemetry
   server/federation

.. toctree::
   :maxdepth: 1
   :caption: Reference

   reference/rest_api_reference
   reference/server_configuration

Polytope has been developed at ECMWF as part of the EU projects `LEXIS <https://lexis-project.eu/web/>`_ and `HiDALGO <https://hidalgo-project.eu/>`_. The LEXIS and HiDALGO projects have received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreements No. 825532 and No. 824115.