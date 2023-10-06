# GreenLab Profiling

Please add a file named `fabconfig.yaml` to `experiment-runner` folder with the following content:

```yaml
hosts:
  raspberrypi:
    hostname: xxx.xxx.xxx.xxx 
    user: xxx
    password: "xxx"
```

and run the following command **in the folder** `greenlab\experiment-runner`:

```shell
python experiment-runner/ examples/greenlab-profiling/RunnerConfig.py
```

or if you are using `python3` as the Python 3 alias:

```shell
python3 experiment-runner/ examples/greenlab-profiling/RunnerConfig.py
```