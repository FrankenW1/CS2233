user_score = 0
simon_pattern = input()
user_pattern = input()

for simon_pattern in str(simon_pattern):
    for user_pattern in str(user_pattern):
        if str(simon_pattern) == str(user_pattern):
            user_score += 1
            continue
        if str(simon_pattern) != str(user_pattern):
            break

print('User score:', user_score)
