# The Embedded IT Diaries: Be Predictable, Be Trustworthy

tl;dr If you're going to do something big, warn early, often, and with increasing severity and harshness.

This topic is particularly apt, as I recently woke up to do my morning cardio, only to discover the Youtube Music app wouldn't work, with some cryptic error.
It took me a couple minutes to figure out that my YouTube channel and account had been frozen.
No concrete or transparent explanation was given.
The feeling was one of powerlessness, betrayal, confusion, and a desire immediately download and use spotify.
Upon appeal, the account was reinstated completely, with many words of apology but none of explanation.
I was not left with a feeling of trust.

Big tech companies can afford to piss off customers.
They have millions of them.
In embedded IT, this is not the case.
You don't have a ton of customers, and you can't just go out and find more.
You and your customers are stuck together.
Might as well be a happy marriage rather than an angry one.

## Hey Everybody Check Out This Massive Stick Better Watch TF Out

It is common practice in many tech organizations to keep an air of secrecy around operations.
I've also heard a lot of suggestions to just change things and see if the users complain.
This attitude persists because keeping mistakes invisible means you can avoid criticism, and acting in secret allows you to move decisively and unilaterally.

Keeping your users in the dark is a childish way to go about this.
We're supposed to be Adults. Professionals, even.

Even if you act unilaterally, telegraphing what you're going to do before you do it shifts the political and emotional situation in your favor, and usually results in better information for everybody.

Let's say you need to delete a bunch of directories that are too old or are getting too big.
I get it.
Cruft builds up.
The users never read emails.
Some towering intellect discovered a genius hack, and now everybody in his office has set up a cron job that writes a 50GB text file to their home directory every Saturday at 2AM.
Half of them don't read their emails, and are going you yell at you regardless.
If you make a habit of taking drastic action without alerting the users, at some point someone is going to wake up, try to use their home directory, and find themselves locked out.
They will experience all those negative emotions I mentioned earlier, and they will hate and mistrust you forever.
I, of course, love all my users, even the ones who are incompetent, careless, and ugly.
However, perhaps you like making your users feel this way, because they never read your emails and you resent having to pick up after them while they take 2-hour lunches at the Bone Fish Grill.

What if I told you that you can punish your users for their sins, reward good behavior, and cover your ass all at the same time?
If you send a warning email, the lovely people who read your missives will act accordingly, and the philistines with 42,345 unreads in their inbox will wake up and discover their home directory is locked.
Plus, when they call the higher-ups to complain, your ass is covered. 
They look careless, and you look like the guy who knows how to do his job.

## Gradually Escalating Severity

Now that police misconduct increasingly makes the news, more and more people have heard about the Minimum Use of Force principle.
This is like the IT version of that.
Let's say you want to shut down an old compute cluster and want users to make the transition in a timely fashion.
Here's a framework for doing this that showcases the Gradually Escalating Severity principle.

0. Certain users and managers were consulted about when a good time to migrate would be, to make sure we did not overlap with busy times of the year or important deadlines.
1. Sent out an email three months in advance, telling users to migrate to the new cluster on June 1st, and that the old cluster would be off-limits except for emergencies on June 15th and would be shut down permanently at the end of the month.
2. Sent another email on June 1st warning everybody to move off the cluster ASAP.
3. Starting on June 15th, send a BCC'd email to all users signed in to the old cluster.
4. Starting on June 21st, sent a email directly to the user. Sometimes they needed help, and other times just needed a firm reminder. If they were unresponsive, we contacted their supervisor. We kept going until someone had confirmed the message was received. 
5. We shut down the cluster. 

Ultimately, this was still a unilateral decision.
Users of the old cluster would prefer to keep using it forever, if possible, and if allowed veto power over the decision would do so. 
As it was, all of our users were able to be ahead of the ball, and thanked us for the help.
We gave them nothing they could reasonably complain about, even though the change was uncomfortable for them.

## Meet People Where They Are

This is more of a post-script.
I've heard that "we rolled out that change already, that directory should have been deleted a while ago, so let's just fix the glitch".

Even if you communicated earlier, if you didn't follow that up with action, the user will get confused.
If you don't follow up your warnings with action, you have to warn again before acting if you're dealing with people whose faith you want to keep.
Your ass may already be covered, unlike in the previous examples, but if you care about maintaining user good will it's the right thing to do.

### PS: Don't Be A Snitch (if you don't have to)

I once got harassed at work.
I've heard other people go straight to HR in this situation, which can work if HR wants to placate you more than they want to placate the person who's giving you problems.
It might even make you feel powerful, and will allow you to avoid confronting the problem individual directly.
I made a threat instead, or more of a promise.
I promised the problem individual that if they didn't stop, I would go to HR.
It never happened again. 
I felt stronger, and that coworker respected me more and appreciated that I had chosen to talk with them and solve the problem directly instead of get them in trouble.
Ever since then, I've known that as long as I have a backup plan, something to escalate to, I can always stand up for myself.

