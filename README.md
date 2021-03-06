Jenkins automation testing framework for iX projects
===========

The scripts in this repo will allow you to test iX projects, either as an automated job from Jenkins or manually.

It includes support to test the following projects:

 * FreeNAS
 * TrueOS

Requirements
============

Recommended hardware:
* CPU: 1 Cores or more
* Memory: 16GB
* Disk: 100GB
* Wired ethernet connection for vm-bhyve bridge

Required OS:

* [TrueOS](http://download.trueos.org/master/amd64/)

Required Packages:

* See Run Depends in port Makefile

Jenkins Requirements:
* One master node
* Slave nodes for running ixautomation

Required Jenkins Plugins:

* [Log parser](https://wiki.jenkins.io/display/JENKINS/Log+Parser+Plugin)
* [Workspace Whitespace Replacement](https://wiki.jenkins.io/display/JENKINS/Workspace+Whitespace+Replacement+Plugin)
* [Copy Artifact](https://wiki.jenkins.io/display/JENKINS/Copy+Artifact+Plugin)
* [Xvfb Plugin](https://wiki.jenkins.io/display/JENKINS/Xvfb+Plugin)
* [Workspace Cleanup](https://wiki.jenkins.io/display/JENKINS/Workspace+Cleanup+Plugin)


Getting Started
============

To prep a new system for testing, first download the repo:

```
git clone --depth=1 https://github.com/iXsystems/ixautomation.git
```

Enter the directory for installing ixautomation from git:

```
cd ixautomation/src/
```

Install the framework
```
sudo python3.6 setup.py install
```

VM Tests
============

Make sure vm-bhyve is enabled, and we set the vm location for ixautomation

```
sysrc -f /etc/rc.conf vm_enable="YES"
sysrc -f /etc/rc.conf vm_dir="/usr/local/ixautomation/vms"
```

Specify a connected ethernet interface with access to DHCP for VMs ( Substitue re0 with your interface )

```
sysrc -f /etc/rc.conf ixautomation_iface="re0"
```

Add the ixautomation service

```
rc-update add ixautomation
```

Start the ixautomation service

```
service ixautomation start
```

Copy ixautomation conf.dist to ixautomation.conf 

```
cp /usr/local/etc/ixautomation.cfg.dist /usr/local/etc/ixautomation.cfg
```

Edit ixautomation.cfg

```
edit /usr/local/etc/ixautomation.cfg
```

Set location of git repo with tests when running local

```
# When running outside of jenkins set WORKSPACE to the path of the local git repo containing tests
WORKSPACE="/home/jmaloney/projects/ixsystems/ixautomation"
export WORKSPACE
```

Create a VM, and test install using vm-bhyve

```
sudo ixautomation --run vm-tests --systype freenas
sudo ixautomation --run vm-tests --systype trueos
```

Selenium Tests
============

Test webui with selenium
```
ixautomation --run webui-test --systype freenas
```
