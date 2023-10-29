## Configurations

Check the raspeberry pie 4B documentation for more details. https://www.raspberrypi.com/documentation/computers/raspberry-pi.html

Main channels are more stable to provide electricity for the Raspberry Pie(based on our experience).

The connections should be done as the following steps:
```shell
1 Set up the USB-to-USB Cable (better not use any adapters)
2 Use an crocodile clip to connect the power output positive port to the 5V power pin
3 Use another crocodile clip to connect the power output negative port to the ground pin
4 power on the monsoon monitor (make sure all the connections are correct before then)
5 Run the SimpleSamplingExample.py script
```
## Run
Run the following command **in the folder** `greenlab/experiment-runner/examples/greenlab-profiling/MonsoonSampling`:

```shell
python SimpleSamplingExample.py
```
Then the power readings are sampled 5000 times per second, the result is stored in `HV Output.csv`

Dont forget to start the Experiment Runner because the monitor has already begun recording right now!

When you want to stop sampling, type `control+C` on the keyboard, this will break the sampling process

The sampling data should be copied to the path `greenlab/experiment-runner/examples/greenlab-profiling` for performing the next merging stage

