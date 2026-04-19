# 8-13 User Profile

def build_profile(first, last, **info):
    profile = {
        "first_name": first,
        "last_name": last
    }

    for key, value in info.items():
        profile[key] = value

    return profile

user = build_profile(
    "Arno",
    "Mostert",
    age=20,
    city="Pretoria",
    hobby="coding"
)

print(user)