# Lawn Mower

<https://open.kattis.com/problems/houselawn>

You have just bought a new house, and it has a huge, beautiful lawn. A lawn that needs cutting. Several times. Every week. The whole summer.
After pushing the lawnmower around the lawn during the hottest Saturday afternoon in history, you decided that there must be a better way. And then you saw the ads for the new robotic lawnmowers. But which one should you buy? They all have different cutting speeds, cutting times and recharge times, not to mention different prices!

According to the advertisement, a robotic lawnmower will spend all its time either cutting the lawn or recharging its battery. Starting from a full battery, it will cut the lawn at a given rate of c square meters per minute for a cutting time of t minutes, after which it has run out of battery. Once out of battery, it will immediately start recharging. After recharging for r minutes the battery is full again and it immediately starts cutting.

You decide that in order for your lawn to look sufficiently prim and proper, the lawnmower that you buy must be powerful enough to cut your whole lawn at least once a week on average. Formally, if we start the mower fully charged at the beginning of the week and run it for exactly T weeks, it needs to cut the whole lawn at least T times, for all positive integers T. But apart from this, you have no specific requirements, so among the ones that satisfy this requirement, you will simply go for the cheapest option. For the purposes of cutting your lawn, you may make the simplifying assumption that a week is always exactly 10080 minutes long.

## Input

The first line of input contains one integer ℓ (1≤ℓ≤106), the size of your lawn in square meters.

Then follow line(s), each containing a string n and 4 integers p, c, t, and r, separated by commas, describing a lawnmower as follows:

* n is the name of the lawnmower, a string of at most 60 printable characters (ASCII 32 to 126) excluding ‘,’, neither starting nor ending with a space,
* 1≤p≤100000 is the price of the lawnmower,
* 1≤c≤100 is the cutting rate in square meters per minute,
* 1≤t≤10080 is the cutting time in minutes, and
* 1≤r≤10080 is the recharge time in minutes.

## Output

Output the name of the cheapest lawnmower capable of cutting your whole yard at least once a week on average. If several lawnmowers share the same lowest price, output all of their names, in the same order they were given in the input. If there is no such mower, output “no such mower”.
