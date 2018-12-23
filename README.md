# serial-python
Experiments around Python functions serialization.

__Endpoint.py__ exposes a function as "REST RPC" service.
(Listening on port 8080 from the localhost currently)

The function attached to this HTTP endpoint is loaded from a serialized form, form the file system.

The goal is to decouple the creation of the function and its consumation as a "REST API".

This function could be a trained model seralized form a machine learning framework.  
