.. _quick_start:

Quick Start
===========

Making a request to a Polytope service is made simple by using *polytope-client*. The following snippet is all you need to start downloading data.

.. code-block:: bash

    # install the client
    pip install polytope-client
    
    # set your credentials
    export POLYTOPE_USERNAME=polly
    export POLYTOPE_PASSWORD=tope

    # set the URL of the polytope-server
    export POLYTOPE_ADDRESS=polytope.example.com

    # see what collections are available
    polytope list collections

    # construct a request
    cat > request.json <<EOF
    {
        "year" : 2018
        "parameter" : [ "population", "GDP" ]
        "country" : [ "ALL" ]
    }
    EOF

    # submit the request and download the data
    polytope retrieve census-data request.json result.json


The credentials you use, the collections that you access and the format of the request will all depend on the configuration of the *polytope-server* which you speak to. The following sections explain in more detail.