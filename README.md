# serial-python

## Experiments around Python functions serialization.


__Endpoint.py__ exposes a function as "REST RPC" service.
(Listening on port 8080 from the localhost currently)

The function attached to this HTTP endpoint is loaded from a serialized form, form the file system.

The goal is to decouple the creation of the function and its consumation as a "REST API".

This function could be a trained model seralized form a machine learning framework.  

## Example

Service launch
> python -m modele.endpoint --file estpair.bin

where estpair.bin is the path to the file containing the serialized function estPair

Service call
> wget -qO - http://localhost:8080/api/13

Result
> {"number": 13, "estPair": false}


Function __estpair__
> def estpair(n):  return n % 2 == 0
 
 
 ## Docker image
 
 To build the Docker image
 
 > docker build -t marc.durocher/serial-python .
 
 To run a container from this image
 
 > docker run --rm --net=host -it marc.durocher/serial-python
 
 
 _Enjoy..._
 
 _CU_
