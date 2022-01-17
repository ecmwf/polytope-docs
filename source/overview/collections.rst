.. _collections:

Collections and Datasources
===========================

The configuration of the *polytope-server*, in terms of collections and datasources, determines what users will be able to access and how they should describe their requests.

Datasources
-----------

Polytope acts as a unified API for accessing different kinds of data storage backend (`datasources`). Polytope currently supports the following datasources:

* ECMWF's open-source `FDB <https://github.com/ecmwf/fdb/>`_ object store
* ECMWF's `public web service <https://confluence.ecmwf.int/display/WEBAPI/Access+MARS/>`_ for the MARS meteorological archive
* ECMWF's proprietary service for direct access to MARS meteorological archive
* A Polytope proxy datasource which forwards requests to other instances of Polytope

When a user makes a request to Polytope, the user-provided request string (usually JSON/YAML) is sent to the datasource handler along with various metadata about the request (including user attributes and roles). The datasource handles this request and passes the result back to Polytope.

Collections
-----------

`Collections` group datasources together into a common endpoint for the user-facing API (see :ref:`rest_api`). All datasources in a collection should accept the same request format. Polytope will try each datasource in a collection in turn until the request has been successfully processed.

Collections are also the level at which role-based access control is set, so different users can be granted access to different collections. There are also quality of service (QoS) options for collections to control the number of simultaneous requests allowed by a user.

The configuration file of the Polytope server is where all the datasources and collections are specified, including QoS limits and role-based access control. See :ref:`server_configuration`.

