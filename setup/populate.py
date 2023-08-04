import dj_scope

from random import randint, choices
from string import ascii_letters
from foos.models import Foo
import datetime

for _ in range(10):
    title = ''.join(choices(ascii_letters,k=5))
    rate = randint(100,300)
    date = datetime.date(randint(1990,2023),randint(1,12),randint(1,29))
    foo = Foo(
        title = title,
        rate = rate,
        date = date)

    foo.save()

