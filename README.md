RadioDNS-plugit
===============

## /!\ THIS PROJECT IS UNDER HEAVY REFACTORING. IT IS ADVISED TO WAIT THE NEXT RELEASE AS IT WILL HAVE BREAKING CHANGES /!\

This project gathers a web interface based on [plugit](https://github.com/ebu/plugit) to manage RadioDNS
services ([RadioVIS, RadioEPG and ServiceFollowing](http://www.radiodns.org)). 

Check each folder for specifics README about each part.

## How to run in local without installing dependencies
To start up a local instance

```
docker-compose -f docker-compose-standalone.yml up --build -d
```

Then you may visit http://localhost:4000.

To shut down the local instance

```
docker-compose -f docker-compose-standalone.yml down
```

To remove the database and start afresh

```
docker-volume rm radiodns-plugit_db_data
docker-volume rm radiodns-plugit_mock_api_data
```

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and
testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
- python 2.7 and 3.7
- docker 18.06.1+
- virtualenv 16.0.0+
- docker-compose 1.23.2+

### Installing
To install automatically the python environment on an unix system use the `setup-envs.sh` script (in the scripts folder).

On windows you'll have to setup a virtual env for the following projects (create and activate the venv + installing pip 
dependencies):
- LightweightPlugitProxy (python2)
- RadioDns-PlugIt (python2)
- RadioVisServer (python2)
- MockApi (python3)
- tests (python3)

## How to run tests
If you haven't already, run the `setup-envs.sh` (if you are on an unix based system, script located in the scripts folder).
Then set your working directory to the tests folder and read its README for further instructions.
    
## Deployment in production - EBU.io
Deployment instructions on a production server are detailed in [the docs](/docs/Radiodns_manual_deployment_EBU-IO.md).

## Deployment in production - standalone
Deployment instructions on a production server without EBU.io are detailed in [the docs](/docs/Radiodns_manual_deployment.md).

## General architecture
Architecture is described in [the docs](/docs/Radiodns_architecture.md)

## Contributing
- Always fix version of dependencies.
- Any new module that can be written in python 3 must be written in python 3.
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Contact
Contact the EBU (Ben Poor poor@ebu.ch) if you need more information about RadioDNS and its associated developments.

## Contributors
* Maximilien Cuony [@the-glu](https://github.com/the-glu)
* Malik Bougacha [@gcmalloc](https://github.com/gcmalloc)
* Michael Barroco [@barroco](https://github.com/barroco)
* Mathieu Habegger [@mhabegger](https://github.com/mhabegger)
* Ioannis Noukakis [@inoukakis](https://github.com/ioannisNoukakis)


## Copyright & License
The code is under GPLv3 License. (see LICENSE.txt)
