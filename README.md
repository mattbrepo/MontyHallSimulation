# MontyHallSimulation
Simulation of the [Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem)

**Language: Python**

**Start: 2022**

## Why
I just wanted to write a quick and dirty simulation of the [Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem) mainly because I was trying to convince my intuition that you have to take advantage of the opportunity and switch door!

I ran 100,000 simulation:

```
number of winning games when sticking with the first door: 33316 / 100000 (33%)
number of winning games when switching door: 66684 / 100000 (67%)
```

## Bayes' Theorem approach
The [Bayes' theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem) can be used to tackle the Monty Hall problem in a more rigorous way. In particular, we can use the -so called- diachronic interpretation of the Bayes' Theorem. Diachronic refers to a phenomena that changes over time.

$$ P(\textbf{H}|\textbf{D}) = \frac{P(\textbf{H}) P(\textbf{D} | \textbf{H})}{P(\textbf{D})} $$

where:

- P(H | D) is the probability of the hypothesis after we see the data (**posterior**)
- P(H) is the hypothesis before we see the data (**prior**)
- P(D) is the probability of the data under any hypothesis (**normalizing constant**)
- P(D | H) is the probability of the data under the hypothesis (**likelihood**)

In this case, we can imagine the scenario (S) where the participant picked door A and the host of the game opened door C. Now, the question becomes: is the participant better off switching to door B rather than sticking to door A? Which in Bayes terms can be written as:

$$ P(B | S) > P(A | S) $$

Now we can solve this two terms with the Bayes' theorem:

$$ P(A | S) = \frac{P(A) P(S | A)}{P(S)} $$

$$ P(B | S) = \frac{P(B) P(S | B)}{P(S)} $$

where:

$$ P(S) = P(B open | A pick) = \frac{1}{2} $$

$$ P(A) = P(B) = \frac{1}{3} $$

because P(A) is the prior therefore it answers the question: which is the probability that door A (or door B) hides the price? 

And where:

$$ P(S | A) = \frac{1}{2} $$

because if the prize is behind the door A, the host can either open B or C.

Instead:

$$ P(S | B) = 1 $$

because if the price is behind the door B, the host can only open door C.

Therefore:

$$ P(A | S) = \frac{P(A) P(S | A)}{P(S)} = \frac{1/3 \cdot 1/2}{1/2} = \frac{1}{3} $$

$$ P(B | S) = \frac{P(B) P(S | B)}{P(S)} = \frac{1/3 \cdot 1}{1/2} = \frac{2}{3} $$


