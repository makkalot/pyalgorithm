import os
#some configuration variables
IPTABLES_PATH = "/sbin/iptables"
SQUID_SRV = "192.168.1.3"
SQUID_PORT = 6666
CUR_DIR =os.path.abspath(os.path.dirname(__file__).decode('utf-8')) 

import socket
def server_live():
    """
    Simple method checks if can connect to server
    """
    s = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((SQUID_SRV, SQUID_PORT))
    except Exception,e:
        print "Couldnt connect to server ",e
        return False
    return True


def rule_it(add_remove):
    os.system("".join([IPTABLES_PATH," -t nat -",add_remove," PREROUTING -i eth0 -s ! ",SQUID_SRV," -p tcp --dport 80 -j DNAT --to ",SQUID_SRV,":",str(SQUID_PORT)]))
    os.system("".join([IPTABLES_PATH," -t nat -",add_remove," PREROUTING -i eth0 -s ! ",SQUID_SRV," -p tcp --dport 443 -j DNAT --to ",SQUID_SRV,":",str(SQUID_PORT)]))


def set_iptables_rule():
    """
    Will keep a very small db
    """
    if server_live():
    #aktivate iptables to use squid
        rule_it("D")
        rule_it("A")
    else:
        rule_it("D")


if __name__ == "__main__":
    set_iptables_rule()
