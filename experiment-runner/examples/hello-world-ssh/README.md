# Test SSH Connection

Please add a file named `fabconfig.yaml` to `experiment-runner` folder with the following content:

```yaml
hosts:
  raspberrypi:
    hostname: xxx.xxx.xxx.xxx 
    user: xxx
    password: "xxx"
```

and run the following command:

```shell
python experiment-runner/ examples/hello-world-ssh/RunnerConfig.py
```
