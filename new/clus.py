import os
import subprocess as sp

sp.getoutput("ssh 192.168.43.187 yum install httpd -y -''")
sp.getoutput("ssh 192.168.43.187 cat > /var/www/html/idex.html")
sp.getoutput("systemctl restart httpd")
#sp.getoutput("systemctl stop firewalld")
#sp.getoutput("systemctl disable firewalld")


