# A Classy Problem

<https://open.kattis.com/problems/classy>

In his memoir "So, Anyway", comedian John Cleese writes of the class difference between his father (who was "middle-middle-middle-lower-middle class" and his mother (who was "upper-upper-lower-middle class"). These fine distinctions between classes tend to confuse North American readers, so you are to write a program to sort a group of people by their classes to show their true place in the social class hierarchy.

For this problem, there are three main classes: upper, middle, and lower. Obviously, the highest is upper and the lowest is lower. But there can be distinctions within a class, so upper-upper is a higher class than middle-upper, which is higher than lower-upper. However, all of the upper classes (upper-upper, middle-upper, and lower-upper) are higher than any of the middle classes.

Within a class like middle-upper, there can be further distinctions as well, leading to classes like lower-middle-upper-middle-upper. When comparing classes, once you have reached the lowest level of detail, you should assume that all further classes are the same as the middle level of the previous level of detail. So upper class and middle-upper class are equivalent, as are middle-middle-lower-middle and lower-middle.

## Input

The first line of input contains a single positive integer *T* (T≤500) indicating the number of cases to follow. Each case starts with a positive integer *n* (n≤100) on a line indicating the number of people to consider. Each of the next n lines contains the name of a person followed by a colon and a space, followed by the class of the person. The name contains up to 30 lowercase characters. The class is a string consisting of a nonempty sequence of up to 10 of the words upper, middle, lower separated by hyphens (-), followed by a space, followed by the word class. No two people will have the same name in a single case.

##Output

For each test case, print the list of names from highest to lowest class. If two people have the same or equivalent classes, they should be listed in alphabetical order by name. Output a line of 30 equal signs (=) after each case.
