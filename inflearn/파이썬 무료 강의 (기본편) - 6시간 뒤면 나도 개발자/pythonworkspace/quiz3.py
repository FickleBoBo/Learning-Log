# site = "https://naver.com"
site = "https://ficklebobo.dev"

s1 = site[8:]
s2 = s1[: s1.index(".")]
s3 = s2[:3] + str(len(s2)) + str(s2.count("e")) + "!"

print(s3)
