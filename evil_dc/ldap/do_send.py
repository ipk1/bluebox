import socket
import binascii

packet = binascii.unhexlify('3084000001040201016384000000fb04000a01000a0100020100020100010100a084000000d4a3840000001c0409446e73446f6d61696e040f6d69736b61746f6e69632e756e692ea384000000170404486f7374040f4445534b544f502d44514c4d473337a384000000250409446f6d61696e5369640418010400000000000515000000b9e81cc93f161323478e6dbca3840000001e040a446f6d61696e4775696404109833dc516c2789468b2bcf581b826058a3840000000d04054e74566572040416000000a3840000002d040b446e73486f73744e616d65041e4445534b544f502d44514c4d4733372e6d69736b61746f6e69632e756e6930840000000a04084e65746c6f676f6e')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.sendto(packet, ('127.0.0.1', 389))
data = ''
while (len(data) < 10):
  data += s.recv(8192)

packet = binascii.unhexlify('30840000015802010163840000014f04000a01000a0100020100020178010100870b6f626a656374636c61737330840000012b0411737562736368656d61537562656e747279040d6473536572766963654e616d65040e6e616d696e67436f6e7465787473041464656661756c744e616d696e67436f6e746578740413736368656d614e616d696e67436f6e74657874041a636f6e66696775726174696f6e4e616d696e67436f6e746578740417726f6f74446f6d61696e4e616d696e67436f6e746578740410737570706f72746564436f6e74726f6c0414737570706f727465644c44415056657273696f6e0415737570706f727465644c444150506f6c69636965730417737570706f727465645341534c4d656368616e69736d73040b646e73486f73744e616d65040f6c646170536572766963654e616d65040a7365727665724e616d650415737570706f727465644361706162696c6974696573')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 389))
s.send(packet)
data = ''
while (len(data) < 10):
  data += s.recv(8192)
s.close()
 