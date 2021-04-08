I use git to make reports and figures much more reproducible. This makes it easier to check my own work, or redo analyses if I discover a bug, as well as being more transparent to others.

When the software that generated an analysis is versioned in git, simply including a git hash gives you a lot of provenance information.
Git also allows you to organize your software for different, but related, analyses.

I often have to answer particular questions based on the same core data source (a webapp and connected database). All the code I use for particular data source queries, cleaning and analyzing the data, or any other steps I took to validate a claim or produce a figure, are stored on the master branch. 

The workflow begins with a ticket. First, I create a new branch with the ticket name.
The question may be a one-off that I already have functionality to answer. In that case, I will probably modify my query, download and analyze my data, commit everything, save the hash in a notebook or report, and call it a day.

If I develop new functionality or make modifications to the core analysis or ingestion code, I merge the branch back into master.

I also use the short version of the git hash as a subdirectory into which I can place the data (in json files) together with any produced figures. This allows me to keep a copy of the data and all figures produced therefrom in a common location that is tied to the code used to both download the data and produce the figures from the data.

for example:

```
archive_by_hash/
  ie9cccf/
    28Oct2020Week_rhel62.json
    28Oct2020_rhel62_waitHist.html
  23rrv8x/
    7Aug2020Incident_all.json
    7Aug2020IncidentGantt.html
```

This does not involve a lot of overhead of infrastructure, but even a practice as simple as this makes it so much easier to try out new analyses quickly without worrying about breaking core functionality, and helps to keep code quality high (less chunks of copypasta  and commented-out options). It also makes it much easier to recreate analyses with new datasets as long as I have the original ticket number from jira or hash from my notebook.
