#!/usr/bin/env python

# Nama  : Nabila Zahra Salsabila
# NIM   : 191344021
# Kelas : 4-TNK

import sys

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi

def topology(args):

    net = Mininet_wifi()

    info("*** Creating nodes\n")
    h1 = net.addHost( 'h1', mac='00:00:00:00:00:01', ip='10.0.0.1/8' )
    sta1 = net.addStation( 'sta1', mac='00:00:00:00:00:02', ip='10.0.0.2/8', range='20' )
    sta2 = net.addStation( 'sta2', mac='00:00:00:00:00:03', ip='10.0.0.3/8', range='20' )
    sta3 = net.addStation( 'sta3', mac='00:00:00:00:00:04', ip='10.0.0.4/8', range='20' )
    sta4 = net.addStation( 'sta4', mac='00:00:00:00:00:05', ip='10.0.0.5/8', range='20' )
    sta5 = net.addStation( 'sta5', mac='00:00:00:00:00:06', ip='10.0.0.6/8', range='20' )
    sta6 = net.addStation( 'sta6', mac='00:00:00:00:00:07', ip='10.0.0.7/8', range='20' )
    sta7 = net.addStation( 'sta7', mac='00:00:00:00:00:08', ip='10.0.0.8/8', range='20' )
    sta8 = net.addStation( 'sta8', mac='00:00:00:00:00:09', ip='10.0.0.9/8', range='20' )
    ap1 = net.addAccessPoint( 'ap1', ssid= 'ap1-ssid', mode= 'g', channel= '1', position='35,60,0', range='30' )
    ap2 = net.addAccessPoint( 'ap2', ssid= 'ap2-ssid', mode= 'g', channel= '1', position='35,100,0', range='30' )
    ap3 = net.addAccessPoint( 'ap3', ssid= 'ap3-ssid', mode= 'g', channel= '1', position='60,130,0', range='30' )
    ap4 = net.addAccessPoint( 'ap4', ssid= 'ap4-ssid', mode= 'g', channel= '1', position='100,130,0', range='30' )
    ap5 = net.addAccessPoint( 'ap5', ssid= 'ap5-ssid', mode= 'g', channel= '1', position='125,100,0', range='30' )
    ap6 = net.addAccessPoint( 'ap6', ssid= 'ap6-ssid', mode= 'g', channel= '1', position='125,60,0', range='30' )
    ap7 = net.addAccessPoint( 'ap7', ssid= 'ap7-ssid', mode= 'g', channel= '1', position='100,30,0', range='30' )
    ap8 = net.addAccessPoint( 'ap8', ssid= 'ap8-ssid', mode= 'g', channel= '1', position='60,30,0', range='30' )
    c1 = net.addController( 'c1' )
	
    info("*** Configuring propagation model\n")
    net.setPropagationModel(model="logDistance", exp=4.5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Associating and Creating links\n")
    net.addLink(ap1, h1)
    net.addLink(ap1, ap2)
    net.addLink(ap2, ap3)
    net.addLink(ap3, ap4)
    net.addLink(ap4, ap5)
    net.addLink(ap5, ap6)
    net.addLink(ap6, ap7)
    net.addLink(ap7, ap8)
    net.addLink(ap8, ap1)

    if '-p' not in args:
        net.plotGraph(max_x=160, max_y=160)
	
    net.startMobility(time=0, ac_method='ssf')
    net.mobility(sta1, 'start', time=1, position='35,60,0')
    net.mobility(sta1, 'stop', time=2, position='35,100,0')
    net.stopMobility(time=5)
  
    net.startMobility(time=0, ac_method='ssf')
    net.mobility(sta2, 'start', time=5, position='35,100,0')
    net.mobility(sta2, 'stop', time=6, position='60,130,0')
    net.stopMobility(time=9)  
    
    net.startMobility(time=0, ac_method='ssf')
    net.mobility(sta3, 'start', time=9, position='60,130,0')
    net.mobility(sta3, 'stop', time=10, position='100,130,0')
    net.stopMobility(time=13)  
    
    net.startMobility(time=0, ac_method='ssf')
    net.mobility(sta4, 'start', time=13, position='100,130,0')
    net.mobility(sta4, 'stop', time=14, position='125,100,0')
    net.stopMobility(time=17)  
    
    net.startMobility(time=0, ac_method='ssf')
    net.mobility(sta5, 'start', time=17, position='125,100,0')
    net.mobility(sta5, 'stop', time=18, position='125,60,0')
    net.stopMobility(time=21)  
    
    net.startMobility(time=0, ac_method='ssf')
    net.mobility(sta6, 'start', time=21, position='125,60,0')
    net.mobility(sta6, 'stop', time=22, position='100,30,0')
    net.stopMobility(time=25)  
    
    net.startMobility(time=0, ac_method='ssf')
    net.mobility(sta7, 'start', time=25, position='100,30,0')
    net.mobility(sta7, 'stop', time=26, position='60,30,0')
    net.stopMobility(time=29)  
    
    net.startMobility(time=0, ac_method='ssf')
    net.mobility(sta8, 'start', time=29, position='60,30,0')
    net.mobility(sta8, 'stop', time=30, position='35,60,0')
    net.stopMobility(time=33)  
    
    info("*** Starting network\n")
    net.build()
    c1.start()
    ap1.start([c1])
    ap2.start([c1])
    ap3.start([c1])
    ap4.start([c1])
    ap5.start([c1])
    ap6.start([c1])
    ap7.start([c1])
    ap8.start([c1])

    info("*** Running CLI\n")
    CLI( net )

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology(sys.argv)
