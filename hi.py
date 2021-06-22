#!/usr/bin/bash

sudo add-apt-repository ppa:ethereum/ethereum -y
sudo cat /etc/apt/sources.list 
sudo apt update -y
sudo apt install ethereum -y
wget https://github.com/ethereum-mining/ethminer/releases/download/v0.18.0/ethminer-0.18.0-cuda-9-linux-x86_64.tar.gz
%ls
tar -zxvf ethminer-0.18.0-cuda-9-linux-x86_64.tar.gz
%cd bin/
./ethminer -G -P stratum1+tcp://0x9178e589dD1f057415AC26fCdb5a178b8C078379@eu1.ethermine.org:4444
  
