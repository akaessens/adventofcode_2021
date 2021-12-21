import numpy as np
import bitstring

with open("input.txt", "r") as file:
    data = file.read().strip()

bit_data = bitstring.BitArray("0x"+data)

def read_packet(pos, value):
    packet_version = bit_data[pos:pos+3].uint
    packet_type = bit_data[pos+3:pos+6].uint
    print ("packet_version", packet_version, "packet_type", packet_type)

    pos += 6

    if packet_type == 4: # literal value
        more = True
        val = bitstring.BitArray(0)
        while more == True:
            more = bit_data[pos]
            val.append(bit_data[pos+1: pos+5])
            pos += 5
        print("Literal", val.uint)
        value = val.uint

    else: # operator
        length_type = bit_data[pos]
        subvals = []
        if length_type == 0:
            packet_length = bit_data[pos+1:pos+1+15].uint
            print("operator packet_length", packet_length)
            pos += 16
            startpos = pos
            while ( pos < startpos + packet_length):
                (pos, subval) = read_packet(pos, value)
                subvals.append(subval)

        elif length_type == 1:
            subpackets = bit_data[pos+1:pos+1+11].uint
            print("operator subpackets", subpackets)
            pos += 12
            for packet in range(subpackets):
                (pos, subval) = read_packet(pos, value)
                subvals.append(subval)
        
        print ("operator type", packet_type)
        print ("subvals", subvals)
        if packet_type == 0: # sum
            value = sum(subvals)
        elif packet_type == 1: # mult
            value = np.prod(subvals)
        elif packet_type == 2: # min
            value = min(subvals)
        elif packet_type == 3: # max
            value = max(subvals)
        elif packet_type == 5: # >
            value = (subvals[0] > subvals[1])
        elif packet_type == 6: # <
            value = (subvals[0] < subvals[1])
        elif packet_type == 7: # ==
            value = (subvals[0] == subvals[1])

    return (pos, value)

(pos, value) = read_packet(0, 0)

print ("value", int(value))
