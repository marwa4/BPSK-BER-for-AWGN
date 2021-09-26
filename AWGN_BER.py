
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as nr
from scipy.stats import norm


BlockLength = 10000000 # transmitted symbols
SNRdB = np.arange(1.0,14.1) # SNR range in dB
BER = np.zeros(SNRdB.size) # Initialization of the BER vector
SNR = 10**(SNRdB/10) # from dB to linear
Sym = 2*nr.randint(2,size=BlockLength)-1 # generation of BPSK symbols (-1, 1) the average power is P = 1


noise = nr.normal(0.0,1.0,BlockLength) # Generation of white noise with 0 mean and noise power  1

for itersnrdB in range(SNRdB.size):
    Txbits = np.sqrt(SNR[itersnrdB])*Sym # different SNRs symbol
    Rxbits = Txbits+noise # add noise
    Decbits = 2*(Rxbits>0)-1 # detection with threshold 0
    BER[itersnrdB] = BER[itersnrdB]+np.sum(Decbits!=Sym) # count number of bit errors

BER = BER/BlockLength # over the number of total bits

plt.yscale('log')
plt.plot(SNRdB, BER, 'go')
plt.plot(SNRdB, 1-norm.cdf(np.sqrt(SNR)),'r-') # Qfunction for Pe (cdf = 1-qf)
plt.grid(1,which = 'both')
plt.suptitle('BER for AWGN')
plt.xlabel('SNR (dB)')
plt.ylabel('BER')
plt.legend(['Experiments', 'Theory'])
plt.show()
