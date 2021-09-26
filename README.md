# Performance Analysis for Communication Systems 

Bit Error Rate (BER) is a metric which can be employed to characterize the performance of a communication system. In communication system, one transmits bits of information from 
the transmitter to receiver. However, all the transmitted bits are not received correctly by the receiver; frequently there are bit errors occuring during the communication process.

In this first project, we will present the analytical theory behind the probability error of AWGN channel for BPSK modulated transmission. Moreover, we simulate using Python this system model
and we present its bit error rate performance.

The project report contains the definition and the expression of : 
* [Bit Error Rate ](#BER)
* [Information bits ](#Information-bits)
* [Detection at Receiver ](#Detection-at-Receiver)
* [Model of Wireline Communication system ](#Model-of-Wireline-Communication-system)
* [Probability error expression ](#Probability-error-expression)


## BER
The BER is the average rate of bit error. For instance, if 10 000 bits are transmetted and 100 bits are received in error, then the average BER:

![equation1](https://latex.codecogs.com/gif.latex%5Cfrac%7B%5Ctext%7BNumber%20of%20bits%20in%20error%7D%7D%7B%5Ctext%7BTotal%20number%20of%20bits%20transmitted%7D%7D%20%3D%20%5Cfrac%7B100%7D%7B10000%7D%20%3D%201%25)

Since the transmitted and the received bits are random quantities, the BER can also be expressed as probability known as the probability of bit error.

## Information bits

Note that the information bits are modulated prior to transmission over the channel. One such modulation format is BPSK : Binary Phase Shift Keying, in which, the information symbol 0 is modulated as []!(https://latex.codecogs.com/gif.latex?%5Csqrt%7BP%7D) and the infomation symbol 1 is modulated as 
[]!(https://latex.codecogs.com/gif.latex?-%5Csqrt%7BP%7D).
So, there are two phases 0 and 180 degrees. The average power of this modulation format is P.

## Detection at Receiver

If the received symbol >= 0 then it is mapped to the binary information 0 else it is mapped to 1. In this case, 0 is the threshold.
This is a threshold based detection.

## Model of Wireline Communication system

In the figure bellow, we present a simple model of a wireline communication system, where x is the transmitted symbol, y the received symbol and n is the noise at the receiver.

![](Figure/modelAWGN.png)

If the noise process is a white Gaussian, then the system model is a AWGN (additive White Gaussian Noise). 
The noise probability density function for a zero 0 and noise power ![](https://latex.codecogs.com/gif.latex?%5Csigma%5E2) is given by: 

![equation](https://latex.codecogs.com/gif.latex?F_N%28n%29%20%3D%20%5Cfrac%7B1%7D%7B%5Csqrt%7B2%5Cpi%20%5Csigma%5E2%7D%7De%5E%7B-%5Cfrac%7Bn%5E2%7D%7B2%5Csigma%5E2%7D%7D)

The shape of the pdf is as depicted in the Figure below:

![](Figure/pdfnoise.png)

## Probability error expression


Consider ![](https://latex.codecogs.com/gif.latex?x%3D%201%20%3D%20-%5Csqrt%7BP%7D), then the received symbol ![](https://latex.codecogs.com/gif.latexy%20%3D%20x&plus;%20n%20%3D%20-%5Csqrt%7BP%7D%20&plus;%20n).
The bit error occurs if ![](https://latex.codecogs.com/gif.latex?y%20%5Cgeq%200) meaning ![](https://latex.codecogs.com/gif.latex?n%20%5Cgeq%20%5Csqrt%7BP%7D)


Therefore, the probability of error is given by:

![equation1](https://latex.codecogs.com/gif.latex?P%28n%20%5Cgeq%20%5Csqrt%7BP%7D%29%20%3D%20%5Cint_%7B%5Csqrt%7BP%7D%7D%5E%7B%5Cinfty%7D%20F_N%28n%29dn%20%3D%20%5Cint_%7B%5Csqrt%7BP%7D%7D%5E%7B%5Cinfty%7D%20%5Cfrac%7B1%7D%7B%5Csigma%20%5Csqrt%7B2%5Cpi%7D%7De%5E%7B-%5Cfrac%7Bn%5E2%7D%7B2%5Csigma%5E2%7D%7Ddn%20%3D%20%5Cint_%7B%7B%5Cfrac%7B%5Csqrt%7BP%7D%7D%7B%5Csigma%7D%7D%7D%5E%7B%5Cinfty%7D%20%5Cfrac%7B1%7D%7B%5Csqrt%7B2%5Cpi%7D%7De%5E%7B-%5Cfrac%7Bt%5E2%7D%7B2%7D%7Ddt)

This corresponds to the ![](https://latex.codecogs.com/gif.latex?Q%28%5Csqrt%7B%5Cfrac%7BP%7D%7B%5Csigma%5E2%7D%7D%29) where Q is the qfunction, and it is expressed by:
![equation1](https://latex.codecogs.com/gif.latex?Q%28v%29%20%3D%20%5Cint_v%5E%7B%5Cinfty%7D%20%5Cfrac%7B1%7D%7B%5Csqrt%7B2%5Cpi%7D%7D%20e%5E%7B-%5Cfrac%7Bt%5E2%7D%7B2%7D%7Ddt)

To sum up, the probability of bit error in AWGN channel for BPSK modulated transmission of average power P is given by:
![equation1](https://latex.codecogs.com/gif.latex?Q%28%5Csqrt%7B%5Cfrac%7BP%7D%7B%5Csigma%5E2%7D%7D%29)


By defining the SNR : Signal to Noise Power Ratio by : 

![equation1] (https://latex.codecogs.com/gif.latex?%5Ctext%7BSNR%7D%20%3D%20%5Cfrac%7BP%7D%7B%5Csigma%5E2%7D)

Then, the probability of error is thus ![](https://latex.codecogs.com/gif.latex?P_e%20%3D%20Q%28%5Csqrt%7B%5Ctext%7BSNR%7D%7D%29).

Through our simulation using Python, the resulted BER curve against the theoretical probability of error is depicted in the figure below: 

![](Figure/berawgn.png)

