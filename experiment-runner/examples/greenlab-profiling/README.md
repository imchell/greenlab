# GreenLab Profiling

## Green Lab Profiling

We have a separate README for the Green Lab Profiling project, which uses Experiment Runner as its infrastructure. You can find it [here](experiment-runner/examples/greenlab-profiling/README.md).

It lists the steps to reproduce the results of _Comparative Analysis of Energy Efficiency between
ChatGPT-Generated Codes and Handwritten Codes_.

R code for the statistical analysis can be found [here](experiment-runner/examples/greenlab-profiling/r-analysis).

Intermediate results can be found [here](experiment-runner/examples/greenlab-profiling/generated-data).

> **Note**
> Before checking out the Green Lab Profiling, please read the following sections to install the Experiment Runner and try connecting Raspberry Pi with SSH.

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

The necessary dependencies and their corresponding installation derivatives on Raspberry Pi are listed below:

- `sysstat` for Disk I/O monitoring

  ```shell
  sudo apt-get install sysstat
  ```

- `gmpy2` which is used in `pidigits.py`

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

- `Node.js` for JavaScript execution

  ```shell
  sudo apt-get install nodejs
  ```

- `npm` for Node.js package management

  ```shell
  sudo apt-get install npm
  ```

- `big-integer` for JavaScript big integer support

  ```shell
  npm install big-integer
  ```

- `Java` for Java compilation and execution

  ```shell
  sudo apt update
  sudo apt install openjdk-11-jdk
  java -version
  ```

- `gcc` for C/C++ compilation and related libraries

  ```shell
  sudo apt-get update
  sudo apt-get install g++
  sudo apt-get install libpthread-stubs0-dev
  sudo apt-get install build-essential
  ```

- Enter the `~/xxx/xxx/codes/handwritten` folder and run the following command to compile the C/C++ codes:

  ```shell
  g++ -std=c++20 -O3 -o fasta fasta.cpp -lpthread
  g++ -c -pipe -O3 -fomit-frame-pointer -march=native -std=c++14 knucleotide.cpp -o knucleotide.o
  g++ knucleotide.o -o knucleotide -Wl,--no-as-needed -lpthread
  g++ -c -pipe -O3 -fomit-frame-pointer -march=native -std=c++14 -g pidigits.cpp -o pidigits.o
  g++ pidigits.o -o pidigits -lgmp -lgmpxx
  sudo apt-get install g++ libpcre++-dev
  sudo apt-get install libpcre3-dev
  g++ -c -pipe -O3 -fomit-frame-pointer -march=native -std=c++17 -fopenmp -flto regexredux.cpp -o regexredux.o
  g++ regexredux.o -o regexredux -fopenmp -lpcre
  g++ revcomp.cpp -o revcomp -lpthread -O3
  ```

- Enter the `~/xxx/xxx/codes/gpt` folder and run the following command to compile the C/C++ codes:

  ```shell
  g++ fasta.cpp -o fasta
  g++ knucleotide.cpp -o knucleotide -O3
  g++ pidigits.cpp -o pidigits -O3 -lmpfr -lgmp
  g++ regexredux.cpp -o regexredux -O3 -std=c++11
  g++ revcomp.cpp -o revcomp -O3
  ```

- Enter the `~/xxx/xxx/codes/handwritten` folder and run the following command to compile the Java codes:

  ```shell
  javac binarytrees.java
  javac fasta.java
  javac regexredux.java
  javac spectralnorm.java
  javac revcomp.java
  ```

- Enter the `~/xxx/xxx/codes/gpt` folder and run the following command to compile the Java codes:

  ```shell
  javac binarytrees.java
  javac fasta.java
  javac regexredux.java
  javac spectralnorm.java
  javac revcomp.java
  ```

- Enter the `~/xxx/xxx/codes/handwritten` folder and run the following command to compile the C codes:

  ```shell
  gcc fasta.c -o fasta.compiled
  gcc knucleotide.c -o knucleotide.compiled
  gcc pidigits.c -o pidigits.compiled -lgmp -lm
  gcc -pipe -Wall -O3 -fomit-frame-pointer nbody.c -o nbody.compiled -lm
  gcc -pipe -Wall -O3 -fomit-frame-pointer -fopenmp spectralnorm.c -o spectralnorm.compiled -lm
  ```

- Enter the `~/xxx/xxx/codes/gpt` folder and run the following command to compile the C codes:

  ```shell
  gcc fasta.c -o fasta.compiled
  gcc knucleotide.c -o knucleotide.compiled
  gcc pidigits.c -o pidigits.compiled -lgmp -lm
  gcc -pipe -Wall -O3 -fomit-frame-pointer nbody.c -o nbody.compiled -lm
  gcc -pipe -Wall -O3 -fomit-frame-pointer -fopenmp spectralnorm.c -o spectralnorm.compiled -lm
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
