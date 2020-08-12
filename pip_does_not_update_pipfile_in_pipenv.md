You may think pipenv works like this:                       
                                                            
```                                                         
pipenv install --python 3.6                                 
pipenv shell                                                
pip install requests fabric                                 
```                                                         
                                                            
That is, in a manner somewhat analogous to virtualenv. This is technically true, but is a bad way to use pipenv.
                                                            
This will create a working environment inside your virtualenv. You will be able to use the things you install. However, *this will not update your Pipfile*. If you have made this error, like I did, here is how to fix:
                                                            
`pipenv graph` and take note of the bolded dependencies you need
                                                            
`pipenv install <your dependencies>`                        
`pipenv install <your dev dependencies> --dev`                        
                                                            
Now you should have a Pipfile that you can actually share.  

(pipenv, version 2018.11.26, GNU bash, version 3.2.57(1)-release, maxOS High Sierra 10.13.6)
