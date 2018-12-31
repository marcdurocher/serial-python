# serial-python

## Experiments around Python functions serialization.


__Endpoint.py__ exposes a function as "REST RPC" service.
(Listening on port 8080 from the localhost currently)

The function attached to this HTTP endpoint is loaded from a serialized form, form the file system.

The goal is to decouple the creation of the function and its consumation as a "REST API".

The function used here is a predictive function, result of a trained model, using sckit learn framework. 
The algorithm used is a linear regression. The data are production using a predefined linear function.
The model tries to fit thie function.

## Example

The initial linear function is the following one:  
>
    def f(x):
       r = x * 250 + 3
       return r

Service launch
> python -m modele.endpoint --file function.bin

where function.bin is the path to the file containing the serialized function estPair

Service call
> wget -qO - http://localhost:8080/api/3

Result
> {"value": 3, "prediction": 752.9999999999568}

 
 
 ## Docker image
 
 To build the Docker image
 
 > docker build -t marc.durocher/serial-python .
 
 To run a container from this image
 
 > docker run --rm --net=host -it marc.durocher/serial-python
 
 Using the host network (form docker container point of view) you can call the service the same way as previously
 > wget -qO - http://localhost:8080/api/13
 
 _Enjoy..._
 
 _CU_
