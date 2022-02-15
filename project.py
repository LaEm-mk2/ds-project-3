import OpenDartReader

api_key = '8b177892a2e3dcfd88f3b111434646e3dc1e0e12'

dart = OpenDartReader(api_key)

print(dart.list('005930',end='2022-02-15'))
