# Junior Data Engineer task template

This repository is created as a reference solution for Junior Data Engineer technical task.

Expected task completion time: **3h**.


### Requirements
 
* The web-service has to implemented using Flask. Use Docker as an execution and testing environment.
* The application has to be configurable using **config.yaml** file. Only the port of the host machine can be left as a script argument.
* The web-service has to runnable with no more than one or two commands.
* The application should work only on inference and with low load (no more than several RPM). 
* The inference should be possible both on CPU and GPU. 
* The code has to contain tests to check the correctness of the execution of the service.

### Testing

Tests have to start from the main run script with additional `Test` parameter: 
`$ bash run.sh <port> Test`

It should test whether the app and its submodules work and whether the model makes correct predictions. 
To test that the app actually returns correct responses on images sent with POST, use `curl`: 
`$ curl -F 'file=@<local file path>' http://<external ip>:<port>/predict`

* **Sergey Kastryulin** - _Initial work_ - `sergey.kastryulin@philips.com` 