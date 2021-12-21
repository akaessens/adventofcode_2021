import numpy as np
import bitstring

with open("input.txt", "r") as file:
    data = file.read().strip()

bit_data = bitstring.BitArray("0x"+data)
sum_packet_version = 0

def read_packet(pos):
    packet_version = bit_data[pos:pos+3].uint
    packet_type = bit_data[pos+3:pos+6].uint
    print ("packet_version", packet_version, "packet_type", packet_type)

    global sum_packet_version
    sum_packet_version += packet_version

    pos += 6

    if packet_type == 4: # literal value
        more = True
        val = bitstring.BitArray(0)
        while more == True:
            more = bit_data[pos]
            val.append(bit_data[pos+1: pos+5])
            pos += 5
        print("Literal", val.uint)

    else: # operator
        length_type = bit_data[pos]
        
        if length_type == 0:
            packet_length = bit_data[pos+1:pos+1+15].uint
            print("operator packet_length", packet_length)
            pos += 16
            startpos = pos
            while ( pos < startpos + packet_length):
                pos = read_packet(pos)

        elif length_type == 1:
            subpackets = bit_data[pos+1:pos+1+11].uint
            print("operator subpackets", subpackets)
            pos += 12
            for packet in range(subpackets):
                pos = read_packet(pos)

    return pos

read_packet(0)
print ("sum_packet_version", sum_packet_version)
