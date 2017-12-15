"""
THIS SCRIPT SORTS RFC1918 ADDRESSES
"""

list_of_ip = ["192.168.0.1", "192.168.0.2", "172.16.0.1", "172.30.0.1", "10.0.0.1", "10.255.0.0", "8.8.8.8"]

list_of_192 = ["192", "168"]
list_of_172 = ["172"]
list_of_10 = ["10"]

list_of_init = []
list_of_rfc1918 = []
list_of_others = []

print "\nHere are your ip's:\n%s\n" % (list_of_ip)

def split_ip():
   print "Here are your octets:"
   for x in list_of_ip:
      x = x.split('.')
      print x
      list_of_init.append(x)

   print "\nStarting Loop:"

   for ip in list_of_init:
      if ip[0:2] == list_of_192:
         print "adding %s to list_of_rfc1918" % (ip)
         list_of_rfc1918.append(ip)

      elif ip[0:1] == list_of_172:
         print "adding %s to list_of_rfc1918" % (ip)
         list_of_rfc1918.append(ip)

      elif ip[0:1] == list_of_10:
         print "adding %s to list_of_rfc1918" % (ip)
         list_of_rfc1918.append(ip)

      else:
         print "Address %s not in RFC1918" % (ip)
         list_of_others.append(ip)
         continue


   print "ENDING LOOP\n"
   print "\nRFC1918:"
   for x in sorted(list_of_rfc1918):
      print x  

   print "\nOTHER ADDRESSES:"
   for x in list_of_others:
      print x

split_ip()




