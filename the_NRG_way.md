# The Embedded IT Diaries: Family Counseling

I have spent the last five years or so in embedded IT, serving as professional \(couples therapist / child of the divorced parents that are Central IT and the rest of the organization\). I have seen both remarkably functional and remarkably dysfunctional interactions between IT people and the researchers I was embedded with.

To clarify, this is NOT about direct customer support, or working in a call center.
That is a whole different ballgame.
This is about IT groups that service the core technology that keeps the broader organization running.

I learned a lot about how people from these different groups, with different skillsets, norms, and goals, can work together more productively. Especially at my last workplace, the Harvard NRG, we had a lot of norms which really helped to keep things functional.

I want to sum these things up and write them down while the memories are still (mostly) fresh. In this series I'll try to articulate some of the NRG's best principles, with illustrative examples. All example scenarios are purely fictional, and any resemblance to any other scenarios, real or imaginary, is purely coincidental.

## if you don't fix it, it isn't fixed / if the customer is wrong, tell them

IT is as much about talking with people as it is about fixing computers. It's very much about relationship management, even if it may not appear to be at first. This is a big problem for IT. Unfortunately, if you were lonely enough in high school to get good at computers, you're probably a kind of a freak. Relationships are not your thing, computers are. 

One of the consequences of this awkwardness is that a lot of internal customers end up dissatisfied with their IT group, despite the fact that the IT group has a lot of talented computer people in it. It's easy to find reasons not to provide service in IT -- your customers are usually less competent around technology than you are, or you would be out of a job. On top of this, IT is often overloaded. Many customers will not do basic things like read documentation unless forced to, or may have unrealistic expectations about what technology can do. 

Just as it is easy for IT to blame the customer, it is easy for the customer to blame IT. Customers often have misconceptions about how technology works, or moral failings such as pride or sloth. They are often wrong. However, in a relationship, you are not responsible for being right(morally or factually), you are responsible for a positive outcome for everyone. Resist the temptation to simply blame your counterparty for incompetence due to frustration or out of your own laziness.

This mindset of communicating clearly, no matter what, is usually difficult, but worthwhile, and keeps the relationships that drive IT's value functional.

### Dysfunctional example: missing files
 
>**Customer Joe**: Hello [(nb: never do this)](https://www.nohello.com)
>
>**IT Bob**: Hello, Joe, what is your problem?
>
>**C**: I'm not seeing the files that were supposed to be uploaded to the linux cluster! We've been unable to do our research for a week! This is ridiculous.
>
>**IT**: OK, what should the files look like, and where are they supposed to be?
>
>**C**: They should be at /ncf/JoeLab/fMRI bay 2/2019

At this point, IT Bob checks the directory given, and finds that not only is the directory given nonexistent, but that the parent directory `/ncf/JoeLab` doesn't even exist. IT Bob is frustrated, just doesn't reply, and moves on to other things.

#### IT Bob's mistakes and how to do better

This is not a morality play. God is not going to descend from the heavens and judge you the Reasonable And Smart One, and condemn your client to IT hell. (no matter how much they may deserve it). Most importantly, you will not be able to evade the bad perception of your IT group forever. Customer Joe may not even understand that IT blames him for the issue. As far as he is concerned, IT is terrible and didn't do their job. As far as IT is concerned, Customer Joe is completely unreasonable and incompetent. Even if IT Bob is right, Customer Joe is also still right. How can this be so?

It is IT's job to enable the customer to use technology to further the broader organization's mission. If fundamental business operations are blocked, and IT has abandoned the problem, they have failed. I'm not saying the customer is always right. In IT, in fact, the customer is usually wrong. That's what we're here for.

It is categorically better to explain to the customer why they are wrong, and continue to work with them on their problem, than it is to ignore them. Sometimes the customer will make this emotionally difficult for you to do. Do it anyway -- it's your job. In this 'missing files' case, the problem is clearly somewhat urgent, so it's particularly inexcusable to just drop the thread of communication. 

You may be worried that telling the customer they're wrong will make them angry. This may be true, in the short term. However, they probably have a boss. Your choices are 

1. Risk making them angry but work towards solving the problem now.
2. Ignore them for a week until the problem gets bad, one or both of your bosses gets involved, and you look like you didn't do your job by leaving them hanging  (because you didn't).

These are all important goals for IT workers, but IT workers are only human, and many of them may not have even read this article! So,  just as IT must strive to enable customers, it's equally important that customers learn to enable IT.

#### Customer Joe's mistakes and how to do better

[Never just say hello](https://www.nohello.com/2013/01/please-dont-say-just-hello-in-chat.html)

It is much, MUCH better to admit ignorance than give incorrect specific information. Customers often feel a need to prove their technical chops to the IT person for a variety of emotional reasons I won't go into here. Other customers may (rightly) think that the more computery they speak, the easier it will be for IT to understand them. However, incorrect details can mislead and frustrate the IT person. While precise compu-speak is preferable, precise and accurate english is much, much better than imprecise or innacurate compuspeak. 

A more nuanced aspect of striving for accuracy is accurately conveying uncertainty. Written language is not always the best at this, but even just using modifiers like "I think", and avoiding jumping to conclusions can help. For example, it is better to say "I think the hard drive is broken because it doesn't show up when I plug it in to my macbook" than simply "My hard drive is broken", because in this example the problem could easily be with some configuration on your mac, or an incompatibility between the mac and the hard drive. This sort of observation-first language allows for easier collaboration than conclusion-based declarative language.

Memory can also be a hazard in this arena. People in general are terrible at remembering specific directory names down to the letter. Sometimes, there is an intermittent error message that flashes up on screen but you can't reference to copy word-for-word. It is equally important that you find some way to communicate this type of uncertainty. Uncertain information marked as such is usually more valuable than if you had left it out, but uncertain information presented as certain can quickly lead to SNAFU.

For the more adventurous, an experimental precision-uncertainty-communication technique I have personally taken to using employs spanish-style punctuation to denote parts of a sentence I am especially unsure about:

> Whenever I check the job status, it's at "starting" or ¿"initializing"?, but don't ever appear to enter "running" state

The over-arching principle is this: Your job is to describe your problem effectively, and ask good questions. If you have suggestions or have come to your own conclusions about the origin of the problem, that's great, but the IT professional may know things you don't, and it's always good to explain your conclusions to allow for collaboration and build mutual trust. It's also important to clearly explain your high-level goal, because the IT professional may be able to figure out a solution you were not aware existed.

Here are two good guides to asking good questions: ([shorter](https://www.techsupportalert.com/content/how-ask-question-when-you-want-technical-help.htm),[longer](https://github.com/selfteaching/How-To-Ask-Questions-The-Smart-Way/blob/master/How-To-Ask-Questions-The-Smart-Way.md)). If you're working in a technical field, I highly recommend giving them a read. If you're doing any coding whatsoever, I would read this [short debugging guide](https://ericlippert.com/2014/03/05/how-to-debug-small-programs/).

You will have to be flexible about how you seek out information. Official documentation, google search, man pages, mailing lists, or even a google doc may be the best source of information about a particular piece of software, and part of learning a new library or other tool is figuring out where to go first for information. Especially in niche technical fields, the best source of information varies a lot, and it's usually not just a google search. Similarly, you will have to learn how to get the most out of IT. Depending on your department and the problem at hand, in-person, a chatline, the docs, submitting a ticket, or an email to a particular individual might be the most effective way to get your problem solved.

Now, let's see what our 'missing files' example could look like after applying some of these principles:

### Functional example: missing files

>**Customer Joe**: I'm not seeing the .dcm files from 2019 that were supposed to be uploaded to the cluster. This is URGENT as it is completely blocking our work. I used filezilla to look in our lab's folder, which I think is supposed to be /ncf/JoeLab, but don't see anything!
>
>**IT Bob**: I see the problem. The files were sent to `/ncf/Joelab_archive`. Can you see that?
>
>**C**: I can't
>
>**IT**: OK, I changed the group permissions for that folder. Hopefully you can see them now.
>
>**C**: Great, I can see them now!
> **ticket has been closed**

### Theory of Mind: the importance of Empathy

A lot of customer-service culture focuses on disingenuous appeasement exemplified by the phrase "the customer is always right". While this may de-escalate conflict or win customers in the short-term, in the IT business, where you have recurring relationships that must actually function (i.e., solve technical problems), this is a losing strategy. Phrased differently, in a retail or direct support role you are often interested in getting the customer's money primarily -- even if the customer is being unreasonable or is mistaken, you are usually trained to appease them so that your company can continue to take their money. In embedded IT, you can't play games with people's emotions like that. You're in a committed relationship, and it is in your best interest to make it as functional as you can.

Ultimately, "if the customer is wrong, tell them" is just a specific rule. In general, the broader principle is to work on your cognitive empathy. Although it often helps, you _don't_ always need to feel the same way as the customer / feel bad for them (affective empathy / sympathy). You _do_ need to understand what's going on in their head or know how to take their perspective.

This is true for both parties. For example, imagine the inverse of the 'missing files' scenario above: 

### Functional example: files missing

>**Customer Joe**: I'm not seeing the .dcm files from 2019 that were supposed to be uploaded to the cluster. This is URGENT as it is completely blocking our work. I used filezilla to look in our lab's folder, which I think is supposed to be /ncf/JoeLab, but don't see anything!
>
>**IT Bob**: I see the problem. Just chmod 777 that dir
>
>**C**: _stays silent because they feel embarassed that they don't know what IT Bob is talking about_

Here, IT has "fixed" the problem by spouting some jargon that the customer does not understand. If IT Bob was talking to his colleague, IT Bill, they would understand him right away. However, the customer is confused. In that scenario, it is vital that the customer explain what they do not understand, and allow the IT person to provide needed context or further information. This can be difficult because it involves admitting a limitation, which can feel vulnerable. Still, you have to be transparent about these things if you want to move forward.

Here are some other brief examples of where taking the time to appreciate your counterparty's frame of reference can reduce frustration and make the relationship more functional:

#### To IT workers:
- You know where the docs are. You have sent out links to the docs twelve times this week. Everyone in IT knows where the docs are. Everyone in IT doesn't even need the docs because they already understand your systems so well. The new research assistant is still not going to know where the docs are. Bear this in mind.
- The customer probably doesn't care how many gigahertz the new chip has. To them, Amber Lake might as well be that girl they went to middle school with that was obsessed with horses. Please refrain from spending  all your time with a customer talking about chip architectures, especially if the customer has been unable to complete work for weeks due to technical problems. It feels like going to the doctors and getting stuck listening to him walk you through his pokémon collection.

#### To IT customers:
- IT does not know how long you have been debugging your problem. IT probably doesn't even know your problem existed until you contacted them. Do not blame IT for a week-long problem if you only just contacted them!
- No amount of cajoling, blackmail, or kowtowing will enable your IT person to fix a problem you have not described in sufficient detail. They are probably not refusing to fix it because they dislike you. They probably dislike you because you want them to FIX IT!!! without giving them sufficient information to do so.
- Do not worry about not knowing technical things. That is IT's job, not yours. Your job is to be as honest as possible and ask good questions. If you are honest, ask good questions, and demonstrate that you tried to read the docs before submitting a ticket, IT will love you and won't care if you don't know some technical detail. 

### Addendum: Managers, stay in your lane

This is related, but I couldn't find a nice place to put it.

Managers (correctly) understand that their complaints will be taken more seriously and will be expedited. However, they frequently garble important technical details given to them by underlings in their escalation emails. Don't try and play telephone. If you're a manager (yes, professors, you are managers), your go-to option should be "email them about it and CC me". Make sure you are CC'd on chains, or forward emails where they need to go, but leave the details to the detail people if at all possible. Less work for you, and usually less work for everyone.
