# GreenLab

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
