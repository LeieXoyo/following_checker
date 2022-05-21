import sys

from following_checker.extract_profile import extract_follow

args = sys.argv

if len(args) == 2:
    username = args[1]
    followers = extract_follow(f'https://github.com/{username}?tab=followers')
    following = extract_follow(f'https://github.com/{username}?tab=following')
    print(f'关注了对方而没被对方关注的:{following - followers}')
else:
    raise Exception('参数个数错误,请检查!')