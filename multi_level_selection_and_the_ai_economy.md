# Multi-Level Selection and the AI Economy

Reading https://institute.deepmind.com/essays/the-economics-of-intelligence/, which is both elegant and informative.

The figures are really worth looking at, and if you look at all of them, you have the gist of the paper. I can't think of a better use of the next five minutes of your time.

In a world of jagged capabilities, grouping people with complementary abilities leads to greater firm efficiency than you would expect from just averaging everybody. They call this "organizational mosaic intelligence" and nod to Bostrom. To phrase it like our silicon friend might: Technocapital was already recursively-self-improving superintelligence. Humans were just the compute.

And now, we are able to unload cognitive tasks in a general sense. Right now we have a very jagged capabilities frontier. Bots are better than humans at navigation, welding car parts together, and sometimes driving. Note that even for navigation, where robots have dominated humans for decades now, humans cannot fully hand over the task. Problems include map/territory mismatch, lack of cell service, and electronic warfare GPS jammers. But understanding the future isn't just about capabilities, but economics.

Speaking of economics, why are we seeing holy-grail feats like finding a subexponential-time algorithm for 3-SAT, but an economy that is mostly the same. I'd bet a random guy pulled off the street would be more concerned about gas prices than AI.

✽ Flummoxing…

Yeah, it's 50pct AI vs 74pct gas prices. I even checked [the source](https://www.pewresearch.org/politics/2026/10/08/cost-concerns-dominate-as-publics-economic-ratings-turn-more-negative/). You ever heard about this thing called hallucination? It's very important to cite a reliable source. 

So, to recap, The Man just upped my rent last night, with whitey on the moon. Or, as that other old chestnut goes, "the future is already here -- it's just not evenly distributed". (And how, I bet whoever wrote that used ChatGPT.)

So what's happening, is the entire economy Fake & Gay™ ? (I guess I'll have to ask Grok that one). Well, no, say the brains at deepmind, it's just that "the individual AI agent is the wrong economic object". They argue that the correct analysis widens its scope from merely the individual to also include the firm. This makes sense. There are selection dynamics at play on both levels: Firms select people to hire and fire, and the market selects firms to grow or go bankrupt.

This is remarkably similar to the whole multi-level selection debate in Evolutionary Biology. Is selection a phenomena that happens on the level of selfish genes? Is it the individual organism? What about tribes, or ant colonies? There's still work to be done at the transitions -- for example, how does a phase shift from single cells to multicellularity, or from (correlated-genetic-destiny multi-line colonies) to (monogenetic ant colonies). Lots going on there. But speaking generally, the answer to "is there selection happening on the genic, individual, or group level" is yes. The gene's eye view is useful, but the gene's continued existence is inextricably tied to the fate of its individual organism (except for lateral gene transfer)

Returning to economics, naturally the unit of interest is the firm. But how can it be that "a model can exceed the performance of every person one-on-one and still lose to a well-structured team" if the overperformance of teams is due to ricardian comparative advantage? 

![A chemist and a physicist each score well only in their own field on GPQA graduate-level science questions, so as a team they cover more than either alone. GPT-4 (2023) scored like a non-expert; Claude Sonnet 4.6 (2026) beats both experts in their own fields.](figures/multi_level_selection_and_the_ai_economy/mosaic_gpqa.svg)

*Figure: a real-data, two-skill version of DeepMind's mosaic intelligence figure, using measured expert and model accuracy on GPQA. [Figures, code and sources](figures/multi_level_selection_and_the_ai_economy/).*

Mosaic intelligence alone can outperform GPT-4 from 2023, but Claude Sonnet 4.6 dominates across the board. If a single LLM can dominate a firm of people, who cares about coordination costs? 

They make a good point that humans tend to be jagged in complementary ways, but AI is jagged in identical ways. So, "We can add a complementary human specialist to a team to fill a gap, but spinning up another copy of a model only adds capacity without increasing breadth of capabilities." But I return to the above figure. In three years, a SOTA model has gone from inside the human average, blown through the paradigm where it is better than average but the firm still dominates, to reach a paradigm where a single model dominates even a firm of humans. Presumably if they needed scale, they could just run two agents. Identical jaggedness doesn't matter as it beats every human on every task skill. So this "Minimal AGI" is an interesting case, and does much to help us understand the current situation. But I think in the long term, We will end up with ASI. It seems overwhelmingly likey that coordination between agents will get much better than it is now, and capabilities increases are a runaway freight train.

| Silicon > Meat at... | **Thinking: Sometimes** | **Thinking: Always** |
|:--------------------|:------------------------|:---------------------|
| **Coordinating: No** | Minimal AGI | Supercompetent AI |
| **Coordinating: Yes** | Supercooperative AGI | **ASI** |
  
So this is a very cool call to action on coordination. It's also a good default model for the economic changes ahead for us in the next 5 years or so. It will be interesing to see which regime we land in for different industries -- assuming the singularity doesn't come for us all.
