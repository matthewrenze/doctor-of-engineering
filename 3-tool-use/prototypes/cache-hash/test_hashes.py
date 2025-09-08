import base64
import hashlib

string_1 = "forest-cover-area-of-Madhya-Pradesh-India-State-of-Forest-Report-2019-site-wikipedia-org"
string_2 = "forest-cover-area-of-Madhya-Pradesh-India-State-of-Forest-Report-2019-site-wikipedia-org-Forest-cover-by-state-in-India"
string_3 = "forest-cover-area-of-Madhya-Pradesh-India-State-of-Forest-Report-2019-site-wikipedia-org-Forest-cover-by-state-in-India"

md5_hash_1 = hashlib.md5(string_1.encode()).hexdigest()
md5_hash_2 = hashlib.md5(string_2.encode()).hexdigest()
md5_hash_3 = hashlib.md5(string_3.encode()).hexdigest()

print("MD5 Hashes:")
print(md5_hash_1)
print(md5_hash_2)
print(md5_hash_3)
print()

sha_hash_1 = hashlib.sha1(string_1.encode()).hexdigest()
sha_hash_2 = hashlib.sha1(string_2.encode()).hexdigest()
sha_hash_3 = hashlib.sha1(string_3.encode()).hexdigest()

print("SHA 256 Hashes:")
print(sha_hash_1)
print(sha_hash_2)
print(sha_hash_3)
print()

b64_hash_1 = base64.b64encode(sha_hash_1.encode()).decode()

print(b64_hash_1)
