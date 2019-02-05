'''
задача 4  - вывести диагностическую информацию рабочей машины  -
 - ЦПУ,
 - оперативная память
   - свободная
   - занятая,
 - диски
   - свободно
   - занято,
 - сетевые интерфейсы,
 - тип и версия ОС
'''

import psutil
from platform import system, release
from collections import namedtuple

Disk = namedtuple('Disk', 'device, mountpoint, mem_used, mem_free')
RAM = namedtuple('RAM', 'mem_total, mem_used, mem_free')
Interface = namedtuple("Interface", 'name, address,netmask')
OS = namedtuple('OS', 'type, version')
SystemStats = namedtuple('SystemStats', 'cpu, ram, hdd, interfaces, os')


def size2GB(size):
    return '%.2f GB' % float(size / (1024 ** 3))


def get_diagnostic_info() -> SystemStats:
    cpu = psutil.cpu_percent(interval=1)
    mem = RAM(size2GB(psutil.virtual_memory().total), size2GB(psutil.virtual_memory().used),
              size2GB(psutil.virtual_memory().free))
    hdd_partitions = [
        Disk(part.device, part.mountpoint, size2GB(psutil.disk_usage(part.mountpoint).used),
             size2GB(psutil.disk_usage(part.mountpoint).free))
        for part in psutil.disk_partitions() if 'snap' not in part.mountpoint]

    ints = psutil.net_if_addrs()
    interfaces = [Interface(key, ints[key][0].address, ints[key][0].netmask) for key in ints.keys()]
    os = OS(system(), release())
    return SystemStats(cpu=cpu, ram=mem, hdd=hdd_partitions, interfaces=interfaces, os=os)


def print_banner(msg, width=20):
    print(str(msg).center(width, '-'))


def print_diagnostic_info(system_stats: SystemStats, verbose: bool):
    if verbose: print_banner("CPU")
    print("CPU usage: {0}%% ".format(system_stats.cpu))
    if verbose: print_banner("RAM")
    print("Total:\t{0}\nUsed:\t{1}\nFree:\t{2}".format(system_stats.ram.mem_total, system_stats.ram.mem_used,
                                                    system_stats.ram.mem_free))
    if verbose: print_banner("HDD")
    print('Device'.ljust(10), 'Mountpoint'.ljust(15), 'Used'.ljust(10), 'Free'.ljust(10))
    for each in system_stats.hdd:
        print(each.device.ljust(10), each.mountpoint.ljust(15), each.mem_used.ljust(10), each.mem_free.ljust(10))

    if verbose: print_banner("Interfaces")
    print('Name'.ljust(10), 'Address'.ljust(15), 'Netmask'.ljust(15))
    for each in system_stats.interfaces:
        print(each.name.ljust(10), each.address.ljust(15), each.netmask.ljust(15))

    if verbose: print_banner("OS")
    print("OS:\t\t\t{0}\nVersion:\t{1}".format(system_stats.os.type, system_stats.os.version))


if __name__ == "__main__":
    print_diagnostic_info(get_diagnostic_info(), True)
