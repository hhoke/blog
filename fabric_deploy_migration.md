---
layout: default
comments: true
---

# Patterns for Migration From Fabric 1 to Fabric 2

Fabric 1 is deprecated.
I had to move a reasonably complicated deploy script from fabric 1 to fabric 2.
I wrote this for me-at-the-beginning-of-this-project, so if you are frantically googling this topic I hope this turns up.
My goal is to provide a useful guide to how to effectively understand and work with fabric 2, especially if you are coming from a fabric 1 background.

## Useful Guides

There is the [Official Fabric Guide](https://www.fabfile.org/upgrading.html) for detailed reference use.

I also found [Yoong Kang's deploy guide](https://yoongkang.com/blog/fabric-deployment/) extremely useful, because it explained some of the tricky bits needed to pull off a successful migration.
One of these tricks is understanding that much of Fabric is meant to inherit functionality from Invoke.

## General Principles
### Navigating Parent and Child Docs

Fabric inherits functionality from Invoke in a very seamless way so that it appears this is fabric functionality.
The documentation of this functionality stays in Invoke, which can be confusing if you are just looking at Fabric.
The key is to understand that the documentation just follows the DRY principle, and that you are going to need to look at both Fabric and Invoke, as well as maybe Paramiko or Patchwork libraries to find what you're looking for.

For example, I use `-r` to enable calling the same fabfile from any directory.
(specifically, I have an alias in my `~/.zshrc`, `alias efab="fab -r /PATH/TO/DIR/CONTAINING/THE/FABFILE/I/USE"`).
When my code was being reviewed, my reviewer went to the [CLI docs](https://docs.fabfile.org/en/2.6/cli.html), ran a find command to locate `-r`, and couldn't find it.
This is because it was not there, but is only in the invoke docs.
There's a note to check the invoke docs, and a link there, so I was easily able to figure this out and explain it.
I don't know how to go about fixing this, but the fact that the user interface itself has the inherited functionality right there, but the docs websites are nested, is confusing.

### Hacks Required

You could do things straightforwardly in fabric 1 that require ugly workarounds in fabric2.

For example, I needed to use workarounds because I could not do the following:

- [use `put` with `use_sudo`](https://github.com/fabric/fabric/issues/1750)
- [use Invoke contexts like `with cd` with Groups](https://github.com/fabric/fabric/issues/1861)
- [use `cd` context with `sudo`](https://github.com/fabric/fabric/issues/2091)

My deploy script in particular made heavy use of roles, which are not implemented in fabric 2 and required some hacky workarounds.

The lack of roles was a serious problem for me and [others](https://github.com/fabric/fabric/issues/2156).
I'm relying entirely on a role-my-own runtime object in order to construct and pass around a role the way I want.
More on this in the [Cursed Roles Workaround](#cursed-roles-workaround).

The closest thing I could find to roles were Groups, and you cannot pass Groups as Contexts/Connections to tasks.
This means that even if you use groups extensively, you still have to define tasks with a c-for-context-or-connection argument, and pass a dummy context to a task whenever you call it from another task, even if you never make use of this.

### So Long, Env!

Fabric1's `env`, while useful, could easily get huge and bloated.
With Fabric2, I was able to break it up into two separate objects, both of which were much smaller and well-defined.
My config files are smaller, and better-defined.
Plus, I can import them like an actual human being now instead of the strange workaround I had for Fabric1, where I defined most functions in a `fab_common.py` file, then imported from there into what was basically a glorified config file with `from fab_common import *`, and finally symlinked this glorified config file AND `fab_common` into the deploy directory of each project.

### Just Enough Magic

Less magic means less strange workarounds to deal with the magic.
Groups and explicit connections in particular allowed me to do a lot of neat things (see section on [Blessed Retry Logic](#blessed-retry-logic)).
I *love* the fact that Groups can be operated on as if they are lists of Connections.
Plus, Paramiko still just works (though unfortunately, [not in some people's virtualenvs](https://github.com/paramiko/paramiko/issues/1181)).

## In-Depth Example

Enough talk, let's see some code!
The following (partially simplified) example from my production code has several examples:

Fabric 1 code:

```python
@task
@runs_once
def select(build_name):

    with warn_only():
        prev = execute(_select, build_name)

    execute(restart, "all")

    puts(_get_revert_command(prev.values()[0]))

    if get_role() == "prod":
        _send_notification(build_name)

@parallel
def _select(build_name):
    with cd(env.build_dir):
        prev = _create_link(build_name)
    return prev

def _create_link(build_name):
    prev = sudo("readlink current", user="evergreen")
    sudo("rm -f current", user="evergreen")
    sudo("ln -s {0} current".format(build_name), user="evergreen")
    return prev

def _send_notification(build_name):
    if not env.get("recipient"):
        recipient = local("git config user.email", capture=True).strip() 
    else:
	recipient = env.recipient
    mail_cmd = 'mail -s "deployed {0}" {1}'.format(build_name, recipient)
    local(mail_cmd) 
```

The same, but in Fabric 2:

```python
@task
def select(c, build_name):
    """ set current binary for servers """
    prev_vals = create_link(build_name, group=runtime.rungroup, warn_only=True)

    systemctl(runtime.canary, "restart", "all", group=runtime.rungroup)

    prev_val = list(prev_vals.values())[0]

    print(_get_revert_command(prev_val))

    if runtime.active_role == "prod":
        _send_notification(build_name, build_name, prev_val if prev_val else None)

def create_link(build_name, group=None, warn_only=False):
    """ creates a link to build_name from "current" on the group's hosts,
    and returns a modified results dict of the form {Fabric.Connection:binary name}
    """
    if group is None:
        group = runtime.rungroup
    prev_result = group.sudo(f"readlink {codebase.build_dir}/current", user="evergreen", warn=warn_only, hide=True)
    group.sudo(f"rm -f {codebase.build_dir}/current", user="evergreen", warn=warn_only, hide=True)
    group.sudo(f"ln -s {codebase.build_dir}/{build_name} {codebase.build_dir}/current", user="evergreen", warn=warn_only, hide=True)
    prev = {}
    for conn in prev_result:
        prev[conn] = prev_result[conn].stdout.strip()
    return prev

def _send_notification(build_name)
    recipient = sp.check_output("git config user.email", shell=True).decode().strip()
    mail_cmd = f"mail -s 'deployed {build_name}' {recipient}"
```

To walk through the replacements:

- `with cd` replaced by using absolute paths
- `puts` replaced with regular old `print`
- `local` replaced with `sp.run` wrapper

Task flow is also different.
In fab1, I defined a `@runs_once` task, `select`, where I `execute` a `@parallel` task, `_select`.
This allows me to do some things once, and parallelize other things across all specified hosts.

In fabric2, I was able to achieve the same thing in a somewhat cleaner way by using [Groups](https://docs.fabfile.org/en/2.6/api/group.html).

As my code has aged (like wine, of course!), I have found the modularity this enables to be useful.
Take the following batch feature, which I implemented to stagger restarts rather than doing them all at once.

## Friendship Ended With Thread Pool, Now Batching Is My Best Friend

In line with my experience, fabric2 eliminated a useful feature, thread pool limits, and also enabled a useful solution to the problem that turned out being better than the original.
In the execution model used under fabric1, a task is run as a unit under a particular set of host and environment variables, concurrently with other tasks being run with different host parameters.
If this was still the case, I would have had to use a workaround where I import `threading` and use `threadLimiter.acquire()` at the top of my script.
Instead, I was able to replace a single call to `group.sudo` with a wrapper function, and leave the rest of the script without any thread limits.
This allowed me to run only the app restart in batches to ensure uptime.
Crucially, it was only possible because of how fabric2 allows you to pass around explicit connections from group to group.

```python
def batch_sudo_cmd(cmd, kwargs=None, batches=None, group=None):
    """batch a command by splitting up group into subgroups and running them sequentially.
    This is useful so that, e.g. we do not restart all the app servers at once"""
    if batches is None or batches < 1:
        batches = 4

    if group is None:
        group = runtime.rungroup
    grouptype = type(group)
    batch_size = len(group)//batches
    if batch_size == 0:
        batch_size = 1
    subgroups = []
    for i in range(0, len(group), batch_size):
        temp_group = grouptype()
        temp_group.extend(group[i:i+batch_size])
        subgroups.append(temp_group)

    for subgroup in subgroups:
        subgroup.sudo(cmd, **kwargs)
```

## Cursed Roles Workaround

Maybe _cursed_ is a strong word, but it's at least **SpOoKy**.

```python
# use this one file for multiple projects
codebase_name = sp.run("basename `pwd`", shell=True, capture_output=True).stdout.decode().strip()
codebase = __import__(codebase_name)

# helper class for roles
class Runtime:
    def __init__(self):
        self.active_role = None
        self.canary = None
        self.rungroup = None

runtime = Runtime()

@task(help={
    "role": "Name of the group of servers to operate on, overrides hostlist",
    "host": "custom list of hosts. Role will automatically be set. --host host1 --host host2",
    "serial": "boolean value. If not present, default is to run in parallel where possible",
    },
    iterable = ["host"],
    )
def set_role(c, role=None, host=None, serial=False):
    """ set --role <staging, prod> or delineate hosts with --host <host1> --host <host2>"""
    if role:
        hosts = codebase.roledefs[role]["hosts"]
    elif host:
        if isinstance(host, str):
            hosts = [host]
            role = _check_hosts_in_role(host)
        else:
            hosts = host
            role = _check_hosts_in_role(hosts[0])
    else:
        raise Exit("must define either role or hostlist")
    runtime.active_role = role
    if serial:
        runtime.rungroup = SerialGroup()
    else:
        runtime.rungroup = ThreadingGroup()

    # default group constructor is serial and each connection takes 10 seconds to start up,
    # so this is needed
    async def get_connection(host):
        loop = asyncio.get_event_loop()
        conn = await loop.run_in_executor(concurrent.futures.ThreadPoolExecutor(), Connection, host)
        return conn

    async def populate_group(hosts, group):
        conns = await asyncio.gather(*[get_connection(host) for host in hosts])
        runtime.canary = conns[0]
        group.extend(conns)

    asyncio.run(populate_group(hosts, runtime.rungroup))

@task
def is_role_set(c):
    """helper function to ensure role is set before running other tasks"""
    if runtime.active_role is None:
        raise Exit("set-role first!")
```

As mentioned elsewhere, Groups can be operated on as if they are lists of Connections, but the default constructor creates connections using a serial list comprehension and so has a runtime of (# Connections * 10 seconds). As group construction is an essential part of setup, this is not acceptable. I fixed this by wrapping the creation of connections with asyncio for largely concurrent execution, which gives a runtime more on the order of 10 seconds rather than 200.


## Blessed Retry Logic 

Having explicit Groups is awesome.
It allows you to do cool stuff like this:

```python
def retry_cmd(cmd, retries, succeedmsg, failmsg, group=None):
    """ retry command retries+1 times,
    returns as soon as commands succeed on all hosts"""
    if group is None:
        group = runtime.rungroup
    result = group.run(cmd, hide=True, warn=True)
    if all(r.exited==0 for r in result.values()):
        print(succeedmsg)
        return

    grouptype = type(group)
    failgroup = grouptype()
    for connection in result:
        if result[connection].exited!=0:
            failgroup.append(connection)

    for retry in range(retries):
        result = failgroup.run(cmd, hide=True, warn=True)
        if all(r.exited==0 for r in result.values()):
            print(succeedmsg)
            return
        else:
            time.sleep(10)

        for connection in result:
            if result[connection].exited==0 and connection in failgroup:
                failgroup.remove(connection)
    print(f"{failmsg} on the following hosts:")
    for failure in failgroup:
        print(failure)
    raise Exit(f"{failmsg} after {retries} attempts")
```

This assumes a fundamentally reliable network connection.
If you need to handle more gnarly retries, you may want to check out the result.failed dict, which contains total failures of remote command execution instead of commands that were executed remotely but simply errored or failed.

You could also use a similar pattern to this to only update files on hosts where the file differs from a template file on your deploy machine.

## Conclusion

This was more difficult than I expected, but not so difficult that I abandoned fabric and started using Ansible or wrote something into one of our go codebases, which were the other two main options.
Hopefully these notes will be useful to anyone who decides to stick with fabric.
If I had to do it again, I would have given more serious consideration to configuration management tools mentioned in [this article](https://gitlab.torproject.org/tpo/tpa/team/-/wikis/howto/fabric/#alternatives-considered).
That being said, I hear that pyinfra has poor performance, and a faster alternative, transilience, is relatively new and unproven.

Ultimately, I am satisfied with my fabric codebase, and I hope my notes help you all improve your own fabric codebases.

{% if page.comments %}
<div id="disqus_thread"></div>
<script>
    /**
    *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
    *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables    */
    /*
    var disqus_config = function () {
    this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
    this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
    };
    */
    (function() { // DON'T EDIT BELOW THIS LINE
    var d = document, s = d.createElement('script');
    s.src = 'https://https-hhoke-github-io-blog.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
    })();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
{% endif %}
