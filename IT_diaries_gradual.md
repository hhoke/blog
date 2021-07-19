# The Embedded IT Diaries: Be Predictable, Be Trustworthy

tl;dr If you're going to do something big, warn early, often, and with increasing severity and harshness.

The other day, I woke up to do my morning cardio, only to discover Youtube Music was completely inoperable.
Everything I tried to do resulted in a cryptic error.
After I gave up on debugging and decided to check my email, I saw that my YouTube channel and account had been frozen.
No concrete or transparent explanation was given.
The feeling was one of powerlessness, betrayal, confusion, and a desire to immediately download and use spotify and finish my workout.
After an appeal and several days, the account was reinstated completely, with many words of apology but none of explanation.
I was not left with a feeling of trust.

Big tech companies can afford to piss off a couple customers.
They have millions of them.
In embedded IT, this is not the case.
You don't have a ton of customers, and you can't just go out and find more.
You and your customers are stuck together.
Might as well be a happy marriage rather than an angry one.

## InfoWars

It is common practice in many tech organizations to keep an air of secrecy around operations.
Some people think FUD will make it easier to cover their ass, or like the feeling of power and control the information asymmetry gives them.
The attitude is "Let's just turn it off, and if the users complain then we'll know something broke," or "Let's just roll out the upgrade tonight, what are the users going to do about it?"
It may be the case that obscuring your actions means you can avoid criticism, and acting in secret allows you to move decisively and unilaterally (at least, until you get pushback).
Plus, communication can be difficult.

However, keeping your users in the dark is and unsustainable and dysfunctional in the long term, and is, frankly, childish.
We're supposed to be Adults. Professionals, even.

If you make a habit of taking drastic action without alerting the users, at some point someone is going to wake up, try to run their usual workflow, and find that everything has broken.
They will have no plan, and may not even know what broke, because you didn't tell them.
They will experience all those negative emotions I experienced when youtube locked me out. 
They may miss important deadlines or fail to close key clients.
They will hate and mistrust you forever.

Many of your users don't ever read your emails, and are going to yell at you basically no matter what.
I get it.
Still, we shouldn't use these lusers as an excuse to make your ops opaque and mysterious.

I, of course, love all my users, even the ones who are incompetent, careless, and ugly.
However, perhaps you like making your users feel this way, because they never read your emails and you resent having to pick up after them while they take 2-hour lunches at the Bone Fish Grill.
Worry not. You can have your cake and eat it too.

## Hey Everybody Check Out This Massive Stick Better Watch Out

Even if you want to act unilaterally, telegraphing what you're going to do before you do it shifts the political and emotional situation in your favor, and usually results in better information for everybody.

More than this, communicating effectively allows you to, at once, punish the lusers, reward good behavior.
In other words, you are going to teach people to treat your emails not as irrelevant scribblings but as divine instructions from a just and merciful IT god.

Once you send a warning email, your faithful readers, people of the IT covenant, will act accordingly, and prepare themselves for a smooth transition.

Conversely, the Philistines with 42,345 unreads in their inbox will ignore as always, only to one day wake up and discover they really should have updated that key dependency when they had the chance.
When they call the higher-ups to complain, your ass is covered. 
They look careless, and you look like the guy who knows how to do his job.

## Gradually Escalating Severity

We have established that communication is a good long-term strategy.
Now, let's talk tactics.

Police misconduct increasingly makes the news, so many of you may already have heard about the Minimum Use of Force principle.
This is like the IT version of that.
Let's say you want to shut down an old compute cluster and want users to make the transition in a timely fashion.
Here's a framework for doing this that showcases the Gradually Escalating Severity principle.

0. Consulted certain users and managers about when a good time to migrate would be, to make sure we did not overlap with busy times of the year or important deadlines.
1. Sent out a listserv email three months in advance, telling users to migrate to the new cluster on June 1st, and that the old cluster would be off-limits except for emergencies on June 15th and would be shut down permanently at the end of the month.
2. Sent another email on June 1st warning everybody to move off the cluster ASAP.
3. Starting on June 15th, sent a warning email, with BCC, to all users signed in to the old cluster.
4. Starting on June 21st, sent a email directly to the user. Sometimes they needed help, and other times just needed a firm reminder. If they were unresponsive, we contacted their supervisor. We kept going until someone had confirmed the message was received. 
5. We shut down the cluster. 

Two remarks:

In the first place, each of these communications is obviously a way for you to give information to users.
Less obviously, each of these steps was an opportunity for users to give information to you, even if the information is implicit.
This allows the communication to be more targeted at each step.
For example, users who ignored the email in step 2 implicitly gave you the information that they require additional prodding or help.
By narrowing down the target audience with the first few emails, you avoided the scenario in which there are too many users to prod individually, resulting in you desperately sending **IMPORTANT!!** blast emails into the void.

In the second place, this was ultimately still a unilateral decision, but gracefully-executed rather than ham-fistedly.
There was some wiggle room on the specific date, but we needed the old cluster shut down by August, and this was non-negotiable.
Users of the old cluster would prefer to keep using it forever, if possible, and if allowed veto power over the decision would do so. 
As such, we couldn't be fully open to a consensus approach, but things still went much more smoothly for everyone because we communicated.
All of our users were able to be ahead of the ball, and thanked us for the help.
We gave them nothing they could reasonably complain about, even though the change was uncomfortable for them.

## PS: Meet People Where They Are (not where they ought to be)

I've heard that "we rolled out that change already, that directory should have been deleted a while ago, so let's just fix the glitch".

*important data go poof*

Even if you communicated earlier, if you didn't follow that up with action, the user will get confused. It sends a mixed message.
If you don't follow up your warnings with action, you will have to warn again before acting, if you're dealing with people whose faith you want to keep.
Your ass may already be covered, unlike in the previous examples, but if you care about maintaining user good will and the functionality of critical business systems, it's the right thing to do.
