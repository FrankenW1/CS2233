
def print_points(name, age, total_points):
    print('{} is {}'.format(name, age))
    print('{} made {} points'.format(name, total_points))

user_name = 'Sue'
user_age = 18
regular_time_points = 27
overtime_points = 3

print_points(user_name, user_age, regular_time_points + overtime_points)
