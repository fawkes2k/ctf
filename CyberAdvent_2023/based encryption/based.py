from base64 import b64decode, b32decode, b16decode

a = 'R1UzVEtNWlVIRTJVQ04yQ0dZMkRHTVpXR0kzRENNWlZHWTJUS1JSVEdFM1RJTktHR00yRE1RWldJTTJVTU1aWEdZNERHTVpWSVkzVE9NWlVHNDRUT1JBPQ=='
b = b64decode(a)
c = b32decode(b)
d = b16decode(c)
print(d)