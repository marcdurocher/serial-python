# serial-python

## Experiments around Python functions serialization and machine learning productionalization paths

**Model**

The initial linear function is the following one:  
>
    def f(x):
       r = x * 250 + 3
       return r


### First approach : focusing on preditive function and reuse as a REST API
__Endpoint.py__ exposes a function as "REST RPC" service.
(Listening on port 8080 from the localhost currently)

The function attached to this HTTP endpoint is loaded from a serialized form, form the file system.

The goal is to decouple the creation of the function and its consumation as a "REST API".

The function used here is a predictive function, result of a trained model, using sckit learn framework. 
The algorithm used is a linear regression. The data are production using a predefined linear function.
The model tries to fit thie function.

Service launch
> python -m modele.endpoint --file function.bin

where function.bin is the path to the file containing the serialized function estPair

Service call
> wget -qO - http://localhost:8080/api/3

Result
> {"value": 3, "prediction": 752.9999999999568}
 
 #### Docker image
 
 To build the Docker image
 
 > docker build -t marc.durocher/serial-python .
 
 To run a container from this image
 
 > docker run --rm --net=host -it marc.durocher/serial-python
 
 Using the host network (form docker container point of view) you can call the service the same way as previously
 > wget -qO - http://localhost:8080/api/13
 
 
 ### Second approach : generate source code into another programming language like Java
 
 Using the m2cgen library, the trained model with scikit-learn is transform in a Java source class.
 
 Operation in two steps:
 * Train the model, and then serialize the whole model into a file
 * Read back the file and generate a Java file source
 
 
 > python -m modele.generate_ser_model

This generate a file named ml_model.bin into the working directory

Then invoking convert_ser_model_to_java the ml_model.bin is read back and then transformed into a 
Java class named Modelo, into the java package bzh.marcdurocher.prediction, so into a the directory
structure ./bzh/marcdurocher/prediction/

The resulting source code is a below

> cat bzh/marcdurocher/prediction/Modelo.java
 
```
package bzh.marcdurocher.prediction;
 
public class Modelo {

    public static double score(double[] input) {
       return (2.999999999985448) + ((input[0]) * (249.99999999999997));
    }
}
```
 
 _Enjoy..._
 
 _CU_
