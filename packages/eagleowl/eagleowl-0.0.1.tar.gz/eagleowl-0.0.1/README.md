# EagleOwl

A tool for installing sophisticated Kubernetes application consisting of numerous components and intricate configurations.

EagleOwl is distributed as a Python package, officially registered within the Python Package Index (PyPi).  
It support all Python versions since 3.6.

The installation of EagleOwl is straightforward:
```
pip install eagleowl
```

For assistance and command options, use: `eagleowl -h` \
This command provides usage instructions and a list of available options, including but not limited to specifying work directories, setting log levels, and executing install or uninstall commands.

## The design behind the installer

EagleOwl offers a range of functionalities designed to accommodate diverse customer needs, including those with varying Kubernetes cluster configurations and pre-existing Kubernetes resources.

Central to this customization capability is *Application Manifests* — a collection of YAML files outlining the architecture of the application.  
EagleOwl, leveraging *Application Manifests*, acts as a versatile tool capable of applying these Kubernetes resources and configurations to customers' Kubernetes clusters.  
