# GreenLab

## Green Lab Profiling

We have a separate README for the Green Lab Profiling project, which uses Experiment Runner as its infrastructure. You can find it [here](experiment-runner/examples/greenlab-profiling/README.md).

It lists the steps to reproduce the results of _Comparative Analysis of Energy Efficiency between
ChatGPT-Generated Codes and Handwritten Codes_.

R code for the statistical analysis can be found [here](experiment-runner/examples/green-lab-profiling/r-analysis/).

Intermediate results can be found [here](experiment-runner/examples/green-lab-profiling/generated-data/).

Before checking out the Green Lab Profiling, please read the following sections to install the Experiment Runner and try connecting Raspberry Pi with SSH.

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
