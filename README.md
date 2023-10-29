# GreenLab

## Green Lab Profiling

We have a separate README for the Green Lab Profiling project, which uses Experiment Runner as its infrastructure. You can find it [here](experiment-runner/examples/greenlab-profiling/README.md).

It lists the steps to reproduce the results of _Comparative Analysis of Energy Efficiency between
ChatGPT-Generated Codes and Handwritten Codes_.

R code for the statistical analysis can be found [here](experiment-runner/examples/greenlab-profiling/r-analysis).

Intermediate results can be found [here](experiment-runner/examples/greenlab-profiling/generated-data).

> **Note**
> Before checking out the Green Lab Profiling, please read the following sections to install the Experiment Runner and try connecting Raspberry Pi with SSH.

## How to Install Experiment Runner

```shell
cd experiment-runner/
pip install -r requirements.txt
```

To verify

```shell
python experiment-runner/ examples/hello-world/RunnerConfig.py
```

or if your Python 3 is not the default Python

```shell
python3 experiment-runner/ examples/hello-world/RunnerConfig.py
```

## Connect with Raspberry Pi via SSH

The IP address of the Raspberry Pi can be found by running

```shell
ifconfig
```

The IP address is the one listed under `eth0`, followed by `inet`, because during the experiment we are using the network cable connection.

Then connect to the Raspberry Pi via SSH

```shell
ssh pi@{IP_ADDRESS}
```

## Dependencies Installation on Raspberry Pi

Check if dependencies are already installed:

```shell
python3 --version
```

### Python 3.9.6

```shell
sudo apt update
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz
tar -xf Python-3.9.6.tgz
cd Python-3.9.6
./configure
make -j 4
sudo make altinstall
```
