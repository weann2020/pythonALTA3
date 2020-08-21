#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
print(proto)
print(proto[1])
proto.extend("dns")
print(proto)
protoa = ["ssh", "http", "https"]
protoa.append("dns")
print(protoa)
