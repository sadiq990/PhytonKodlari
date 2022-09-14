#continue command

from pkg_resources import safe_extra


numbers = range(1,10)     #   -------------> 1,2,3,4,5,6,7,8,9


# tek ededler ucun
for number in numbers:
    if number%2==0:
        continue
    print(number)

# cut ededler ucun
for number in numbers:
    if number%2==1:
        continue
    print(number)