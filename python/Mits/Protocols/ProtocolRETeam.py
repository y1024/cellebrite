"""
Written By: Nadav Horesh
#this is for the change_baudrate_function
import hashlib
class ProtocolRETeam(object):
    class Commands:
        PROB_NAND       = "PRBN"   
        
    def __init__(self, framer, safe_recv = False):
    def init_bootloader(self, param_vector):
                

    def mmc_init(self, version = 0):
    def mmc_read(self, block_start, block_count,ram_address):

    def nand_init(self, page_size, spare_size, block_size, block_count, width):

    def invalidate_cache(self):

    def rpc(self,address,arg0=0,arg1=0,arg2=0,arg3=0,arg4=0):

    def ping(self, string,shouldPrint=True):
    def debug_print(self):
    def test_params(self, param_list):
    def write_ram(self, address, data, max_retry_count = 10):
            res = self.write_ram(address + offset, data[offset:offset+length])
    def finish(self):
    def scan_mem(self, start=0, end=0x100000000, step=0x10000):