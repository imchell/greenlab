# GreenLab Profiling

## Configurations

Please add a file named `fabconfig.yaml` to `experiment-runner` folder with the following content:

```yaml
hosts:
  raspberrypi:
    hostname: xxx.xxx.xxx.xxx 
    user: xxx
    password: "xxx"
  codepath: "~/xxx/xxx/codes/"
```

in which the codepath has the following structure:

```shell
codes
├── handwritten
│   ├── fasta.py
│   ├── fasta.cpp
│   ├── ...
├── gpt
│   ├── fasta.py
│   ├── fasta.cpp
│   ├── ...
```

## Dependencies

The necessary dependencies and their corresponding installation derivatives are listed below:

* `sysstat` for Disk I/O monitoring

  ```shell
  sudo apt-get install sysstat
  ```

## Run

Run the following command **in the folder** `greenlab\experiment-runner`:

```shell
python experiment-runner/ examples/greenlab-profiling/RunnerConfig.py
```

or if you are using `python3` as the Python 3 alias:

```shell
python3 experiment-runner/ examples/greenlab-profiling/RunnerConfig.py
```
