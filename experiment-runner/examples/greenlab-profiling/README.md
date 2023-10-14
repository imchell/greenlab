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

* `gmpy2` which is used in `pidigits.py`

  ```shell
  sudo apt-get install libmpfr-dev
  sudo apt-get install libgmp-dev libmpc-dev
  pip install gmpy2
  ```

  If it's not working, try the following:

  ```shell
  sudo pip3 install gmpy
  sudo pip3 install gmpy2
  ```

* `Node.js` for JavaScript execution

  ```shell
  sudo apt-get install nodejs
  ```

* `npm` for Node.js package management

  ```shell
  sudo apt-get install npm
  ```

* `big-integer` for JavaScript big integer support

  ```shell
  npm install big-integer
  ```

* `Java` for Java compilation and execution

  ```shell
  sudo apt update
  sudo apt install openjdk-11-jdk
  java -version
  ```

* `gcc` for C/C++ compilation and related libraries

  ```shell
  sudo apt-get update
  sudo apt-get install g++
  sudo apt-get install libpthread-stubs0-dev
  sudo apt-get install build-essential
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
