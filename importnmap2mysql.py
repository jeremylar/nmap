import xml.etree.ElementTree as ET
import MySQLdb
import datetime
nmapdb = MySQLdb.connect(host="localhost", user="root", passwd="passwd", db="nmap")
cursor = nmapdb.cursor()
hostsql = "INSERT INTO hosts (timeofscan,ipaddress,hostname,osname,accuracy) values(%s,%s,%s,%s,%s);" 
portsql = "INSERT INTO ports (timeofscan,ipaddress,protocol,portid,state,reason,reason_ttl,servicename) values(%s,%s,%s,%s,%s,%s,%s,%s);"
tree = ET.parse('/home/shieldadmin/nmap3.xml')
root = tree.getroot()	
for host in root.iter('host'):
	hosts=[]
	timescan = int(host.get('starttime'))
	timeof = (datetime.datetime.fromtimestamp(timescan).strftime('%Y-%m-%d %H:%M:%S'))
	for address in host.iter('address'):
		addr = address.get('addr')
	for hostnames in host.iter('hostnames'):
		if len(hostnames.findall('hostname')) > 0:
			for hostname in host.iter('hostname'):
				hostn = hostname.get('name')
		else: 
			hostn = "none"
	for os in host.iter('osmatch'):
		osname = os.get('name')
		accuracy = os.get('accuracy')
	hosts.append(timeof)
	hosts.append(addr)
	hosts.append(hostn)
	hosts.append(osname)
	hosts.append(accuracy)
	cursor.execute(hostsql,hosts)
	for port in host.iter('port'):
		ports=[]
		ports.append(timeof)
		ports.append(addr)
		ports.append(port.get('protocol'))
		ports.append(port.get('portid'))
		for state in port.iter('state'):
			ports.append(state.get('state'))
			ports.append(state.get('reason'))
			ports.append(state.get('reason_ttl'))
		for service in port.iter('service'): 
			ports.append(service.get('name'))
		cursor.execute(portsql,ports)
nmapdb.commit()
cursor.close()
nmapdb.close()	