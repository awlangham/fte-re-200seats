# fte-re-200seats
My solution of this week's 538 Riddler Express.

An auditorium with 200 seats, numbered from 1 to 200, is filled to capacity. A speaker, who happens to be a mathematician, steps up to the podium overlooking the audience and pauses for a moment. “You know,” she says, “I’m thinking of a rather large whole number. Every seat number in this auditorium evenly divides my number, except for two of them — and those two seats happen to be next to each other.”

As you’d expect, adjacent seats in the auditorium have consecutive numbers. Which two numbers was the speaker referring to?

The intermediate goal is to find a number which will evenly divide all but 2 consecutive seats, which I'll call N. We can rule out the first 100 seats. Why? Because if we say any of these first 100 seats (seat x for example) isn't a factor of N, it doesn't make sense that seat 2x can also still be a factor (for example, seats 90 and 91 can't be the seats, because N will have 180 and 182 as factors, and thus 90 and 91 as well).

Our options are now limited to [101, 200]. Looking for prime numbers is a good place to go next, since we can easily divide N by a prime number to remove it from the factor list. We've already removed any numbers that would have a multiple in the list of 200 seats, meaning we won't accidentally make another number not a factor. The primes in [101, 200] are 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, and 199. Of course, there are no consecutive primes in this list.

The last piece of insight is that we can also look into prime numbers that have been raised to a power (such as 2^2 or 3^4). For a given prime, the largest power of it in our list of 200 can easily be removed from the list of factors of N by simply dividing by the base prime. This is because we have removed any possible multiples, so we know there can't be another factor of N we accidentally remove - i.e. this prime to this power will only show up once in the list of prime factorizations. Trying 3 as the base we see that our range of [101, 200] holds none of 3's powers: 1, 3, 9, 27, 81, 243... Let's try 2: 1, 2, 4, 8, 16, 32, 64, 128, 256...

128 looks pretty good. And hey! it's right next to 127, a prime number.
