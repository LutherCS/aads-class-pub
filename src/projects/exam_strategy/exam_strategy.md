# Taking an exam

Consider a case of an exam where questions have different level of complexity and may take different amount of time to answer. More complex questions are usually worth more points but it's not always true.

Each input file describes questions of such exam. The first line of the file contains two numbers, a floating point *t* (exam time limit), and an integer *n* (number of exam questions). The rest of the file contains the value (points) and weight (time complexity) of each of the question (item). Both values and weights will be integers.

You goal is to implement function `pick_questions_to_answer` that takes file name and returns a tuple of (`list`, `int`) where list is an ordered sequence of indices of the selected questions and the number is the total point value of the selected questions.

## References

* [Algorithm Repository: Knapsack Problem](http://algorist.com/problems/Knapsack_Problem.html)
* [Knapsack Problems: Algorithms and Computer Implementations by Silvano Martello and Paolo Toth](http://www.or.deis.unibo.it/kp.html)
* [Knapsack problem - Wikipedia](https://en.wikipedia.org/wiki/Knapsack_problem)
