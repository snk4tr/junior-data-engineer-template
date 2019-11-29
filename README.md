# Junior Data Engineer task template

This repository in created as a reference solution for Junior Data Engineer technical task.

Expected task completion time: **3h**.

### Testing

Tests have to start from the main run script with additional `Test` parameter:  
`$ bash run.sh <port> Test`

It should test whether the app and it submodules work and whether the model makes correct predictions. 
To test that the app actually returns correct responses on images sent with POST, use `curl`:  
`$ curl -F 'file=@<local file path>' http://<external ip>:<port>/predict`

* **Sergey Kastryulin** - _Initial work_ - `sergey.kastryulin@philips.com` 