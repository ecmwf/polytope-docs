.. _authentication:

Authentication and Authorization
================================

Polytope can handle user authentication, authorization and identity (AAI) by itself, using MongoDB as a database of users. However, it is possible (and recommended) to configure Polytope server to connect to dedicated services for these purposes.

The configuration of the *polytope-server*, in terms of AAI, determines what kind of credentials users will have to provide in order to communicate with the server.

Authentication
--------------

`Authentication` is performed whenever a user accesses a secure endpoint of the Polytope service. The purpose of authentication is to check that the user is who they say they are. The authentication services may annotate specific attributes to the user. Polytope server currently supports the following services for authentication:

* Polytope's own MongoDB user database
* Keycloak
* ECMWF's single sign-on system
* Plain -- user credentials specified in the configuration file directly

The unintuitively named ``Authorization`` HTTP header is used to pass the authentication credentials of the user. These credentials are typed depending on the format of the credentials (Basic, Bearer, EmailKey, etc.). The credentials will be checked against all compatible authentication providers, and the first successful authentication will be used. The original credentials are not stored by Polytope, except briefly in process memory.

For example::

    Authorization: Bearer XXXX-API-KEY-XXXX
    Authorization: EmailKey polly@polytope.com:XXXX-API-KEY-XXXX
    Authorization: Basic base64(username:password)


Authorization
-------------

Following authentication, `authorization` is performed to determine which roles the user has, which are later used to determine if they can access protected resources (such as collections or admin-only endpoints). The authorization services may also annotate specific attributes to the user. Polytope server supports the following services for authorization:

* Polytope's own MongoDB user database
* LDAP
* Plain -- user roles specified in the configuration file directly

Polytope will visit all authorization providers, appending all roles and attributes gathered from the different providers.

Identity
--------

Identity is the ability to create, delete, and manage users. For external authentication services, identity should be handled externally. For Polytope's own MongoDB user database there is a basic mechanism for creating and deleting users with the ``/api/v1/auth/users`` (``POST`` & ``DELETE``) endpoint.

API keys
--------

Users are able to generate long-lived API keys by POSTing to ``/api/v1/auth/keys`` with valid authentication credentials. This provides them with a Bearer token which can be used instead of their original credentials. The original credentials are not stored, and the original authentication provider will not be re-contacted. A special API key authenticator is used instead. Authorization providers will still be revisited.

Realms
------

A single instance of Polytope can be configured with many authentication and authorization providers. This can cause issues with username conflicts when the same identities are assigned in different providers. For example, an admin user `polly` may be authenticated using the `plain` authenticator (credentials specified in the config file), and given administrator roles using a `plain` authorizer. Later, a keycloak authenticator might be used which also has a `polly` user -- but it is actually a different user!

If you are not in control of the external AAI providers and their user management, realms allows you to maintain security by differentiating between users in different realms. You don't need to use separate realms for every provider if you won't have username conflicts.

.. note::
   It is perfectly valid to mix and match authentication and authorization providers which deliberately overlap usernames. You may want `polly` the adminstrator to be able to authenticate with Basic attributes, as well as via Keycloak, if they are the same person. The plain authorizer will then add admin roles to `polly` regardless of how she authenticated.

See :ref:`server_configuration` for the full range of options relating to realms, AAI providers and API keys.